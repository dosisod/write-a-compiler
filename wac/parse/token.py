from dataclasses import dataclass
from enum import Enum, auto
from itertools import groupby
from typing import Generator, List, Optional


class TokenType(Enum):
    IDENTIFIER = auto()
    WHITESPACE = auto()
    NEWLINE = auto()
    PLUS = auto()
    DASH = auto()
    ASTERISK = auto()
    SLASH = auto()
    POWER = auto()
    OPEN_PAREN = auto()
    CLOSE_PAREN = auto()
    EQUAL = auto()
    LESS_THEN = auto()
    GREATER_THEN = auto()
    DOT = auto()
    COMMENT = auto()


@dataclass
class Token:
    content: str
    line: int
    column: int
    type: Optional[TokenType] = None


def generate_token_locations(
    code: str,
) -> Generator[Token, None, None]:
    line = 1
    column = 1

    for c in code:
        yield Token(c, line, column)

        if c == "\n":
            line += 1
            column = 1

        else:
            column += 1


def char_to_token_type(c: str) -> Optional[TokenType]:
    simple_token_types = {
        "\n": TokenType.NEWLINE,
        "+": TokenType.PLUS,
        "-": TokenType.DASH,
        "*": TokenType.ASTERISK,
        "/": TokenType.SLASH,
        "^": TokenType.POWER,
        "(": TokenType.OPEN_PAREN,
        ")": TokenType.CLOSE_PAREN,
        "=": TokenType.EQUAL,
        "<": TokenType.LESS_THEN,
        ">": TokenType.GREATER_THEN,
        ".": TokenType.DOT,
        "#": TokenType.COMMENT,
    }

    if token_type := simple_token_types.get(c):
        return token_type

    if c.isspace():
        return TokenType.WHITESPACE

    if c.isalpha():
        return TokenType.IDENTIFIER

    return None


def collapse_comment(tokens: List[Token]) -> List[Token]:
    out: List[Token] = []
    in_comment = False

    for token in tokens:
        if token.type == TokenType.COMMENT:
            in_comment = True

        elif in_comment:
            if token.type == TokenType.NEWLINE:
                in_comment = False

            else:
                out[-1].content += token.content
                continue

        out.append(token)

    return out


def tokenize(code: str) -> List[Token]:
    def collapse_token(tokens):
        contents = "".join([token.content for token in tokens])

        first = tokens[0]
        return Token(contents, first.line, first.column, first.type)

    def add_token_type(token: Token) -> Token:
        token.type = char_to_token_type(token.content)

        return token

    tokens = [
        add_token_type(token) for token in generate_token_locations(code)
    ]

    tokens = collapse_comment(tokens)

    grouped = groupby(tokens, lambda token: token.type)

    return [collapse_token(list(group[1])) for group in grouped]
