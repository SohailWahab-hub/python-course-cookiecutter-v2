import sys
from pathlib import Path

THIS_DIR = Path(__file__).parent
# \cookie-cutter\python-course-cookiecutter-v2 - since we are running from the root python-course-cookiecutter-v2
TEST_DIR_PARENT = (THIS_DIR / "..").resolve()

"""
insert this dir (tests) one directory up (pythonb course dir) at the zero element of the python path
"""
sys.path.insert(0, str(TEST_DIR_PARENT))

# set up paths to our files and imports them
pytest_plugins = [
    "tests.fixtures.projects_dir"
]