from twttr import shorten

def main():
    test_shorten()

def test_shorten():
    assert shorten("hello") == "hll"
    assert shorten("HELLO") == "HLL"
    assert shorten("hello10") == "hll10"
    assert shorten("mismis,") == "msms,"

if __name__ == "__main__":
    main()