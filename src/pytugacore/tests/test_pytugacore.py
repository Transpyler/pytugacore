import pytest
import pytugacore


def test_project_defines_author_and_version():
    assert hasattr(pytugacore, '__author__')
    assert hasattr(pytugacore, '__version__')
