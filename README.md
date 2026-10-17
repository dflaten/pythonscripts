# pythonscripts
Repository for Python Scripts.

## Deleting Buckets from S3.

`delete_s3_bucket_cli.py`

This script calls an aws account (uses default credentials stored in .aws) to
retrieve the S3 buckets in an account and delete any buckets that contain a
prefix dfined in the Script. 

This script could be used as a base to automate actions via CLI commands in
general and are not specific to this use case.

## Development Setup (uv)

This project uses [uv](https://docs.astral.sh/uv/) for Python version and dependency management, and `ruff` + `ty` for linting/formatting and type checking.

**Requirements:** Python >=3.13, uv >=0.10.12

### Quick start

```bash
# Install uv (if needed)
curl -LsSf https://astral.sh/uv/install.sh | sh   # or: pip install uv / brew install uv

# Sync dependencies (creates .venv with ruff + ty)
uv sync --dev

# Run any script with the project environment
uv run python scripts/delete_s3_bucket_cli.py
uv run python learning/dataStructuresAlgos/lists.py
uv run python learning/state_machine/state_machine.py
# or directly:
uv run scripts/delete_s3_bucket_cli.py   # if executable + PEP 723 metadata

# Or activate the venv manually
source .venv/bin/activate
python scripts/delete_s3_bucket_cli.py
```

Python version is pinned in `.python-version` (3.13). `uv run` and `uv sync` will automatically use/download the correct interpreter.

### Lint / Format (ruff 0.17.1)

```bash
uv run ruff check .            # lint
uv run ruff check --fix .      # lint + autofix
uv run ruff format .           # format
uv run ruff format --check .   # check formatting without writing
```

Configuration lives in `pyproject.toml` under `[tool.ruff]` and `[tool.ruff.format]` / `[tool.ruff.lint]` (target-version `py313`, line-length 88).

### Type check (ty 0.0.89)

```bash
uv run ty check                # type check scripts/ + learning/
uv run ty check --help         # options
```

Configuration lives in `pyproject.toml` under `[tool.ty]` (python-version 3.13, relaxed overrides for `learning/**`).

### Managing dependencies

```bash
uv add <package>               # add runtime dependency
uv add --dev <package>         # add dev dependency (e.g., pytest)
uv remove <package>
uv sync --upgrade              # update lockfile
uv lock                        # re-resolve without installing
uv tree                        # show dependency tree
```

The lockfile `uv.lock` is committed for reproducible installs. `.venv/`, `.ruff_cache/`, etc. are gitignored.

### Project layout

```
.
├── pyproject.toml      # project + tool config (ruff, ty, uv)
├── .python-version     # pinned Python 3.13
├── uv.lock             # reproducible lockfile
├── scripts/            # runnable CLI scripts
│   └── delete_s3_bucket_cli.py
└── learning/           # educational examples
    ├── advanced/
    ├── dataStructuresAlgos/
    ├── oop/
    └── state_machine/
```

### CI suggestion

```yaml
- uses: astral-sh/setup-uv@v6
- run: uv sync --dev
- run: uv run ruff check .
- run: uv run ruff format --check .
- run: uv run ty check
```
