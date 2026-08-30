import os
import subprocess

use_type_checking = "{{ cookiecutter.use_type_checking }}"
use_pre_commit = "{{ cookiecutter.use_pre_commit }}"


def remove_files(*paths):
    """Drop config files belonging to tooling the user opted out of."""
    for path in paths:
        if os.path.exists(path):
            os.remove(path)


if use_type_checking == "n":
    remove_files("ty.toml")

if use_pre_commit == "n":
    remove_files(".pre-commit-config.yaml", "taplo.toml")


def init_git_repo():
    """Initialize a fresh git repository for the generated project."""
    try:
        subprocess.run(["git", "init", "-b", "main"], check=True)
    except subprocess.CalledProcessError:
        subprocess.run(["git", "init"], check=False)
    except FileNotFoundError:
        print("git not found; skipping repository initialization.")
        return


def create_venv():
    """Create a virtual environment using the pinned Python version."""
    try:
        subprocess.run(["uv", "venv"], check=True)
    except subprocess.CalledProcessError:
        print("uv venv failed; skipping virtual environment creation.")
    except FileNotFoundError:
        print("uv not found; skipping virtual environment creation.")


def install_pre_commit_hooks():
    """Register the git hooks so the very first commit is already checked."""
    if use_pre_commit == "n":
        return
    hint = "Run `uv sync && uv run pre-commit install` to enable the hooks."
    try:
        subprocess.run(["pre-commit", "install"], check=True)
    except subprocess.CalledProcessError:
        print("pre-commit install failed. " + hint)
    except FileNotFoundError:
        print("pre-commit not found on PATH. " + hint)


init_git_repo()
create_venv()
install_pre_commit_hooks()
