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
        raise ValueError("List and target must only be integers")


def recursive_binary_search_helper(lyst, low_index, high_index, target):
    if low_index >= high_index:
        return False

    mid_idx = (low_index + high_index) // 2
    mid_val = lyst[mid_idx]

    if mid_val == target:
        return True

    if mid_val > target:
        return recursive_binary_search_helper(lyst, low_index, mid_idx, target)

    if mid_val < target:
        return recursive_binary_search_helper(lyst, mid_idx + 1, high_index, target)


def recursive_binary_search(lyst, target):
    """A function that performs the recursive binary search. """
    if all(isinstance(x, int) for x in lyst) and type(target) == int:
        high_index = len(lyst) - 1
        low_index = 0
        if recursive_binary_search_helper(lyst, low_index, high_index, target):
            return True
        else:
            return False
    else:
        raise ValueError("List and target must only be integers")


def jump_search(lyst, target):
    """A function that performs the jump search. """
    print("Jump search")


# if linear_search([1, 2, 3, 4, 5, 6, 7, 9], 5):
#     print("Yes")

print(recursive_binary_search([1, 2, 3, 4, 5, 6, 7, 9], 10))

