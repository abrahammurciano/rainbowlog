import pytest
import logging
from colors import color
from typing import Any, Mapping
from rainbowlog import Formatter, Format, Style, Color


@pytest.fixture(
    params=[
        pytest.param(
            {
                logging.DEBUG: {"fg": "grey", "style": "bold"},
                logging.INFO: {"fg": "green", "style": "bold+italic+negative"},
                logging.WARNING: {"fg": "yellow", "style": "underline+italic"},
                logging.ERROR: {"fg": "red", "style": "italic+blink"},
                logging.CRITICAL: {
                    "fg": "red",
                    "bg": "white",
                    "style": "bold+italic+underline",
                },
            },
            id="dict",
        ),
        pytest.param(
            {
                logging.DEBUG: Format(Color.BLUE, style=Style.FAINT),
                logging.INFO: Format(Color.GREEN),
                logging.WARNING: Format(Color.YELLOW, style=Style.ITALIC),
                logging.ERROR: Format(Color.RED, Color.WHITE, Style.BOLD),
                logging.CRITICAL: Format(
                    Color.RED, Color.YELLOW, (Style.BOLD, Style.UNDERLINE)
                ),
            },
            id="Format",
        ),
    ]
)
def color_configs(request) -> Mapping[str, Any]:
    return request.param


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
def color_config(
    color_configs: Mapping[int, Mapping[str, Any]], level: int
) -> Mapping[str, Any]:
    return color_configs[level]


@pytest.fixture
def formatter(color_configs: Mapping[int, Mapping[str, Any]]) -> Formatter:
    return Formatter(logging.Formatter("%(message)s"), color_configs=color_configs)


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
    color_config: Mapping[str, Any],
    record: logging.LogRecord,
    message: str,
) -> None:
    assert formatter.format(record) == color(message, **color_config)
