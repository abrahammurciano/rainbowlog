import logging
from typing import Callable, Mapping
from constyle import Attributes


default_styles = {
    logging.DEBUG: Attributes.DIM,
    logging.INFO: Attributes.GREEN,
    logging.WARNING: Attributes.YELLOW,
    logging.ERROR: Attributes.RED,
    logging.CRITICAL: Attributes.RED + Attributes.BOLD + Attributes.UNDERLINE,
}


class Formatter(logging.Formatter):
    """This log formatter wraps a given formatter and adds color to the output.

    If you want to use different colors from the default ones, you can pass a mapping to the log_styles argument in the constructor. This mapping should be from log levels (ints) to style callable.

    A style callcable is a one which takes a string and returns a string. It should return the given string with the desired ANSI codes surrounding it. For example `[constyle.Style](https://abrahammurciano.github.io/python-constyle/constyle/#constyle.Style)` and `ansicolors.red`, `ansicolors.green`, etc. objects are good candidates.

    You can also create your own easily by using `functools.partial` or lambdas with any other library you want, or using functions which wrap a string in ANSI escape codes directly.
    """

    def __init__(
        self,
        inner_formatter: logging.Formatter = logging.Formatter(),
        log_styles: Mapping[int, Callable[[str], str]] = default_styles,
        exception_style: Callable[[str], str] = None,
        stack_style: Callable[[str], str] = None,
    ):
        """
        Args:
            inner_formatter: The formatter to use for the log messages. Defaults to a formatter that shows just the log messages.
            log_styles: A mapping from log levels to a style callable. Defaults to sensible colours.
            exception_style: The style callable for exceptions. Defaults to `log_styles[logging.CRITICAL]`.
            stack_style: The style callable for stack traces. Defaults to `log_styles[logging.ERROR]`.
        """
        self.formatter = inner_formatter
        self.styles = log_styles
        self.exception_style = exception_style or log_styles[logging.CRITICAL]
        self.stack_style = stack_style or log_styles[logging.ERROR]

    def format(self, record: logging.LogRecord) -> str:
        return self.styles.get(record.levelno, str)(self.formatter.format(record))

    def formatException(self, exc_info):
        return self.exception_style(self.formatter.formatException(exc_info))

    def formatStack(self, stack_info):
        return self.stack_style(self.formatter.formatStack(stack_info))
