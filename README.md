# Python Repo Template

An opinionated [Cookiecutter](https://cookiecutter.readthedocs.io/) template for
Python projects built on the [Astral](https://astral.sh/) toolchain:
[uv](https://docs.astral.sh/uv/) for dependency management,
[Ruff](https://docs.astral.sh/ruff/) for linting and formatting, and
[ty](https://docs.astral.sh/ty/) for optional static type checking.

## Usage

Generate a new project straight from GitHub. With `uv` (nothing to install):

```bash
uvx cookiecutter gh:aleksey-karasev/python-astral-template
```

Or with Cookiecutter already installed:

```bash
cookiecutter gh:aleksey-karasev/python-astral-template
```

You will be prompted for:

| Prompt                | Description                                            | Default               |
| --------------------- | ------------------------------------------------------ | --------------------- |
| `project_name`        | Human-readable project name                            | `Project name`        |
| `project_slug`        | Package/folder name (auto-derived from `project_name`) | *(derived)*           |
| `project_description` | Short description                                      | `Project description` |
| `author_name`         | Used in the generated `LICENSE`                        | `Your Name`           |
| `python_version`      | Target Python version (choose from the list)           | `3.12`                |
| `use_type_checking`   | Include `ty` type checking (`y`/`n`)                   | `y`                   |
| `use_pre_commit`      | Include the `pre-commit` config (`y`/`n`)              | `y`                   |

## What gets generated

```text
<project_slug>/
├── .env.example
├── .gitignore
├── .pre-commit-config.yaml  # only when pre-commit is enabled
├── .python-version          # pins the chosen Python version
├── LICENSE                  # MIT, filled with author + current year
├── CLAUDE.md
├── README.md
├── markdownlint.json
├── pyproject.toml           # uv-managed; ruff (+ ty, pre-commit if enabled) in the dev group
├── ruff.toml
├── taplo.toml               # TOML formatting; only when pre-commit is enabled
└── ty.toml                  # only when type checking is enabled
```

The generator also runs `git init`, `uv venv`, and — when pre-commit is enabled and the
`pre-commit` binary is on `PATH` — `pre-commit install`. Each step is optional: a missing
tool prints a hint instead of failing the generation.
