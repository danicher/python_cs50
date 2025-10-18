from spellingBee import generate_letters, display_letters, is_valid 

def test_generate_letters():
    letters, main = generate_letters()
    assert len(letters) == 9
    assert main in letters

def test_display_letters():
    letters, main = generate_letters()
    try:
        display_letters(letters, main)
    except Exception as e:
        assert False, f"display_letters raised an exception: {e}"

def test_is_valid():
    assert is_valid("") == False
    assert is_valid("ABCDEFGHIJ") == False
    assert is_valid("XYZ") == False