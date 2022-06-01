import logging
from typing import Any, Mapping
from colors import color


default_config = {
    logging.DEBUG: {"fg": "grey", "style": "bold+italic"},
    logging.INFO: {"fg": "green", "style": "bold+italic"},
    logging.WARNING: {"fg": "yellow", "style": "bold+italic"},
    logging.ERROR: {"fg": "red", "style": "bold+italic"},
    logging.CRITICAL: {"fg": "red", "style": "bold+italic+underline"},
}

default_exception_config = default_config[logging.CRITICAL]
default_stack_config = default_config[logging.ERROR]


class Formatter(logging.Formatter):
    """This log formatter wraps a given formatter and adds color to the output.

    If you want to use different colors from the default ones, you can pass a mapping to the color_configs argument in the constructor. This mapping should be from log levels (ints) to keyword arguments for the ansicolors library's color function. You can find more information on this library here: https://github.com/jonathaneunice/colors.

    The keys that you can use for each log level are:
    - fg (string): the foreground color
    - bg (string): the background color
    - style (string): any number of styles separated by a "+"

    The available colors are "black", "red", "green", "yellow", "blue", "magenta", "cyan", "white".
    The available styles are "none", "bold", "faint", "italic", "underline", "blink", "blink2", "negative", "concealed", "crossed".
    """

    def __init__(
        self,
        inner_formatter: logging.Formatter,
        color_configs: Mapping[int, Mapping[str, Any]] = default_config,
        exception_config: Mapping[str, Any] = default_exception_config,
        stack_config: Mapping[str, Any] = defaul_stack_config,
    ):
        """
        Args:
            inner_formatter: The formatter to use for the log messages.
            color_configs: A mapping from log levels to keyword arguments for the ansicolors library's color function.
            exception_config: The keyword arguments to pass to color for formatting exceptions.
            stack_config: The keyword arguments to pass to color for formatting stack traces.
        """
        self.formatter = inner_formatter
        self.configs = color_configs

    def format(self, record: logging.LogRecord) -> str:
        return color(
            self.formatter.format(record), **self.configs.get(record.levelno, {})
        )

    def formatException(exc_info):
        return color(self.formatter.formatException(exc_info), **self.exception_config)

    def formatStack(stack_info):
        return color(self.formatter.formatStack(stack_info), **self.stack_config)
