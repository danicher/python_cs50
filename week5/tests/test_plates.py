from plates import is_valid

def test_true():
    assert is_valid("CS50") == True
    assert is_valid("MISTY") == True
    assert is_valid("hello") == True

def test_false():
    assert is_valid("h") == False
    assert is_valid("goodbye") == False
    assert is_valid("50") == False
    assert is_valid("cs5y0") == False
    assert is_valid("cs05") == False
    assert is_valid("hello!") == False