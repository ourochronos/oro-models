"""Smoke test — verify the package imports correctly."""

from our_models import __version__


def test_version_is_set() -> None:
    assert __version__ == "0.1.0"
