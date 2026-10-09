import pytest
from Exceptions import ExceptionsDemo, MyException  

def test_division_zero():
    demo = ExceptionsDemo()
    with pytest.raises(ZeroDivisionError):
        demo.divide(10, 0)

def test_division_with_str():
    demo = ExceptionsDemo()
    with pytest.raises(TypeError):
        demo.divide("10", 0)


def test_access_list():
    demo = ExceptionsDemo()
    with pytest.raises(IndexError):
        demo.access_list([1,2,3,4], 5)

def test_access_dict():
    demo = ExceptionsDemo()
    with pytest.raises(KeyError):
        demo.access_dict({"color": "rojo", "forma": "round"}, "sabor")


def test_read_file():
    demo = ExceptionsDemo()
    with pytest.raises(FileNotFoundError):
        demo.read_file("non_existent_file.txt")


def test_access_attribute():
    demo = ExceptionsDemo()
    with pytest.raises(AttributeError):
        demo.access_attribute(object())

def test_check_positive():
    demo = ExceptionsDemo()
    with pytest.raises(MyException):
        demo.check_positive(-5)