from numb3rs import validate

def test_true():
    assert validate("1.2.3.4") == True
    assert validate("127.0.0.1") == True
    assert validate("255.255.255.255") == True

def test_false():
    assert validate("275.6.8.12") == False
    assert validate("1.1.1.1000") == False
    assert validate("001.23.24.25") == False
    assert validate("cat") == False