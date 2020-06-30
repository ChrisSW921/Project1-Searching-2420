"""Search project"""

import recursioncounter
# import test_search


def linear_search(lyst, target):
    """A function that performs the linear search."""
    if all(isinstance(x, int) for x in lyst) and type(target) == int:
        if target in lyst:
            return True
        else:
            return False
    else:
        raise ValueError



def recursive_binary_search(lyst, target):
    """A function that performs the recursive binary search. """
    print("Recursive binary search")


def jump_search(lyst, target):
    """A function that performs the jump search. """
    print("Jump search")


linear_search([1, 2, 3, 4, 5, 6, 7, 9], 5)


