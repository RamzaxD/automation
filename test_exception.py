import pytest

def func1():
    raise ValueError ("Una excepción de la función 1")

def test_cant():
    with pytest.raises(Exception) as excinfo:
        #assert (1,2,3) == (1,2,4)
        func1()
    print (str(excinfo))
    assert (str(excinfo.value)) == "Una excepción de la función 1aaa"

def test_excepcion():
    with pytest.raises(ZeroDivisionError):
        assert (1/0)
