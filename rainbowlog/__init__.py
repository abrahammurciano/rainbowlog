"""
.. include:: ../README.md
"""


try:
    import importlib.metadata as importlib_metadata
except ImportError:
    import importlib_metadata as importlib_metadata  # type: ignore
try:
    __version__ = importlib_metadata.version(__package__ or __name__)
except importlib_metadata.PackageNotFoundError:
    import toml

    __version__ = (
        toml.load("pyproject.toml")
        .get("tool", {})
        .get("poetry", {})
        .get("version", "unknown")
        + "-dev"
    )

from .formatter import Formatter
from .ansi import Format, Color, Style
