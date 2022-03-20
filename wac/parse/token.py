from dataclasses import dataclass
from enum import Enum, auto
from itertools import groupby
from typing import Generator, List, NamedTuple, Optional


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


class LocationInfo(NamedTuple):
    char: str
    line: int
    column: int


def generate_location_info(
    code: str,
) -> Generator[LocationInfo, None, None]:
    line = 1
    column = 1

    for c in code:
        yield LocationInfo(c, line, column)

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
    def create_token(token_info):
        contents = "".join([info.char for info in token_info])

        return Token(contents, token_info[0].line, token_info[0].column)

    location_info = generate_location_info(code)

    grouped = groupby(
        location_info,
        lambda info: char_to_token_type(info.char),
    )

    return [create_token(list(group[1])) for group in grouped]
