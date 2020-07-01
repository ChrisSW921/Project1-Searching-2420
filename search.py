"""Search project"""
import random
import math
import time
from recursioncounter import RecursionCounter


def linear_search(lyst, target):
    """A function that performs the linear search."""
    if all(isinstance(x, int) for x in lyst) and isinstance(target, int):
        for item in lyst:
            if item == target:
                return True
        return False
    raise ValueError("List and target must only be integers")


def recursive_binary_search_helper(lyst, low_index, high_index, target):
    """Binary search helper function"""
    RecursionCounter()
    mid_index = (low_index + high_index) // 2
    mid_value = lyst[mid_index]

    if mid_value == target:
        return True

    if low_index >= high_index:
        return False

    if mid_value > target:
        return recursive_binary_search_helper(lyst, low_index, mid_index, target)

    if mid_value < target:
        return recursive_binary_search_helper(lyst, mid_index + 1, high_index, target)


def recursive_binary_search(lyst, target):
    """A function that performs the recursive binary search. """
    if all(isinstance(x, int) for x in lyst) and isinstance(target, int):
        low_index = 0
        high_index = len(lyst) - 1
        return recursive_binary_search_helper(lyst, low_index, high_index, target)
    raise ValueError("List and target must only be integers")


def jump_search(lyst, target):
    """A function that performs the jump search. """
    if all(isinstance(x, int) for x in lyst) and isinstance(target, int):
        step = math.sqrt(len(lyst))
        prev = 0
        while lyst[int(min(step, len(lyst)) - 1)] < target:
            prev = step
            step += math.sqrt(len(lyst))
            if prev >= len(lyst):
                return False
        while lyst[int(prev)] < target:
            prev += 1
            if prev == min(step, len(lyst)):
                return False
        if lyst[int(prev)] == target:
            return True

        return False
    raise ValueError("lyst and target must be integers")

def main():
    """This is the main function to run the program"""
    print("Creating a sorted array of 1,000,000")
    random.seed(0)
    data = sorted(random.sample(range(0, 10000000), 1000000))
    print("Finished creating sorted array of 1,000,000")
    print("")

    print("Searching for a number at the start of the array")
    start1 = time.perf_counter()
    linear_search(data, data[0])
    end1 = time.perf_counter()
    print(f"\tLinear search returned {linear_search(data, data[0])} in {end1 - start1} seconds")
    start1 = time.perf_counter()
    recursive_binary_search(data, data[0])
    end1 = time.perf_counter()
    print(f"\tRecursive binary search returned {recursive_binary_search(data, data[0])}"
          f" in {end1 - start1} seconds")
    start1 = time.perf_counter()
    jump_search(data, data[0])
    end1 = time.perf_counter()
    print(f"\tJump search returned {jump_search(data, data[0])} in"
          f" {end1 - start1} seconds")
    print("")

    print("Searching for a number in the middle of the array")
    mid_idx = len(data) // 2
    start1 = time.perf_counter()
    linear_search(data, data[0])
    end1 = time.perf_counter()
    print(f"\tLinear search returned {linear_search(data, data[mid_idx])} in"
          f" {end1 - start1} seconds")
    start1 = time.perf_counter()
    recursive_binary_search(data, data[mid_idx])
    end1 = time.perf_counter()
    print(f"\tRecursive binary search returned {recursive_binary_search(data, data[mid_idx])} in"
          f" {end1 - start1} seconds")
    start1 = time.perf_counter()
    jump_search(data, data[mid_idx])
    end1 = time.perf_counter()
    print(f"\tJump search returned {jump_search(data, data[mid_idx])} in"
          f" {end1 - start1} seconds")
    print("")

    print("Searching for number at the end of the array")
    start1 = time.perf_counter()
    linear_search(data, data[-1])
    end1 = time.perf_counter()
    print(f"\tLinear search returned {linear_search(data, data[-1])} in"
          f" {end1 - start1} seconds")
    start1 = time.perf_counter()
    recursive_binary_search(data, data[-1])
    end1 = time.perf_counter()
    print(f"\tRecursive binary search returned {recursive_binary_search(data, data[-1])} in"
          f" {end1 - start1} seconds")
    start1 = time.perf_counter()
    jump_search(data, data[-1])
    end1 = time.perf_counter()
    print(f"\tJump search returned {jump_search(data, data[-1])} in"
          f" {end1 - start1} seconds")
    print("")

    print("Searching for a number NOT in the array")
    start1 = time.perf_counter()
    linear_search(data, -1)
    end1 = time.perf_counter()
    print(f"\tLinear search returned {linear_search(data, -1)} in"
          f" {end1 - start1} seconds")
    start1 = time.perf_counter()
    recursive_binary_search(data, -1)
    end1 = time.perf_counter()
    print(f"\tRecursive binary search returned {recursive_binary_search(data, -1)} in"
          f" {end1 - start1} seconds")
    start1 = time.perf_counter()
    jump_search(data, -1)
    end1 = time.perf_counter()
    print(f"\tJump search returned {jump_search(data, -1)} in"
          f" {end1 - start1} seconds")
