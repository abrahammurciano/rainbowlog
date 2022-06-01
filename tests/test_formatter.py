import pytest
import logging
from colors import color
from typing import Any, Mapping
from rainbowlog import Formatter

color_configs = {
	logging.DEBUG: {"fg": "grey", "style": "bold"},
	logging.INFO: {"fg": "green", "style": "bold+italic+negative"},
	logging.WARNING: {"fg": "yellow", "style": "underline+italic"},
	logging.ERROR: {"fg": "red", "style": "italic+blink"},
	logging.CRITICAL: {"fg": "red", "bg": "white", "style": "bold+italic+underline"},
}

@pytest.fixture(params=[
	logging.DEBUG, logging.INFO, logging.WARNING, logging.ERROR, logging.CRITICAL
])

def level(request) -> int:
	return request.param

@pytest.fixture
def color_config(level: int) -> Mapping[str, Any]:
	return color_configs[level]

@pytest.fixture
def formatter(color_config: Mapping[str, Any]) -> Formatter:
	return Formatter(logging.Formatter("%(message)s"), color_configs=color_configs)

@pytest.fixture
def message(level: int) -> str:
	return logging.getLevelName(level)

@pytest.fixture
def record(level: int, message: str) -> logging.LogRecord:
	return logging.LogRecord('rainbowlog', level, "/path/to/file.py", 1, message, None, None)


def test_format(formatter: Formatter, color_config: Mapping[str, Any], record: logging.LogRecord, message: str) -> None:
	assert formatter.format(record) == color(message, **color_config)
