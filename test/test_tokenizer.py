from wac.parse.token import (
    Token,
    TokenType,
    generate_token_locations,
    tokenize,
)


def test_create_token():
    token = Token("hello", 1, 2)

    assert token.content == "hello"
    assert token.line == 1
    assert token.column == 2
    assert not token.type


def test_create_token_with_type():
    token = Token("hello", 1, 2, TokenType.IDENTIFIER)

    assert token.content == "hello"
    assert token.line == 1
    assert token.column == 2
    assert token.type == TokenType.IDENTIFIER


def test_token_compare():
    assert Token("hello", 1, 1) == Token("hello", 1, 1)


def test_generate_location_info():
    locations = list(generate_token_locations("a\nbc\ndef"))

    assert locations == [
        Token("a", 1, 1),
        Token("\n", 1, 2),
        Token("b", 2, 1),
        Token("c", 2, 2),
        Token("\n", 2, 3),
        Token("d", 3, 1),
        Token("e", 3, 2),
        Token("f", 3, 3),
    ]


def test_tokenize_single_token():
    tokens = tokenize("hello")

    assert tokens == [Token("hello", 1, 1, TokenType.IDENTIFIER)]


def test_tokenize_2_tokens():
    tokens = tokenize("hello\n")

    assert tokens == [
        Token("hello", 1, 1, TokenType.IDENTIFIER),
        Token("\n", 1, 6, TokenType.NEWLINE),
    ]


def test_tokenize_many_tokens():
    tokens = tokenize("hello world")

    assert tokens == [
        Token("hello", 1, 1, TokenType.IDENTIFIER),
        Token(" ", 1, 6, TokenType.WHITESPACE),
        Token("world", 1, 7, TokenType.IDENTIFIER),
    ]


def test_tokenize_unknown_token():
    tokens = tokenize("!")

    assert tokens == [Token("!", 1, 1, None)]


def test_collapse_comment():
    tokens = tokenize("# hello world")

    assert tokens == [Token("# hello world", 1, 1, TokenType.COMMENT)]


def test_collapse_comment_respect_newlines():
    tokens = tokenize("# hello\n# world")

    assert tokens == [
        Token("# hello", 1, 1, TokenType.COMMENT),
        Token("\n", 1, 8, TokenType.NEWLINE),
        Token("# world", 2, 1, TokenType.COMMENT),
    ]
