# Rainbow Log

Format your python logs with colours based on the log levels.

## Installation

	pip install rainbowlog

## Docs

You can find the documentation [here](https://abrahammurciano.github.io/rainbowlog/rainbowlog)

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

If you want to change the format of the logs for each log level, you can construct the `rainbowlog.Formatter` object like this:

```py
import logging
from rainbowlog import Formatter, Format, Color, Style

formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
color_formatter = Formatter(
	formatter,
	color_configs={
		logging.DEBUG: Format(Color.BLUE, style=Style.FAINT),
		logging.INFO: Format(Color.GREEN),
		logging.WARNING: Format(Color.YELLOW, style=Style.ITALIC),
		logging.ERROR: Format(Color.RED, Color.WHITE, Style.BOLD),
		logging.CRITICAL: Format(Color.RED, Color.YELLOW, (Style.BOLD, Style.UNDERLINE)),
	}
	exception_config=Format(Color.RED, Color.WHITE, Style.BOLD),
	stack_config=Format(Color.RED, Color.WHITE, Style.BOLD),
)
```

> NOTE: You can pass instead of a Format object, a dict of keyword arguments which ansicolors library's `color` function accepts. See the [ansicolors documentation](https://pypi.org/project/ansicolors/). This will usually not be necessary.