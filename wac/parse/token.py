from dataclasses import dataclass
from enum import Enum, auto
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

    token_info: List[LocationInfo] = []
    tokens: List[Token] = []
    last_type: Optional[TokenType] = None

    for info in location_info:
        token_type = char_to_token_type(info.char)
        assert token_type

        if last_type and token_type != last_type:
            tokens.append(create_token(token_info))
            token_info = [info]

        else:
            token_info.append(info)

        last_type = token_type

    if len(token_info) > 0:
        tokens.append(create_token(token_info))

    return tokens
