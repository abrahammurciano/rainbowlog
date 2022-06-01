# Rainbow Log

Format your python logs with colours based on the log levels.

## Installation

	pip install rainbowlog

## Usage

Here's a basic example of a script that logs colorfully to the console, but regularly to a file.

```python
import logging
import rainbowlog

logger = logging.getLogger(__name__)

# This one will write to the console
stream_handler = logging.StreamHandler()

# This one will write to a file
file_handler = logging.FileHandler('output.log')

# Here we decide how we want the logs to look like
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# We want the stream handler to be colorful
stream_handler.setFormatter(rainbowlog.Formatter(formatter))

# We don't want the file handler to be colorful
file_handler.setFormatter(formatter)

# Finally we add the handlers to the logger
logger.addHandler(stream_handler)
logger.addHandler(file_handler)

if __name__ == '__main__':
	logger.debug('This is a debug message')
	logger.info('This is an info message')
	logger.warning('This is a warning message')
	logger.error('This is an error message')
	logger.critical('This is a critical message')
```

## Docs

You can find the documentation [here](https://abrahammurciano.github.io/rainbowlog/)
