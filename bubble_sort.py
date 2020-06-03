"""
This module implements "bubble sort" algorithm to sort an array.
"""


def bubbleSort(array):
    """
    Sort incoming array in ascending order with bubble-sort algorithm.

    :param array:
    :return array:
    """
    array_length = len(array)

    for idx1 in range(array_length - 1):
        for idx2 in range(array_length - 1 - idx1):
            if array[idx2] > array[idx2 + 1]:
                array[idx2 + 1], array[idx2] = array[idx2], array[idx2 + 1]

    return array


if __name__ == '__main__':
    from array_manager import print_array, generate_array

    array = generate_array(array_size=100, is_unique=True)
    print_array(array, f'Array [{len(array)}]')
    array = bubbleSort(array)
    print_array(array, f'Sorted array [{len(array)}]')
