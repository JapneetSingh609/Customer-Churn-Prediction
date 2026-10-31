# Contributing

Useful documentation contributions make the experiment easier to inspect,
explain, and reproduce without changing its historical evidence. Start with
the [README](README.md), [evidence map](docs/evidence.md), and
[reproduction boundaries](docs/reproduction.md).

## Scope of documentation changes

Good contributions include correcting a claim with a saved-cell reference,
clarifying setup for an operating system, documenting a verified data source,
improving accessible descriptions, or repairing a broken link.

For a documentation-only contribution, preserve these files byte-for-byte:

- Existing `.py` and `.ipynb` files, including notebook Markdown, metadata, and
  saved outputs.
- Datasets, trained/serialized artifacts, and existing evaluation images.
- `requirements.txt` and `LICENSE`.

Edit `README.md`, add supporting Markdown under `docs/`, or propose a focused
improvement to this guide. The new hero asset is
`Images/customer-intelligence-banner.svg`; keep it self-contained and static.
Do not rerun training or regenerate evaluation charts to validate prose.
Discuss experimental implementation changes as a separate scope, with their
own data provenance and evaluation plan.

## Make claims reviewable

1. Cite the file and notebook cell position supporting a technical claim. The
   evidence map uses one-based positions including Markdown cells; execution
   counters are a different numbering system.
2. Separate saved values, arithmetic derived from saved counts, interpretations,
   and proposed future work. Preserve report rounding when quoting results.
3. State the class and averaging convention for precision, recall, and F1.
   Do not label macro or weighted averages as churn-class scores.
4. Identify missing evidence explicitly. A candidate dataset URL is not a
   verified original source; matching dimensions do not prove matching bytes.
5. Keep roadmap entries marked unimplemented until the corresponding work and
   evaluation evidence exist. Do not claim a deployed product or business
   impact from this notebook alone.

## Review and local validation

Record your starting commit and working-tree state before editing:

```bash
git rev-parse HEAD
git status --short
```

Preserve unrelated local changes. For a protection check, compare SHA-256
values with the [preservation baseline](docs/evidence.md#preservation-baseline).
Windows provides `Get-FileHash -Algorithm SHA256`; Linux provides `sha256sum`,
and macOS provides `shasum -a 256`. Hash the files before and after your change.
Line-ending conversion also changes bytes, so avoid tools that resave notebooks
or format protected files on open.

Before committing:

- Read the whole diff and check that every changed file belongs to your scope.
- Verify relative links from the containing Markdown file, including heading
  fragments, capitalization, and all image paths.
- Confirm tables and code fences render cleanly. Check that the Mermaid
  diagram still matches the actual fit/transform and train/test boundaries.
- Inspect presentation at desktop and narrow widths when preview tooling is
  available. State which renderer you used; local HTML is not proof of GitHub
  rendering.
- Run the whitespace and staged-diff checks below. No ML execution is needed
  for documentation validation.

```bash
git diff --check
git diff --name-only
git diff --cached --check
git diff --cached
```

Stage individual, reviewed paths instead of using a blanket `git add .`.
Exclude local environments, downloaded CSVs, notebook checkpoints, temporary
previews, and newly generated plots. If a protected file changes unexpectedly,
stop and investigate; do not automatically reset someone else's changes.

## Commit and review notes

Use one commit per useful improvement, with a concise Conventional Commit
message, for example `docs: clarify saved churn-class metrics`. Avoid empty
commits and splitting a tiny change to increase contribution counts. Preserve
Git author information and ordinary commit timestamps.

A review description should state the original documentation problem, the
corrected behavior or explanation, the evidence used, validation performed, and
remaining uncertainties. Include the changed-file list and disclose whether
any experiment was executed. Never describe an unexecuted setup command as a
successful reproduction.

[Return to the project README](README.md)
