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
    inputs = [2, 3, 4,3, 4, 2,4, 2, 3,5, 5, 5]
    input_generator = (i for i in inputs)
    monkeypatch.setattr('builtins.input', lambda x: next(input_generator))
    assert tasks.biggest() == 4
    assert tasks.biggest() == 4
    assert tasks.biggest() == 4
    assert tasks.biggest() == 5

@pytest.mark.skipif(not hasattr(tasks, 'evaluatingGrade'), reason="message function does not exist")
def test_task6(monkeypatch):
    inputs = [10,9,20,55]
    input_generator = (i for i in inputs)
    monkeypatch.setattr('builtins.input', lambda x: next(input_generator))
    assert tasks.evaluatingGrade() == "passed"
    assert tasks.evaluatingGrade() == "failed"
    assert tasks.evaluatingGrade() == "passed"
    result = tasks.evaluatingGrade()
    assert result != "failed" and result != "passed"

@pytest.mark.skipif(not hasattr(tasks, 'positiveNegativeProduct'), reason="message function does not exist")
def test_task7(monkeypatch):
    inputs = [2,3, -2,3, 2,-3, -2,-3, 0,0, 0,3, 2,0, 0,-3 ,-25000,10000]
    input_generator = (i for i in inputs)
    monkeypatch.setattr('builtins.input', lambda x: next(input_generator))
    assert tasks.positiveNegativeProduct() == "positive"
    assert tasks.positiveNegativeProduct() == "negative"
    assert tasks.positiveNegativeProduct() == "negative"
    assert tasks.positiveNegativeProduct() == "positive"
    assert tasks.positiveNegativeProduct() == "zero"
    assert tasks.positiveNegativeProduct() == "zero"
    assert tasks.positiveNegativeProduct() == "zero"
    assert tasks.positiveNegativeProduct() == "zero"
    assert tasks.positiveNegativeProduct() == "negative"

@pytest.mark.skipif(not hasattr(tasks, 'absoluteValue'), reason="message function does not exist")
def test_task8(monkeypatch):
    inputs = [2,-2,0,-5,5]
    input_generator = (i for i in inputs)
    monkeypatch.setattr('builtins.input', lambda x: next(input_generator))
    assert tasks.absoluteValue() == 2
    assert tasks.absoluteValue() == 2
    assert tasks.absoluteValue() == 0
    assert tasks.absoluteValue() == 5
    assert tasks.absoluteValue() == 5

@pytest.mark.skipif(not hasattr(tasks, 'averageOfThreeIntegers'), reason="message function does not exist")
def test_averageOfThreeIntegers(monkeypatch):
    inputs = [2, 3, 4,12, 7, 25]
    input_generator = (i for i in inputs)
    monkeypatch.setattr('builtins.input', lambda x: next(input_generator))
    assert tasks.averageOfThreeIntegers() == 3
    assert tasks.averageOfThreeIntegers() == 14.666666666666666

@pytest.mark.skipif(not hasattr(tasks, 'calculateTotalPrice'), reason="message function does not exist")
def test_task10(monkeypatch):
    inputs = [300,700,900,1000,2000,100]
    input_generator = (i for i in inputs)
    monkeypatch.setattr('builtins.input', lambda x: next(input_generator))
    assert tasks.calculateTotalPrice() == 306.0
    assert tasks.calculateTotalPrice() == 714.0
    assert tasks.calculateTotalPrice() == 918.0
    assert tasks.calculateTotalPrice() == 1020.0
    assert tasks.calculateTotalPrice() == 2040.0
    assert tasks.calculateTotalPrice() == 120.0

@pytest.mark.skipif(not hasattr(tasks, 'copyingBill'), reason="message function does not exist")
def test_task11(monkeypatch):
    inputs = [0,5,15,25,150]
    input_generator = (i for i in inputs)
    monkeypatch.setattr('builtins.input', lambda x: next(input_generator))
    assert tasks.copyingBill() == 0
    assert tasks.copyingBill() == 1.25
    assert tasks.copyingBill() == 3.5
    assert tasks.copyingBill() == 5
    assert tasks.copyingBill() == 17.5


@pytest.mark.skipif(not hasattr(tasks, 'childAgeCategory'), reason="message function does not exist")
def test_task12(monkeypatch):
    inputs = [1,2,3,6,7,8,9,10,11,12,16,17]
    input_generator = (i for i in inputs)
    monkeypatch.setattr('builtins.input', lambda x: next(input_generator))
    result = tasks.childAgeCategory() 
    assert result != "poussin" and result != "pupille" and result != "minime" and result != "cadet"
    result = tasks.childAgeCategory() 
    assert result != "poussin" and result != "pupille" and result != "minime" and result != "cadet"
    result = tasks.childAgeCategory() 
    assert result != "poussin" and result != "pupille" and result != "minime" and result != "cadet"
    assert tasks.childAgeCategory() == "poussin"
    assert tasks.childAgeCategory() == "poussin"
    assert tasks.childAgeCategory() == "pupille"
    assert tasks.childAgeCategory() == "pupille"
    assert tasks.childAgeCategory() == "minime"
    assert tasks.childAgeCategory() == "minime"
    assert tasks.childAgeCategory() == "cadet"


@pytest.mark.skipif(not hasattr(tasks, 'monthInLetters'), reason="message function does not exist")
def test_task13(monkeypatch):
    inputs = [1,2,3,4,5,6,7,8,9,10,11,12,15]
    input_generator = (i for i in inputs)
    monkeypatch.setattr("builtins.input", lambda x: next(input_generator))
    month = ["january","february","march","april","may","june","july","august","september","october","november","december"]
    assert tasks.monthInLetters() == month[0]
    assert tasks.monthInLetters() == month[1]
    assert tasks.monthInLetters() == month[2]
    assert tasks.monthInLetters() == month[3]
    assert tasks.monthInLetters() == month[4]
    assert tasks.monthInLetters() == month[5]
    assert tasks.monthInLetters() == month[6]
    assert tasks.monthInLetters() == month[7]
    assert tasks.monthInLetters() == month[8]
    assert tasks.monthInLetters() == month[9]
    assert tasks.monthInLetters() == month[10]
    assert tasks.monthInLetters() == month[11]
    result = tasks.monthInLetters() 
    assert result not in month

@pytest.mark.skipif(not hasattr(tasks, 'displayGoodEvening'), reason="message function does not exist")
def test_task14():
    assert tasks.displayGoodEvening() == "Good eveningGood eveningGood eveningGood eveningGood eveningGood eveningGood eveningGood eveningGood eveningGood evening"

@pytest.mark.skipif(not hasattr(tasks, 'sum1To10'), reason="message function does not exist")
def test_task15():
    assert tasks.sum1To10() == 55
@pytest.mark.skipif(not hasattr(tasks, 'sum1ToN'), reason="message function does not exist")
def test_task16(monkeypatch):
    inputs = [10,75,90,192,647,824,675,9284,12345678]
    input_generator = (i for i in inputs)
    monkeypatch.setattr("builtins.input", lambda x: next(input_generator))
    assert tasks.sum1To10() == 55
    assert tasks.sum1To10() == 55
    assert tasks.sum1To10() == 55
    assert tasks.sum1To10() == 55
    assert tasks.sum1To10() == 55
    assert tasks.sum1To10() == 55
    assert tasks.sum1To10() == 55
    assert tasks.sum1To10() == 55
    assert tasks.sum1To10() == 55

@pytest.mark.skipif(not hasattr(tasks, 'displayHelloTenTimes'), reason="message function does not exist")
def test_task17():
    assert tasks.displayHelloTenTimes() == "HelloHelloHelloHelloHelloHelloHelloHelloHelloHello"
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