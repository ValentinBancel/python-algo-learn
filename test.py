import pytest
import tasks.task as tasks

@pytest.mark.skipif(not hasattr(tasks, 'message'), reason="message function does not exist")
def test_task1():
    assert tasks.message() == "Hello World!"

@pytest.mark.skipif(not hasattr(tasks, 'product'), reason="message function does not exist")
def test_task2():
    assert tasks.product(2, 3) == 6
    assert tasks.product(5, 5) == 25

@pytest.mark.skipif(not hasattr(tasks, 'exchange'), reason="message function does not exist")
def test_task3():
    assert tasks.exchange(2, 3) == (3, 2)
    assert tasks.exchange(5, 5) == (5, 5)

@pytest.mark.skipif(not hasattr(tasks, 'parity'), reason="message function does not exist")
def test_task4():
    assert tasks.parity(2) == "Even"
    assert tasks.parity(3) == "Odd"

@pytest.mark.skipif(not hasattr(tasks, 'biggest'), reason="message function does not exist")
def test_task5(monkeypatch):
    inputs = [2, 3, 4]
    input_generator = (i for i in inputs)
    monkeypatch.setattr('builtins.input', lambda x: next(input_generator))
    assert tasks.biggest() == 4
    inputs = [3, 4, 2]
    input_generator = (i for i in inputs)
    monkeypatch.setattr('builtins.input', lambda x: next(input_generator))
    assert tasks.biggest() == 4
    inputs = [4, 2, 3]
    input_generator = (i for i in inputs)
    monkeypatch.setattr('builtins.input', lambda x: next(input_generator))
    assert tasks.biggest() == 4
    inputs = [5, 5, 5]
    input_generator = (i for i in inputs)
    monkeypatch.setattr('builtins.input', lambda x: next(input_generator))
    assert tasks.biggest() == 5

@pytest.mark.skipif(not hasattr(tasks, 'evaluatingGrade'), reason="message function does not exist")
def test_task6(monkeypatch):
    inputs = [10]
    input_generator = (i for i in inputs)
    monkeypatch.setattr('builtins.input', lambda x: next(input_generator))
    assert tasks.evaluatingGrade() == "passed"
    inputs = [9]
    input_generator = (i for i in inputs)
    monkeypatch.setattr('builtins.input', lambda x: next(input_generator))
    assert tasks.evaluatingGrade() == "failed"
    inputs = [20]
    input_generator = (i for i in inputs)
    monkeypatch.setattr('builtins.input', lambda x: next(input_generator))
    assert tasks.evaluatingGrade() == "passed"
    inputs = [55]
    input_generator = (i for i in inputs)
    monkeypatch.setattr('builtins.input', lambda x: next(input_generator))
    result = tasks.evaluatingGrade()
    assert result != "failed" and result != "passed"

@pytest.mark.skipif(not hasattr(tasks, 'positiveNegativeProduct'), reason="message function does not exist")
def test_task7(monkeypatch):
    inputs = [2,3]
    input_generator = (i for i in inputs)
    monkeypatch.setattr('builtins.input', lambda x: next(input_generator))
    assert tasks.positiveNegativeProduct() == "Positive"
    inputs = [-2,3]
    input_generator = (i for i in inputs)
    monkeypatch.setattr('builtins.input', lambda x: next(input_generator))
    assert tasks.positiveNegativeProduct() == "Negative"
    inputs = [2,-3]
    input_generator = (i for i in inputs)
    monkeypatch.setattr('builtins.input', lambda x: next(input_generator))
    assert tasks.positiveNegativeProduct() == "Negative"
    inputs = [-2,-3]
    input_generator = (i for i in inputs)
    monkeypatch.setattr('builtins.input', lambda x: next(input_generator))
    assert tasks.positiveNegativeProduct() == "Positive"
    inputs = [0,0]
    input_generator = (i for i in inputs)
    monkeypatch.setattr('builtins.input', lambda x: next(input_generator))
    assert tasks.positiveNegativeProduct() == "Positive"
    inputs = [0,3]
    input_generator = (i for i in inputs)
    monkeypatch.setattr('builtins.input', lambda x: next(input_generator))
    assert tasks.positiveNegativeProduct() == "Positive"
    inputs = [2,0]
    input_generator = (i for i in inputs)
    monkeypatch.setattr('builtins.input', lambda x: next(input_generator))
    assert tasks.positiveNegativeProduct() == "Positive"
    inputs = [0,-3]
    input_generator = (i for i in inputs)
    monkeypatch.setattr('builtins.input', lambda x: next(input_generator))
    assert tasks.positiveNegativeProduct() == "Positive"
    inputs = [-25000,10000]
    input_generator = (i for i in inputs)
    monkeypatch.setattr('builtins.input', lambda x: next(input_generator))
    assert tasks.positiveNegativeProduct() == "Negative"

@pytest.mark.skipif(not hasattr(tasks, 'absoluteValue'), reason="message function does not exist")
def test_task8(monkeypatch):
    inputs = [2]
    input_generator = (i for i in inputs)
    monkeypatch.setattr('builtins.input', lambda x: next(input_generator))
    assert tasks.absoluteValue() == 2
    inputs = [-2]
    input_generator = (i for i in inputs)
    monkeypatch.setattr('builtins.input', lambda x: next(input_generator))
    assert tasks.absoluteValue() == 2
    inputs = [0]
    input_generator = (i for i in inputs)
    monkeypatch.setattr('builtins.input', lambda x: next(input_generator))
    assert tasks.absoluteValue() == 0
    inputs = [-5]
    input_generator = (i for i in inputs)
    monkeypatch.setattr('builtins.input', lambda x: next(input_generator))
    assert tasks.absoluteValue() == 5
    inputs = [5]
    input_generator = (i for i in inputs)
    monkeypatch.setattr('builtins.input', lambda x: next(input_generator))
    assert tasks.absoluteValue() == 5

@pytest.mark.skipif(not hasattr(tasks, 'averageOfThreeIntegers'), reason="message function does not exist")
def test_averageOfThreeIntegers(monkeypatch):
    inputs = [2, 3, 4]
    input_generator = (i for i in inputs)
    monkeypatch.setattr('builtins.input', lambda x: next(input_generator))
    assert tasks.averageOfThreeIntegers() == 3
    inputs = [12, 7, 25]
    input_generator = (i for i in inputs)
    monkeypatch.setattr('builtins.input', lambda x: next(input_generator))
    assert tasks.averageOfThreeIntegers() == 14.666666666666666
    inputs = [2, 3, 4]
    input_generator = (i for i in inputs)
    monkeypatch.setattr('builtins.input', lambda x: next(input_generator))
    assert tasks.averageOfThreeIntegers() == 3
    inputs = [2, 3, 4]
    input_generator = (i for i in inputs)
    monkeypatch.setattr('builtins.input', lambda x: next(input_generator))
    assert tasks.averageOfThreeIntegers() == 3

@pytest.mark.skipif(not hasattr(tasks, 'calculateTotalPrice'), reason="message function does not exist")
def test_task10(monkeypatch):
    inputs = [300]
    input_generator = (i for i in inputs)
    monkeypatch.setattr('builtins.input', lambda x: next(input_generator))
    assert tasks.calculateTotalPrice() == 306.0
    inputs = [700]
    input_generator = (i for i in inputs)
    monkeypatch.setattr('builtins.input', lambda x: next(input_generator))
    assert tasks.calculateTotalPrice() == 714.0
    inputs = [900]
    input_generator = (i for i in inputs)
    monkeypatch.setattr('builtins.input', lambda x: next(input_generator))
    assert tasks.calculateTotalPrice() == 918.0
    inputs = [1000]
    input_generator = (i for i in inputs)
    monkeypatch.setattr('builtins.input', lambda x: next(input_generator))
    assert tasks.calculateTotalPrice() == 1020.0
    inputs = [2000]
    input_generator = (i for i in inputs)
    monkeypatch.setattr('builtins.input', lambda x: next(input_generator))
    assert tasks.calculateTotalPrice() == 2040.0
    inputs = [100]
    input_generator = (i for i in inputs)
    monkeypatch.setattr('builtins.input', lambda x: next(input_generator))
    assert tasks.calculateTotalPrice() == 120.0

@pytest.mark.skipif(not hasattr(tasks, 'copyingBill'), reason="message function does not exist")
def test_task11(monkeypatch):
    inputs = [0]
    input_generator = (i for i in inputs)
    monkeypatch.setattr('builtins.input', lambda x: next(input_generator))
    assert tasks.copyingBill() ==0
    inputs = [5]
    input_generator = (i for i in inputs)
    monkeypatch.setattr('builtins.input', lambda x: next(input_generator))
    assert tasks.copyingBill() == 1.25
    inputs = [15]
    input_generator = (i for i in inputs)
    monkeypatch.setattr('builtins.input', lambda x: next(input_generator))
    assert tasks.copyingBill() == 3.5
    inputs = [25]
    input_generator = (i for i in inputs)
    monkeypatch.setattr('builtins.input', lambda x: next(input_generator))
    assert tasks.copyingBill() == 5
    inputs = [150]
    input_generator = (i for i in inputs)
    monkeypatch.setattr('builtins.input', lambda x: next(input_generator))
    assert tasks.copyingBill() == 17.5

@pytest.mark.skipif(not hasattr(tasks, 'childAgeCategory'), reason="message function does not exist")
def test_task12():
    pass

@pytest.mark.skipif(not hasattr(tasks, 'monthInLetters'), reason="message function does not exist")
def test_task13():
    pass

@pytest.mark.skipif(not hasattr(tasks, 'displayGoodEvening'), reason="message function does not exist")
def test_task14():
    pass

@pytest.mark.skipif(not hasattr(tasks, 'sum1To10'), reason="message function does not exist")
def test_task15():
    pass
@pytest.mark.skipif(not hasattr(tasks, 'sum1ToN'), reason="message function does not exist")
def test_task16():
    pass
@pytest.mark.skipif(not hasattr(tasks, 'displayHelloTenTimes'), reason="message function does not exist")
def test_task17():
    pass
@pytest.mark.skipif(not hasattr(tasks, 'sum1To10UsingForLoop'), reason="message function does not exist")
def test_task18():
    pass
@pytest.mark.skipif(not hasattr(tasks, 'sum1ToNUsingForLoop'), reason="message function does not exist")
def test_task19():
    pass
@pytest.mark.skipif(not hasattr(tasks, 'multiplicationTableOf5'), reason="message function does not exist")
def test_task20():
    pass
@pytest.mark.skipif(not hasattr(tasks, 'multiplicationTableOfInteger'), reason="message function does not exist")
def test_task21():
    pass
@pytest.mark.skipif(not hasattr(tasks, 'displayHelloTenTimesUsingWhileLoop'), reason="message function does not exist")
def test_task22():
    pass
@pytest.mark.skipif(not hasattr(tasks, 'sum1To10UsingWhileLoop'), reason="message function does not exist")
def test_task23():
    pass
@pytest.mark.skipif(not hasattr(tasks, 'multiplicationTableOf8UsingWhileLoop'), reason="message function does not exist")
def test_task24():
    pass
@pytest.mark.skipif(not hasattr(tasks, 'enterAndDisplayArray'), reason="message function does not exist")
def test_task25():
    pass
@pytest.mark.skipif(not hasattr(tasks, 'calculateAverageOfNotes'), reason="message function does not exist")
def test_task26():
    pass
@pytest.mark.skipif(not hasattr(tasks, 'maximumOfArray'), reason="message function does not exist")
def test_task27():
    pass
@pytest.mark.skipif(not hasattr(tasks, 'occurrencesOfNElement'), reason="message function does not exist")
def test_task28():
    pass
@pytest.mark.skipif(not hasattr(tasks, 'sortArrayInAscendingOrder'), reason="message function does not exist")
def test_task29():
    pass
@pytest.mark.skipif(not hasattr(tasks, 'factorialOfInteger'), reason="message function does not exist")
def test_task30():
    pass