import pytest
import logging
from constyle import Attributes as Attrs
from typing import Callable, Mapping
from rainbowlog import Formatter


@pytest.fixture
def log_styles() -> Mapping[int, Callable[[str], str]]:
    return {
        logging.DEBUG: Attrs.GREY + Attrs.BOLD,
        logging.INFO: Attrs.GREEN + Attrs.BOLD + Attrs.ITALIC + Attrs.INVERT,
        logging.WARNING: Attrs.YELLOW + Attrs.UNDERLINE + Attrs.ITALIC,
        logging.ERROR: Attrs.RED + Attrs.ITALIC + Attrs.SLOW_BLINK,
        logging.CRITICAL: (
            Attrs.RED + Attrs.ON_WHITE + Attrs.BOLD + Attrs.ITALIC + Attrs.UNDERLINE
        ),
    }


@pytest.fixture(
    params=[
        pytest.param(logging.DEBUG, id="debug"),
        pytest.param(logging.INFO, id="info"),
        pytest.param(logging.WARNING, id="warning"),
        pytest.param(logging.ERROR, id="error"),
        pytest.param(logging.CRITICAL, id="critical"),
    ]
)
def level(request) -> int:
    return request.param


@pytest.fixture
def log_style(
    log_styles: Mapping[int, Callable[[str], str]], level: int
) -> Callable[[str], str]:
    return log_styles[level]


@pytest.fixture
def formatter(log_styles: Mapping[int, Callable[[str], str]]) -> Formatter:
    return Formatter(logging.Formatter("%(message)s"), log_styles=log_styles)


@pytest.fixture
def message(level: int) -> str:
    return logging.getLevelName(level)


@pytest.fixture
def record(level: int, message: str) -> logging.LogRecord:
    return logging.LogRecord(
        "rainbowlog", level, "/path/to/file.py", 1, message, None, None
    )


def test_format(
    formatter: Formatter,
    log_style: Callable[[str], str],
    record: logging.LogRecord,
    message: str,
) -> None:
    assert formatter.format(record) == log_style(message)
