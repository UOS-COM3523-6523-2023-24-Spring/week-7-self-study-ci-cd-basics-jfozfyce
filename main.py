def simple_count(s):
    return len(s)  # FIXME: should return the length of the string


def random_function():
    import random
    if random.random() < 0.001:
        return True
    else:
        return False


def complex_function():
    if random_function():
        return 'behaviour 1'
    else:
        return 'behaviour 2'

def oracle_simple_count(test_case):
    expected = len(test_case)
    actual = simple_count(test_case)
    return expected == actual

test_set_simple_count = [
    "",          # empty string
    "test",      # common string
    "123456789", # number string
    "specal!@#",  # special string
]

# test simple_count
for test_case in test_set_simple_count:
    assert oracle_simple_count(test_case), f"Test failed for input: {test_case}"
print("All tests passed for simple_count.")

# test random_function 和 complex_function return type
assert isinstance(random_function(), bool), "random_function should return a boolean."
possible_behaviours = ['behaviour 1', 'behaviour 2']
assert complex_function() in possible_behaviours, "complex_function returned an unexpected value."
print("Basic checks passed for random_function and complex_function.")