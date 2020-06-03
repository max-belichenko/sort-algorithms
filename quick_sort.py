"""
This module implements "quick sort" algorithm to sort an array.
"""


def getPivot(array):
    array_length = len(array)

    if array_length == 0:
        return None
    elif array_length < 5:
        return array[0]

    first_element = array[0]
    last_element = array[array_length - 1]
    middle_element = array[array_length // 2]

    if first_element <= middle_element <= last_element or last_element <= middle_element <= first_element:
        return middle_element
    elif middle_element <= last_element <= first_element or first_element <= last_element <= middle_element:
        return last_element
    elif last_element <= first_element <= middle_element or middle_element <= first_element <= last_element:
        return first_element


def quickSort(array):
    """
    Sort incoming array in ascending order with quick-sort algorithm.

    :param array:
    :return array:
    """
    array_length = len(array)

    if  array_length <= 1:
        return array

    if array_length == 2:
        if array[0] > array[1]:
            array[0], array[1] = array[1], array[0]
        return array

    pivot = getPivot(array)

    lessThanPivot = []
    equalPivot = []
    moreThanPivot = []

    for element in array:
        if element < pivot:
            lessThanPivot.append(element)
        elif element == pivot:
            equalPivot.append(element)
        elif element > pivot:
            moreThanPivot.append(element)

    return quickSort(lessThanPivot) + equalPivot + quickSort(moreThanPivot)


if __name__ == '__main__':
    from array_manager import print_array, generate_array

    array = generate_array(array_size=100, is_unique=True)
    print_array(array, f'Array [{len(array)}]')
    array = quickSort(array)
    print_array(array, f'Sorted array [{len(array)}]')