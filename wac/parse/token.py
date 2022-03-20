from dataclasses import dataclass
from enum import Enum, auto
from typing import Generator, List, Optional, Tuple


class TokenType(Enum):
    IDENTIFIER = auto()
    WHITESPACE = auto()
    NEWLINE = auto()


@dataclass
class Token:
    content: str
    line: int
    column: int
    type: Optional[TokenType] = None


def generate_location_info(
    code: str,
) -> Generator[Tuple[str, int, int], None, None]:
    line = 1
    column = 1

    for c in code:
        yield (c, line, column)

        if c == "\n":
            line += 1
            column = 1

        else:
            column += 1


def tokenize(code: str) -> List[Token]:
    return [Token(code, 1, 1)]
