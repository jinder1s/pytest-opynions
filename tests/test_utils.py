"""
Tests to make sure the utils for pytest-repo-health plugins work correctly.
"""

import git

from pytest_repo_health.utils import get_git_origin_url


def test_get_git_origin_url_on_non_git_dir(tmpdir):
    """
    Verify that the non git directory returns None on getting origin URL through get_git_origin_url
    """
    repo_dir = tmpdir / "target-repo"
    response = get_git_origin_url(repo_dir)
    assert response is None


def test_get_git_origin_url_without_origin_set(tmpdir):
    """
    Verify that the git repository without remote "origin" set returns None
    on getting origin URL through get_git_origin_url
    """
    repo_dir = tmpdir / "target-repo"
    repo = git.Repo.init(repo_dir)
    response = get_git_origin_url(repo_dir)
    assert response is None


def test_get_git_origin_url_with_origin_set(tmpdir):
    """
    Verify that the origin URL is retrieved through get_git_origin_url on valid git repository with origin set
    """
    url = "https://github.com/edx/pytest-repo-health.git"
    repo_dir = tmpdir / "target-repo"
    repo = git.Repo.init(repo_dir)
    repo.create_remote("origin", url=url)
    response = get_git_origin_url(repo_dir)
    assert response == url
