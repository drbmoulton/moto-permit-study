// Checks the pure study logic (scoring, picking, merging saved progress) in the built page.
// Run after building: node scripts/test_logic.js
'use strict';
const fs = require('fs');
const path = require('path');
const vm = require('vm');
const assert = require('assert');

const html = fs.readFileSync(path.join(__dirname, '..', 'index.html'), 'utf8');
const grab = (id) => {
  const m = html.match(new RegExp('<script id="' + id + '"[^>]*>([\\s\\S]*?)</script>'));
  if (!m) throw new Error('missing script #' + id);
  return m[1];
};
const bank = JSON.parse(grab('bank'));
const ctx = vm.createContext({});
vm.runInContext(grab('logic'), ctx);
const L = ctx.MPP;
new vm.Script(grab('ui')); // syntax check of the UI script

// Seeded random so runs are repeatable.
function rng(seed) { let s = seed >>> 0; return () => ((s = (s * 1664525 + 1013904223) >>> 0) / 4294967296); }

const mods = bank.modules;
const counts = mods.map((m) => m.questions.length);
const alloc = L.allocate(counts, 25);
assert.strictEqual(alloc.reduce((a, b) => a + b, 0), 25, 'allocation sums to 25');
alloc.forEach((n, i) => assert.ok(Math.abs(n - counts[i] * 25 / counts.reduce((a, b) => a + b, 0)) < 1, 'allocation within 1 of the exact share'));
assert.deepStrictEqual(Array.from(L.allocate([3, 1], 4)), [3, 1]);
assert.deepStrictEqual(Array.from(L.allocate([], 25)), []);

for (let seed = 1; seed <= 50; seed++) {
  const ids = L.pickExam(mods, {}, 25, rng(seed));
  assert.strictEqual(ids.length, 25);
  assert.strictEqual(new Set(ids).size, 25, 'no repeated questions');
  mods.forEach((m, i) => assert.strictEqual(ids.filter((id) => id.startsWith(m.id + '-')).length, alloc[i]));
}
// Least-seen questions come first within a section.
const seen = {};
mods[0].questions.forEach((q, i) => { if (i >= 2) seen[q.id] = { a: 3, c: 3, s: 3, l: 1, t: 1 }; });
const ex = L.pickExam(mods, seen, 25, rng(7));
const m1picked = ex.filter((id) => id.startsWith('m1-')).sort();
assert.deepStrictEqual(JSON.parse(JSON.stringify(m1picked)), [mods[0].questions[0].id, mods[0].questions[1].id].sort());

// Quick 10 puts missed questions in.
const all = mods.flatMap((m) => m.questions.map((q) => q.id));
const qs = {};
all.forEach((id) => { qs[id] = { a: 1, c: 1, s: 1, l: 1, t: 1 }; });
['m3-04', 'm8-11', 'm9-02'].forEach((id) => { qs[id] = { a: 2, c: 0, s: 0, l: 0, t: 5 }; });
const quick = L.pickQuick(all, qs, 10, rng(3));
assert.strictEqual(quick.length, 10);
assert.strictEqual(new Set(quick).size, 10);
['m3-04', 'm8-11', 'm9-02'].forEach((id) => assert.ok(quick.includes(id), id + ' in Quick 10'));

// Recording answers.
const st = L.emptyState();
L.recordAnswer(st, 'm1-01', true, 10);
L.recordAnswer(st, 'm1-01', true, 20);
L.recordAnswer(st, 'm1-01', false, 30);
assert.deepStrictEqual(JSON.parse(JSON.stringify(st.q['m1-01'])), { a: 3, c: 2, s: 0, l: 0, t: 30 });
L.recordSection(st, 'm1', 12, 15, 40);
L.recordSection(st, 'm1', 10, 15, 50);
assert.strictEqual(st.sections.m1.best, 12);
assert.strictEqual(st.sections.m1.last, 10);
assert.strictEqual(st.sections.m1.n, 2);

// Merging two copies of progress.
const a = L.emptyState(); const b = L.emptyState();
a.q['m2-01'] = { a: 1, c: 1, s: 1, l: 1, t: 100 };
b.q['m2-01'] = { a: 2, c: 1, s: 0, l: 0, t: 200 };
a.q['m2-02'] = { a: 1, c: 0, s: 0, l: 0, t: 50 };
a.tests.push({ id: 'x', at: 1, dur: 5, score: 20, total: 25, timedOut: false, byMod: {}, items: [['m1-01', 0]] });
b.tests.push({ id: 'y', at: 2, dur: 5, score: 15, total: 25, timedOut: false, byMod: {}, items: [['m1-01', 1]] });
b.tests.push({ id: 'x', at: 1, dur: 5, score: 20, total: 25, timedOut: false, byMod: {}, items: [['m1-01', 0]] });
a.sections.m2 = { best: 14, last: 14, total: 16, n: 1, at: 10 };
b.sections.m2 = { best: 12, last: 12, total: 16, n: 2, at: 20 };
const plain = (x) => JSON.parse(JSON.stringify(x));
const ab = L.mergeStates(a, b), ba = L.mergeStates(b, a);
assert.strictEqual(L.canon(ab), L.canon(ba), 'merge is order-independent');
assert.strictEqual(ab.q['m2-01'].t, 200, 'newer answer wins');
assert.ok(ab.q['m2-02'], 'answers only on one side are kept');
assert.deepStrictEqual(plain(ab.tests.map((t) => t.id)), ['x', 'y'], 'tests unioned once each');
assert.deepStrictEqual(JSON.parse(JSON.stringify(ab.sections.m2)), { best: 14, last: 12, total: 16, n: 2, at: 20 });
assert.strictEqual(L.canon(L.mergeStates(ab, ab)), L.canon(ab), 'merge is idempotent');
assert.strictEqual(L.canon(L.normalize('junk')), L.canon(L.emptyState()));
assert.strictEqual(L.canon(L.normalize({ q: { x: 5 }, tests: [null, { id: 3 }] })), L.canon(L.emptyState()));

// Scoring.
const answerOf = (id) => ({ 'm1-01': 2, 'm1-02': 0, 'm2-01': 1 })[id];
const modOf = (id) => id.split('-')[0];
const sc = L.scoreItems([['m1-01', 2], ['m1-02', null], ['m2-01', 3]], answerOf, modOf);
assert.strictEqual(sc.score, 1);
assert.deepStrictEqual(JSON.parse(JSON.stringify(sc.byMod)), { m1: [1, 2], m2: [0, 1] });

// Display helpers.
assert.strictEqual(L.fmtClock(25 * 60 * 1000), '25:00');
assert.strictEqual(L.fmtClock(59001), '1:00');
assert.strictEqual(L.fmtClock(-5), '0:00');
assert.strictEqual(L.pageRanges([27, 28, 29, 30, 31, 49, 50]), '27–31, 49–50');
assert.strictEqual(L.pageRanges([48, 51, 52]), '48, 51–52');

console.log('logic checks passed:', all.length, 'questions,', 'allocation', alloc.join('/'));
