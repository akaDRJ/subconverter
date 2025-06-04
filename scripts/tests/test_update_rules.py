from pathlib import Path
import sys
import types

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

if 'git' not in sys.modules:
    sys.modules['git'] = types.SimpleNamespace(InvalidGitRepositoryError=Exception, Repo=object)

from update_rules import update_rules


def test_update_rules_copies_files(tmp_path: Path):
    repo_dir = tmp_path / "repo"
    repo_dir.mkdir()
    (repo_dir / "folder").mkdir()

    file1 = repo_dir / "folder" / "a.txt"
    file1.write_text("a")
    file2 = repo_dir / "b.txt"
    file2.write_text("b")

    dest_dir = tmp_path / "dest"
    patterns = ["folder/*.txt", "*.txt"]

    update_rules(str(repo_dir), str(dest_dir), patterns, keep_tree=True)

    assert (dest_dir / "folder" / "a.txt").is_file()
    assert (dest_dir / "b.txt").is_file()
