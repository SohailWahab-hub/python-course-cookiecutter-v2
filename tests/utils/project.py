import subprocess
from pathlib import Path

from tests.const import PROJECT_DIR


def initialize_git_repo(repo_dir: Path):
    # git init
    subprocess.run(
        [
            "git",
            "init",
        ],
        cwd=repo_dir,
        check=True,
    )
    # commit to the contents 'main' branch
    subprocess.run(["git", "branch", "-M", "main"], cwd=repo_dir, check=True)
    subprocess.run(["git", "add", "--all"], cwd=repo_dir, check=True)
    subprocess.run(["git", "commit", "-m", "'feat: inital commit by pytest'"], cwd=repo_dir, check=True)


def generate_project() -> Path:
    """
    helper function to execute: cookie cutter template directory
    """
    cmd = ["cookiecutter", str(PROJECT_DIR), "--output-dir", str(PROJECT_DIR / "sample")]

    cookiecutter_process = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    cookiecutter_process.stdin.write("test-repo\n".encode())
    cookiecutter_process.stdin.flush()

    _, error = cookiecutter_process.communicate(timeout=2.00)

    if error:
        exit(1)

    generated_repo_dir = PROJECT_DIR / "sample/test-repo"
    return generated_repo_dir
