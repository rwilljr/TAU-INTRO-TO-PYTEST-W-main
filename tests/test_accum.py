

import pytest
from stuff.accum import Accumulator 

# This pattern is called "Arrange-Act-Assert". It is the classic three-step pattern for functional test cases.

# Arrange assets for the test (like a setup procedure).
# Act by exercising the target behavior.
# Assert that expected outcomes happen.


# test_accumulator_init() verifies that the new instance of the Accumulator class has a starting count of zero.
@pytest.mark.accumulator
def test_accumulator_init(accum, accum2): 
    assert accum.count == 0 


# test_accumulator_add_one() verifies that the add() method adds one to the internal count when it is called with no other arguments.
@pytest.mark.accumulator
def test_accumulator_add_one(accum): 
    accum.add()
    assert accum.count == 1 

# test_accumulator_add_three() verifies that the add() method adds 3 to the count when it is called with the argument of 3.
@pytest.mark.accumulator
def test_accumulator_add_three(accum): 
    accum.add(3)
    assert accum.count == 3 

# test_accumulator_add_twice() verifies that the count increases appropriately with multiple add() calls.
@pytest.mark.accumulator
def test_accumulator_add_twice(accum): 
    accum.add()
    accum.add()
    assert accum.count == 2

# test_accumulator_cannot_set_count_directly() verifies that the count attribute cannot be assigned directly because it is a read-only property
@pytest.mark.accumulator
def test_accumulator_cannot_set_count_directly(accum):
    with pytest.raises(AttributeError, match=r"property 'count' of 'Accumulator' object has no setter") as e:
        accum.count = 10