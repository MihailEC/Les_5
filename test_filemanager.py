from apps import refill, buy

def test_refill():
    cash_first = 100
    cash_up = 100
    cash_second = refill(cash_first, cash_up)
    assert cash_second == cash_first + cash_up

