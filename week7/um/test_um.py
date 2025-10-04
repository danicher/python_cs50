from um import count

def test_no_um():
    assert count("Hello, world!") == 0
    assert count("hi, mum") == 0

def test_one_um():
    assert count("Um, I think so.") == 1

def test_multiple_ums():
    assert count("Um, this is um, quite interesting. Um!") == 3