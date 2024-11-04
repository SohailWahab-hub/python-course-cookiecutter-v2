import shutil
from pathlib import Path

import pytest

from tests.utils.project import (
    generate_project,
)

"""
this pyfixture function caled the generate_project function to create a project template
we can use the yeild to assert that the project exits and then use the shutil to rm it

the scope will be for the whole session or function level
of the tests that run so set up and tear down will be run the one time
"""


@pytest.fixture(scope="session")
def project_dir() -> Path:
    try:
        print("generating project template")
        generated_repo_dir = generate_project()
        # initialize_git_repo(repo_dir=generated_repo_dir)
        yield generated_repo_dir
    finally:
        shutil.rmtree(path=generated_repo_dir)


# generate one session id per test session
# def generate_test_session_id() -> str:
#     test_session_id = str(uuid())[:6]
#     return test_session_id
