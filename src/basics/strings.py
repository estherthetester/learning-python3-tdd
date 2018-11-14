def test_new_line():
    message = "Something\nelse"
    assert '\n' in message

def test_escape_sequence():
    mountains = "/\\/\\/\\"
    assert mountains == "/\\/\\/\\"


def test_escaped_quotation():
    quotation = '"'
    assert '"' in quotation


def test_concatenation():
    greeting = "Hello"
    name = "Esther"
    assert greet(greeting, name) == "Hello Esther"


def formatted(first, last):
    return f"First Name: {first}, Last Name: {last}"


def formatted_format(first, last):
    return "First Name: {}, Last Name: {}".format(first, last)


def test_formatting_strings():
    first = "Esther"
    last = "Lloyd"
    formatted_string = "First Name: Esther, Last Name: Lloyd"
    assert formatted(first, last) == formatted_string
    assert formatted_format(first, last) == formatted_string


def greet(greeting, name):
    return greeting + " " + name


