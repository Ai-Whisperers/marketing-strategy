#!/usr/bin/env node
/**
 * Documentation coverage audit for the Marketing repository.
 * Compares README files against expected sections and reports gaps.
 *
 * Usage:
 *   node ./mcp-servers/doc-coverage-audit.js [--json] [--root <path>]
 */

const fs = require('fs');
const path = require('path');

const DEFAULT_ROOT = path.resolve(__dirname, '..');

const EXPECTED_SECTIONS = [
  { pattern: /^#\s+.+/m, label: 'Title (H1)' },
  { pattern: /^##\s+(overview|about|purpose|summary)/im, label: 'Overview or purpose section' },
  { pattern: /^##\s+(getting started|quick start|navigation)/im, label: 'Getting started or navigation' },
];

const SKIP_DIRS = new Set([
  'node_modules',
  '.git',
  '.venv',
  'venv',
  'env',
  '_archived',
  '.cursor',
  '.specstory',
  'scripts/dependency-reports',
  'logs',
  'enhanced-documentation',
]);

function parseArgs(argv) {
  const opts = { json: false, root: DEFAULT_ROOT, minScore: 50 };
  for (let i = 2; i < argv.length; i++) {
    if (argv[i] === '--json') opts.json = true;
    else if (argv[i] === '--root' && argv[i + 1]) opts.root = path.resolve(argv[++i]);
    else if (argv[i] === '--min-score' && argv[i + 1]) opts.minScore = Number(argv[++i]);
  }
  return opts;
}

function walkMarkdownFiles(dir, files = []) {
  if (!fs.existsSync(dir)) return files;
  for (const entry of fs.readdirSync(dir, { withFileTypes: true })) {
    const full = path.join(dir, entry.name);
    const rel = path.relative(DEFAULT_ROOT, full).replace(/\\/g, '/');
    if (entry.isDirectory()) {
      if (SKIP_DIRS.has(entry.name)) continue;
      if (rel.split('/').some((p) => SKIP_DIRS.has(p))) continue;
      walkMarkdownFiles(full, files);
    } else if (entry.isFile() && /^readme\.md$/i.test(entry.name)) {
      files.push(full);
    }
  }
  return files;
}

function scoreReadme(content, relPath) {
  const isHub = /AI-Whisperers-Marketing-Hub\/README\.md$/i.test(relPath.replace(/\\/g, '/'));
  const isRoot = /^readme\.md$/i.test(path.basename(relPath)) && !relPath.includes(path.sep);
  const required = isRoot || isHub ? EXPECTED_SECTIONS : EXPECTED_SECTIONS.slice(0, 1);
  const missing = [];
  for (const section of required) {
    if (!section.pattern.test(content)) missing.push(section.label);
  }
  const score = Math.round(((required.length - missing.length) / required.length) * 100);
  return { score, missing, tier: isRoot || isHub ? 'primary' : 'nested' };
}

function main() {
  const opts = parseArgs(process.argv);
  const files = walkMarkdownFiles(opts.root);
  const results = files.map((file) => {
    const content = fs.readFileSync(file, 'utf8');
    const rel = path.relative(opts.root, file);
    const audit = scoreReadme(content, rel);
    return {
      file: rel.replace(/\\/g, '/'),
      ...audit,
      pass: audit.score >= opts.minScore,
    };
  });

  results.sort((a, b) => a.score - b.score);

  if (opts.json) {
    console.log(JSON.stringify({ root: opts.root, count: results.length, results }, null, 2));
    process.exit(results.some((r) => !r.pass) ? 1 : 0);
    return;
  }

  console.log('Documentation coverage audit');
  console.log(`Root: ${opts.root}`);
  console.log(`Files: ${results.length}`);
  console.log('');

  for (const r of results) {
    const status = r.pass ? 'PASS' : 'GAP';
    console.log(`[${status}] ${r.score}%  ${r.file} (${r.tier})`);
    if (r.missing.length) {
      for (const m of r.missing) console.log(`       - missing: ${m}`);
    }
  }

  const failed = results.filter((r) => !r.pass);
  console.log('');
  if (failed.length) {
    console.log(`Summary: ${failed.length} README(s) below ${opts.minScore}% threshold.`);
    process.exit(1);
  }
  console.log('Summary: All audited README files meet the coverage threshold.');
}

main();
