
import pytest

#1 Passed Test
@pytest.mark.math
def test_one_plus_one():
    assert 1 + 1 == 2 


#2 Failed Test
@pytest.mark.math
def test_one_plus_two():
    a = 1
    b = 2
    c = 3 # change to zero to see a failing test 
    assert a + b == c


#3 Using pytest.raises (test function that verifies an exception. catch the exception and keep running the test as if there were no problems)
@pytest.mark.math
def test_divide_by_zero ():
    with pytest.raises(ZeroDivisionError) as e:
        num = 1 / 0 

    assert 'division by zero' in str(e.value)



#4 pytest.mark.parametrize (parametrized test function. Use it to run a test case with multiple inputs) 
# the tuples inside the list below are an example of equivalence classes of test case inputs (number of variables name and the length of each tuple must match)

products = [
    (2, 3, 6),        # positive integers   ( 2 = a , 3 = b , 6 = product)
    (1, 99, 99),      # indentity 
    (0, 99, 0),       # zero
    (3, -4, -12),     # positive by negative 
    (-5, -5, 25),     # negative by negative  
    (2.5, 6.7, 16.75) # float 
]

@pytest.mark.math
@pytest.mark.parametrize ('a, b, product', products) # First argument must match the parameter name for the tes case function. Second argument is the list of paramerized values 
def test_multiplication (a, b, product): 
    assert a * b == product 