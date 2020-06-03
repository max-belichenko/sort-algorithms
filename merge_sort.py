"""
This module implements "merge sort" algorithm to sort an array.
"""


def mergeArrays(array_1, array_2):
    array_merged = []

    idx_1 = 0
    idx_2 = 0
    length_1 = len(array_1)
    length_2 = len(array_2)

    while idx_1 < length_1 and idx_2 < length_2:
        if array_1[idx_1] < array_2[idx_2]:
            array_merged.append(array_1[idx_1])
            idx_1 += 1
        else:
            array_merged.append(array_2[idx_2])
            idx_2 += 1

    if idx_1 == length_1:
        array_merged.extend(array_2[idx_2:])
    else:
        array_merged.extend(array_1[idx_1:])

    return array_merged


def mergeSort(array):
    """
    Sort incoming array in ascending order with merge-sort algorithm.

    :param array:
    :return array:
    """
    array_length = len(array)

    if array_length <= 1:
        return array

    median = array_length // 2

    left_part = mergeSort(array[:median])
    right_part = mergeSort(array[median:])

    return mergeArrays(left_part, right_part)


if __name__ == '__main__':
    from array_manager import print_array, generate_array

    array = generate_array(array_size=100, is_unique=True)
    print_array(array, f'Array [{len(array)}]')
    array = mergeSort(array)
    print_array(array, f'Sorted array [{len(array)}]')
