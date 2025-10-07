from jar import Jar
import pytest   

def test_init():
    jar = Jar()
    assert jar.capacity == 12
    assert jar.size == 0

def test_init_invalid_capacity():
    with pytest.raises(ValueError):
        Jar(-5)

def test_str():
    jar = Jar()
    jar.deposit(5)
    assert str(jar) == "🍪🍪🍪🍪🍪"

def test_deposit():
    jar = Jar()
    jar.deposit(5)
    assert jar.size == 5
    with pytest.raises(ValueError):
        jar.deposit(8)  

def test_withdraw():
    jar = Jar()
    jar.deposit(5)
    jar.withdraw(3)
    assert jar.size == 2
    with pytest.raises(ValueError):
        jar.withdraw(5)

def test_capacity_property():
    jar = Jar(20)
    assert jar.capacity == 20

def test_size_property():
    jar = Jar()
    jar.deposit(7)
    assert jar.size == 7