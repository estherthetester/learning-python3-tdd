def test_split():
    assert split(10) == 2


def test_string():
    city = "String"
    assert type(city) == str


def test_float():
    price = 3.45
    assert type(price) == float


def test_int():
    high_score = 1
    assert type(high_score) == int


def test_boolean():
    is_having_fun = True
    assert type(is_having_fun) == bool


def split(cash):
    bounty = cash / 5
    print(bounty)
    return bounty
