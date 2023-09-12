import math


# тестирование функций filter, map, sorted
# тест функции filter
def test_filter():
    def filter_odd_num(in_num):
        if (in_num % 2) == 0:
            return True
        else:
            return False

    numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    assert list(filter(filter_odd_num, numbers)) == [0, 2, 4, 6, 8, 10]


# тест функции map
def test_map():
    numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    numbers_copy = numbers.copy()

    for i in range(len(numbers_copy)):
        numbers_copy[i] = str(numbers_copy[i])
    assert numbers_copy == list(map(str, numbers))


# тест функции sorted
def test_sorted():
    numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    numbers_revers = numbers.copy()
    numbers_revers.reverse()
    assert sorted(numbers, key=None, reverse=True) == numbers_revers


def test_math_pi():
    assert math.pi == 3.141592653589793


def test_math_sqrt():
    x = 100
    assert math.sqrt(x) == x ** 0.5


def test_math_pow():
    x = 5
    y = 6
    assert math.pow(x, y) == x ** y


def test_math_hypot():
    x = 10
    y = 6
    assert math.hypot(x, y) == math.sqrt((x * x + y * y))


def test_math_fabs():
    x = 10
    if x > 0:
        assert math.fabs(x) == x * 1
    else:
        assert math.fabs(x) == x * -1


def test_math_factorial():
    x = 100
    data = [i for i in range(1, x + 1)]
    result = 1
    for el in data:
        result = result * el
    assert math.factorial(x) == result