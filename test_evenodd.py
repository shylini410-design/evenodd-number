from evenodd import evenodd

def test_even():
    assert evenodd(10) == "Even number"

def test_odd():
    assert evenodd(15) == "odd number"