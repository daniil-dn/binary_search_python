def naive_search(lt, target):
    # example = [1, 3, 10, 12, 15]
    for i in range(len(lt)):
        if lt[i] == target:
            return i
    return -1


# binary search uses divide and conquer!
# we will leverage the fact that our list is SORTED

def binary_search(lt, target, low=None, high=None):
    if low is None:
        low = 0
    if high is None:
        high = len(lt) - 1

    if high < low:
        return -1

    midpoint = (low + high) // 2

    if lt[midpoint] == target:
        return midpoint

    elif target < lt[midpoint]:  # left side
        return binary_search(lt, target, low, midpoint - 1)
    else:
        # target > lt[midpoint]:#right side
        return binary_search(lt, target, midpoint + 1, high)


import random
import time

if __name__ == "__main__":
    list_example = [n for n in range(10000000)]
    # print(list_example)
    print(naive_search(list_example, 2))
    print(binary_search(list_example, 2))

    length = 10000
    sorted_list = set()
    while len(sorted_list) < length:
        sorted_list.add(random.randrange(-3 * length, 3 * length))
    sorted_list = sorted(list(sorted_list))
    start = time.time()
    for target in sorted_list:
        naive_search(sorted_list, target)
    end = time.time()
    print('naive search time: ', (end - start) / length, 'per seconds')
    start = time.time()
    for target in sorted_list:
        binary_search(sorted_list, target)
    end = time.time()
    print('binary search time: ', (end - start) / length, 'per seconds')
