from enum import Enum
from typing import Any, Iterable, Iterator, KeysView, Mapping, Optional, Union


class Color(Enum):
    BLACK = "black"
    RED = "red"
    GREEN = "green"
    YELLOW = "yellow"
    BLUE = "blue"
    MAGENTA = "magenta"
    CYAN = "cyan"
    WHITE = "white"

    def __str__(self):
        return self.value


class Style(Enum):
    NONE = "none"
    BOLD = "bold"
    FAINT = "faint"
    ITALIC = "italic"
    UNDERLINE = "underline"
    BLINK = "blink"
    BLINK2 = "blink2"
    NEGATIVE = "negative"
    CONCEALED = "concealed"
    CROSSED = "crossed"

    def __str__(self):
        return self.value


class Format(Mapping[str, Any]):
    """
    This class represents a format for a log message. It can be used to specify the foreground and background colors and other ANSI styles.

    Args:
        foreground: The foreground color.
        background: The background color.
        style: The style. This can be a single style or several styles.
    """

    def __init__(
        self,
        foreground: Color = None,
        background: Color = None,
        style: Union[Style, Iterable[Style]] = (),
    ):
        self._dict = {
            "fg": str(foreground) if foreground else None,
            "bg": str(background) if background else None,
            "style": str(style)
            if isinstance(style, Style)
            else "+".join(str(s) for s in style),
        }

    def keys(self) -> KeysView[str]:
        return self._dict.keys()

    def __getitem__(self, key: str) -> Optional[str]:
        return self._dict[key]

    def __iter__(self) -> Iterator[str]:
        return iter(self._dict)

    def __len__(self) -> int:
        return len(self._dict)
