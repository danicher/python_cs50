from bank import value

def test_hello():
    assert value("hello") == 0
    assert value("Hello") == 0
    assert value("HELLO") == 0
    assert value("hello, world") == 0

def test_h_only():
    assert value("hi") == 20
    assert value("hey") == 20
    assert value("hmmm") == 20
    assert value("Hooray!") == 20

def test_other():
    assert value("What's up") == 100
    assert value("good morning") == 100
    assert value("yo") == 100
    assert value("greetings") == 100