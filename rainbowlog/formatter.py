import logging
from typing import Any, Mapping, Union
from colors import color
from .ansi import Color, Format, Style


default_config = {
    logging.DEBUG: Format(style=Style.FAINT),
    logging.INFO: Format(foreground=Color.GREEN),
    logging.WARNING: Format(foreground=Color.YELLOW),
    logging.ERROR: Format(foreground=Color.RED),
    logging.CRITICAL: Format(foreground=Color.RED, style=[Style.BOLD, Style.UNDERLINE]),
}

default_exception_config = default_config[logging.CRITICAL]
default_stack_config = default_config[logging.ERROR]


class Formatter(logging.Formatter):
    """This log formatter wraps a given formatter and adds color to the output.

    If you want to use different colors from the default ones, you can pass a mapping to the color_configs argument in the constructor. This mapping should be from log levels (ints) to Format objects.

    Note: Instead of Format objects, you can pass any mapping acceptable as keyword arguments for the ansicolors library's color function. You can find more information on this library here: https://github.com/jonathaneunice/colors.
    """

    def __init__(
        self,
        inner_formatter: logging.Formatter,
        color_configs: Mapping[int, Mapping[str, Any]] = default_config,
        exception_config: Mapping[str, Any] = default_exception_config,
        stack_config: Mapping[str, Any] = default_stack_config,
    ):
        """
        Args:
            inner_formatter: The formatter to use for the log messages.
            color_configs: A mapping from log levels to Format objects.
            exception_config: The Format for exceptions.
            stack_config: The Format for stack traces.
        """
        self.formatter = inner_formatter
        self.configs = color_configs
        self.exception_config = exception_config
        self.stack_config = stack_config

    def format(self, record: logging.LogRecord) -> str:
        return color(
            self.formatter.format(record), **self.configs.get(record.levelno, {})
        )

    def formatException(self, exc_info):
        return color(self.formatter.formatException(exc_info), **self.exception_config)

    def formatStack(self, stack_info):
        return color(self.formatter.formatStack(stack_info), **self.stack_config)
