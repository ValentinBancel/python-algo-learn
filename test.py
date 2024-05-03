import pytest
from tasks.task import *

def test_task1():
    assert message() == "Hello World!"

def test_task2():
    assert product(2, 3) == 6
    assert product(5, 5) == 25

def test_task3():
    assert exchange(2, 3) == (3, 2)
    assert exchange(5, 5) == (5, 5)

def test_task4():
    assert parity(2) == "Even"
    assert parity(3) == "Odd"

def test_task5():
    assert biggest(2, 3, 4) == 4
    assert biggest(3, 4, 2) == 4
    assert biggest(4, 2, 3) == 4
    assert biggest(5, 5, 5) == 5

def test_task6():
    evaluatingGrade(10) == "passed"
    evaluatingGrade(9) == "failed"
    evaluatingGrade(20) == "passed"
    evaluatingGrade(55) != "failed" and evaluatingGrade(55) != "passed"

def test_task7():
    positiveNegativeProduct(2, 3) == "Positive"
    positiveNegativeProduct(-2, 3) == "Negative"
    positiveNegativeProduct(2, -3) == "Negative"
    positiveNegativeProduct(-2, -3) == "Positive"
    positiveNegativeProduct(0, 0) == "Positive"
    positiveNegativeProduct(0, 3) == "Positive"
    positiveNegativeProduct(2, 0) == "Positive"
    positiveNegativeProduct(0, -3) == "Positive"
    positiveNegativeProduct(-2, 0) == "Positive"
    positiveNegativeProduct(0, 0) == "Positive"
    positiveNegativeProduct(0, 3) == "Positive"
    positiveNegativeProduct(2, 0) == "Positive"
    positiveNegativeProduct(0, -3) == "Positive"
    positiveNegativeProduct(-25000, 1000) == "Negative"

def test_task8():
    assert absoluteValue(2) == 2
    assert absoluteValue(-2) == 2
    assert absoluteValue(0) == 0
    assert absoluteValue(-5) == 5
    assert absoluteValue(5) == 5

def test_averageOfThreeIntegers(monkeypatch):
    inputs = [2, 3, 4]
    input_generator = (i for i in inputs)
    monkeypatch.setattr('builtins.input', lambda x: next(input_generator))
    assert averageOfThreeIntegers() == 3
    inputs = [12, 7, 25]
    input_generator = (i for i in inputs)
    monkeypatch.setattr('builtins.input', lambda x: next(input_generator))
    assert averageOfThreeIntegers() == 14.666666666666666
    inputs = [2, 3, 4]
    input_generator = (i for i in inputs)
    monkeypatch.setattr('builtins.input', lambda x: next(input_generator))
    assert averageOfThreeIntegers() == 3
    inputs = [2, 3, 4]
    input_generator = (i for i in inputs)
    monkeypatch.setattr('builtins.input', lambda x: next(input_generator))
    assert averageOfThreeIntegers() == 3

def test_task10(monkeypatch):
    inputs = [300]
    input_generator = (i for i in inputs)
    monkeypatch.setattr('builtins.input', lambda x: next(input_generator))
    assert calculateTotalPrice() == 306.0
    inputs = [700]
    input_generator = (i for i in inputs)
    monkeypatch.setattr('builtins.input', lambda x: next(input_generator))
    assert calculateTotalPrice() == 714.0
    inputs = [900]
    input_generator = (i for i in inputs)
    monkeypatch.setattr('builtins.input', lambda x: next(input_generator))
    assert calculateTotalPrice() == 918.0
    inputs = [1000]
    input_generator = (i for i in inputs)
    monkeypatch.setattr('builtins.input', lambda x: next(input_generator))
    assert calculateTotalPrice() == 1020.0
    inputs = [2000]
    input_generator = (i for i in inputs)
    monkeypatch.setattr('builtins.input', lambda x: next(input_generator))
    assert calculateTotalPrice() == 2040.0
    inputs = [100]
    input_generator = (i for i in inputs)
    monkeypatch.setattr('builtins.input', lambda x: next(input_generator))
    assert calculateTotalPrice() == 120.0


# def test_task11():
#     pass

# def test_task12():
#     pass

# def test_task13():
#     pass

# def test_task14():
#     pass

# def test_task15():
#     pass
# def test_task16():
#     pass
# def test_task17():
#     pass
# def test_task18():
#     pass
# def test_task19():
#     pass
# def test_task20():
#     pass
# def test_task21():
#     pass
# def test_task22():
#     pass
# def test_task23():
#     pass
# def test_task24():
#     pass
# def test_task25():
#     pass
# def test_task26():
#     pass
# def test_task27():
#     pass
# def test_task28():
#     pass
# def test_task29():
#     pass
# def test_task20():
#     pass