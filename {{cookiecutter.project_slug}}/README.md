# {{ cookiecutter.project_name }}

{{ cookiecutter.project_description }}

## Setup

```bash
uv sync
```

## Linting and Formatting

```bash
uv run ruff check .
uv run ruff format .
```

{%- if cookiecutter.use_type_checking == 'y' %}

## Type Checking

```bash
uv run ty check
```

{%- endif %}
{%- if cookiecutter.use_pre_commit == 'y' %}

## Pre-commit

[`pre-commit`](https://pre-commit.com/) runs ruff{% if cookiecutter.use_type_checking == 'y' %}, ty{% endif %},
[`taplo`](https://taplo.tamasfe.dev/) for TOML, `uv lock`, and a set of hygiene checks before
every commit. The generator installs the git hook for you; if you cloned this repo instead:

```bash
uv run pre-commit install
```

To check the whole tree at once, or to bump the pinned hook versions:

```bash
uv run pre-commit run --all-files
uv run pre-commit autoupdate
```

{%- endif %}
