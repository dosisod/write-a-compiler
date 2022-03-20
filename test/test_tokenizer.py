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

    assert len(locations) == 8
    assert locations[0] == ("a", 1, 1)
    assert locations[1] == ("\n", 1, 2)
    assert locations[2] == ("b", 2, 1)
    assert locations[3] == ("c", 2, 2)
    assert locations[4] == ("\n", 2, 3)
    assert locations[5] == ("d", 3, 1)
    assert locations[6] == ("e", 3, 2)
    assert locations[7] == ("f", 3, 3)


def test_tokenize_single_token():
    tokens = tokenize("hello")

    assert len(tokens) == 1
    assert tokens[0] == Token("hello", 1, 1)


"""
def test_tokenize_2_tokens():
    tokens = tokenize("hello\n")

    assert len(tokens) == 2
    assert tokens[0] == Token("hello", 1, 1)
    assert tokens[1] == Token("\n", 1, 6)
"""
