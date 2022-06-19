import bisect


def binary_search(sorted_collection: list[int], item: int) -> int | None:
    """Pure implementation of binary search algorithm in Python

    Be careful collection must be ascending sorted, otherwise result will be
    unpredictable

    :param sorted_collection: some ascending sorted collection with comparable items
    :param item: item value to search
    :return: index of found item or None if item is not found

    Examples:
    >>> binary_search([0, 5, 7, 10, 15], 0)
    0

    >>> binary_search([0, 5, 7, 10, 15], 15)
    4

    >>> binary_search([0, 5, 7, 10, 15], 5)
    1

    >>> binary_search([0, 5, 7, 10, 15], 6)

    """
    left = 0
    right = len(sorted_collection) - 1

    while left <= right:
        # https://ai.googleblog.com/2006/06/extra-extra-read-all-about-it-nearly.html
        midpoint = left + (right - left) // 2
        current_item = sorted_collection[midpoint]
        if current_item == item:
            return midpoint
        elif item < current_item:
            right = midpoint - 1
        else:
            left = midpoint + 1
    return None


def binary_search_by_recursion(
    sorted_collection: list[int], item: int, left: int, right: int
) -> int | None:
    """Pure implementation of binary search algorithm in Python by recursion

    Be careful collection must be ascending sorted, otherwise result will be
    unpredictable
    First recursion should be started with left=0 and right=(len(sorted_collection)-1)

    :param sorted_collection: some ascending sorted collection with comparable items
    :param item: item value to search
    :return: index of found item or None if item is not found

    Examples:
    >>> binary_search_by_recursion([0, 5, 7, 10, 15], 0, 0, 4)
    0

    >>> binary_search_by_recursion([0, 5, 7, 10, 15], 15, 0, 4)
    4

    >>> binary_search_by_recursion([0, 5, 7, 10, 15], 5, 0, 4)
    1

    >>> binary_search_by_recursion([0, 5, 7, 10, 15], 6, 0, 4)

    """
    if right < left:
        return None

    # https://ai.googleblog.com/2006/06/extra-extra-read-all-about-it-nearly.html
    midpoint = left + (right - left) // 2

    if sorted_collection[midpoint] == item:
        return midpoint
    elif sorted_collection[midpoint] > item:
        return binary_search_by_recursion(sorted_collection, item, left, midpoint - 1)
    else:
        return binary_search_by_recursion(sorted_collection, item, midpoint + 1, right)


def binary_search_std_lib(sorted_collection: list[int], item: int) -> int | None:
    """Pure implementation of binary search algorithm in Python using stdlib

    Be careful collection must be ascending sorted, otherwise result will be
    unpredictable

    :param sorted_collection: some ascending sorted collection with comparable items
    :param item: item value to search
    :return: index of found item or None if item is not found

    Examples:
    >>> binary_search_std_lib([0, 5, 7, 10, 15], 0)
    0

    >>> binary_search_std_lib([0, 5, 7, 10, 15], 15)
    4

    >>> binary_search_std_lib([0, 5, 7, 10, 15], 5)
    1

    >>> binary_search_std_lib([0, 5, 7, 10, 15], 6)

    """
    index = bisect.bisect_left(sorted_collection, item)
    if index != len(sorted_collection) and sorted_collection[index] == item:
        return index
    return None
