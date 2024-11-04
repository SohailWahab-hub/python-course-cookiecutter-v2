from pathlib import Path
from typing import Generator


def test_can_generate_project(project_dir: Path):        
    assert project_dir.exists()