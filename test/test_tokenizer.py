from wac.parse.token import Token, TokenType, generate_location_info, tokenize


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
    locations = list(generate_location_info("a\nbc\ndef"))

    assert locations == [
        ("a", 1, 1),
        ("\n", 1, 2),
        ("b", 2, 1),
        ("c", 2, 2),
        ("\n", 2, 3),
        ("d", 3, 1),
        ("e", 3, 2),
        ("f", 3, 3),
    ]


def test_tokenize_single_token():
    tokens = tokenize("hello")

    assert tokens == [Token("hello", 1, 1)]


def test_tokenize_2_tokens():
    tokens = tokenize("hello\n")

    assert tokens == [Token("hello", 1, 1), Token("\n", 1, 6)]


def test_tokenize_many_tokens():
    tokens = tokenize("hello world")

    assert tokens == [
        Token("hello", 1, 1),
        Token(" ", 1, 6),
        Token("world", 1, 7),
    ]


def test_tokenize_unknown_token():
    tokens = tokenize("+")

    assert tokens == [Token("+", 1, 1)]
