# Rainbow Log

Format your python logs with colours based on the log levels.

## Installation

You can instll the package with pip or conda.
```sh
$ pip install rainbowlog
```
```sh
$ conda install rainbowlog -c abrahammurciano
```
```sh
$ conda install rainbowlog -c conda-forge
```

## Links

* [Documentation](https://abrahammurciano.github.io/rainbowlog/rainbowlog)
* [Github](https://github.com/abrahammurciano/rainbowlog)
* [PyPI](https://pypi.org/project/rainbowlog/)

## Usage

Here's a basic example of a script that logs colorfully to the console, but regularly to a file.

```python
import logging
import rainbowlog

logger = logging.getLogger(__name__)

# This one will write to the console
stream_handler = logging.StreamHandler()

# This one will write to a file
file_handler = logging.FileHandler("output.log")

# Here we decide how we want the logs to look like
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")

# We want the stream handler to be colorful
stream_handler.setFormatter(rainbowlog.Formatter(formatter))

# We don't want the file handler to be colorful
file_handler.setFormatter(formatter)

# Finally we add the handlers to the logger
logger.addHandler(stream_handler)
logger.addHandler(file_handler)

if __name__ == "__main__":
	logger.debug("This is a debug message")
	logger.info("This is an info message")
	logger.warning("This is a warning message")
	logger.error("This is an error message")
	logger.critical("This is a critical message")
```

If you want to change the format of the logs for each log level, you can use any callable that takes a string and returns the same string with ANSI codes surrounding it. There are many libraries you can use to provide such callables.

```py
import logging
from rainbowlog import Formatter

# Here are some libraries you can use to get a style callable without dealing with ANSI codes
from constyle import Style, Attributes as Attrs
import termcolor
from functools import partial


formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
color_formatter = Formatter(
	formatter,
	log_styles={
		logging.DEBUG: Style(Attrs.BLUE, Attrs.FAINT), # An example using constyle
		logging.INFO: lambda s: f"\033[32m{s}\033[0m", # An example using lambdas
		logging.WARNING: termcolor.red, # An example using termcolor's predifined functions
		logging.ERROR: partial(termcolor.colored, color="red", on_color="on_white", attrs=["bold"]), # An example using functools.partial
		logging.CRITICAL: Attrs.RED + Attrs.ON_YELLOW + Attrs.BOLD + Attrs.UNDERLINE, # An example using constyle's added attributes
	}
	exception_style=lambda s: f"{Attrs.RED + Attrs.ON_WHITE + Attrs.BOLD}{s}{Attrs.RESET}" # An example using lambdas and constyle,
	stack_style=Attrs.RED, # An example using a single constyle attribute
)
```