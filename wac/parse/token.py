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


def char_to_token_type(c: str) -> Optional[TokenType]:
    if c == "\n":
        return TokenType.NEWLINE

    if c.isspace():
        return TokenType.WHITESPACE

    if c.isalpha():
        return TokenType.IDENTIFIER

    return None


def tokenize(code: str) -> List[Token]:
    locations = generate_location_info(code)

    token_parts = [next(locations)]

    for location in locations:
        token_parts.append(location)

    def collapse_token(parts):
        out = parts.pop(0)

        for part in parts:
            out = (out[0] + part[0], out[1], out[2])

        return Token(out[0], out[1], out[2])

    return [collapse_token(token_parts)]
