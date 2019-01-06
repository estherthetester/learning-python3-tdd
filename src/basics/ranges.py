#Use a for loop to sum every odd number from 10 to 20 inc and store the result to variable x

def test_should_sum_odd_numbers_for_given_odd_range():
    start = 1
    end = 3
    assert 4 == sum_odd_numbers(start, end)


def test_should_sum_odd_numbers_for_given_even_range():
    start = 2
    end = 4
    assert 3 == sum_odd_numbers(start, end)


def sum_odd_numbers(start, end):
    x = 0

    for num in range(start, end + 1):
        if num % 2 != 0:
            x += num
    return x
