import subprocess
from pathlib import Path

import pytest

"""
set up:
1. generate a project using cookie cutter
2. create  virtual environment and install project dependencies
-------
Tests:
3. run tests
4. linting

Cleanup/Teardown
5. remove virtual environment
"""

"""
test that the linting passes, passing in the project fixture function
"""


@pytest.skip("skipping test_linting_passes", allow_module_level=True)
def test_linting_passes(project_dir: Path):
    cmd = ["make", "lint-ci"]
    subprocess.run(cmd, cwd=project_dir, check=True)


@pytest.skip("skipping test_tests_passes", allow_module_level=True)
def test_tests_passes(project_dir):
    subprocess.run(["make", "install"], cwd=project_dir, check=True)
    subprocess.run(["make", "test"], cwd=project_dir, check=True)


# @pytest.skip("skipping test_install_succeeds")
# def test_install_succeeds():
#     pass
