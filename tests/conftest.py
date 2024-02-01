


import pytest
from stuff.accum import Accumulator 


# Fixtures are special functions that pytest uses for setup and cleanup' 
# It's functions that pytest can call before test case functions. # 
# They're the best way to handle "Arrange" steps shared by multiple tests in the context of the Arrange-Act-Assert pattern.



@pytest.fixture
def accum(scope='function'): 
    yield Accumulator()
    print("DONE with the test!")

@pytest.fixture
def accum2(): 
    return Accumulator()

