import random
import time  # for time complexity analysis


# this is a basic naive search in which we can pass a value and iterate over the whole list searching for it
def naive_search(el_list, target):
    for i in range(len(el_list)):
        if el_list[i] == target:
            return i
    return - 1


# SORTED list:
def binary_search(el_list, target, low=None, high=None):
    # el_list = [1, 3, 5, 7, 9]

    if low is None:
        low = 0
    if high is None:
        high = len(el_list) - 1

    if high < low:
        return - 1  # not on the list

    midpoint = (low + high) // 2  # this will keep the list being divided during recursion

    if el_list[midpoint] == target:
        return midpoint
    elif target < el_list[midpoint]:  # takes only the left portion and redo the list half division again
        return binary_search(el_list, target, low, midpoint - 1)
    else:
        return binary_search(el_list, target, midpoint + 1, high)


if __name__ == '__main__':
    # time complexity analysis: created a massive list and try to catch a number out of it
    length = 10000
    sorted_list = set()
    while len(sorted_list) < length:
        sorted_list.add(random.randint(-3 * length, 3 * length))  # a 60k range of int
    sorted_list = sorted(list(sorted_list))  # this will sort the list

    start = time.time()
    for target in sorted_list:
        naive_search(sorted_list, target)
    end = time.time()
    time_per_iteration = (end - start)/length
    print("Naive search time: ", time_per_iteration, "seconds")

    start = time.time()
    for target in sorted_list:
        binary_search(sorted_list, target)
    end = time.time()
    time_per_iteration = (end - start) / length
    print("Binary search time: ", time_per_iteration, "seconds")

    el_list = set()
    el_list_length = 60000
    while len(el_list) < el_list_length:
        el_list.add(random.randint(0, 59999))
    el_list = sorted(list(el_list))

    print("\nNow trying a more controlled scenario: \n")
    start = time.time()
    for target in el_list:
        naive_search(el_list, 33333)
    end = time.time()
    time_per_iteration = (end - start) / length
    print("Naive search time: ", time_per_iteration, "seconds")

    start = time.time()
    for target in el_list:
        binary_search(el_list, 33333)
    end = time.time()
    time_per_iteration = (end - start) / length
    print("Binary search time: ", time_per_iteration, "seconds")

