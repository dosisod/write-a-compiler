from wac.parse.token import Token, TokenType, tokenize


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


def test_tokenize_single_token():
    tokens = tokenize("hello")

    assert len(tokens) == 1
    assert tokens[0] == Token("hello", 1, 1)


def test_tokenize_2_tokens():
    tokens = tokenize("hello\n")

    assert len(tokens) == 2
    assert tokens[0] == Token("hello", 1, 1)
    assert tokens[1] == Token("\n", 1, 6)
