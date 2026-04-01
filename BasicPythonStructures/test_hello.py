from hello import hello

def test_default():
    assert hello() == "hello, world"
    
# def test_argument(): 
#     assert hello("David") == "hello, David"

def test_argument():
    for name in ["Hemione", "Harry", "Ron"]:
        assert hello(name) == f"hello, {name}"