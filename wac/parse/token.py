from dataclasses import dataclass
from enum import Enum, auto
from typing import List, Optional


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


def tokenize(code: str) -> List[Token]:
    return [Token(code, 1, 1)]
