"""
Run three different sort algorithms and note the time it takes to sort specified array of numbers.

Sort algorithms:
    Bubble Sort - average: O(n*n)
    Quick Sort - best: O(n log n) worst: O(n*n)
    Merge Sort - average: O(n log n)
"""
import random
import time

from array_manager import print_array, generate_array
from bubble_sort import bubbleSort
from quick_sort import quickSort
from merge_sort import mergeSort


"""
    Array generator settings.
"""
# Set amount of elements in array
ARRAY_SIZE = 500

# Set amount of rounds to sort array
ROUNDS = 1_000

# All elements are unique or can be repeated?
IS_UNIQUE = True

# Set this to True to create sorted arrays
IS_SORTED = False


if __name__ == '__main__':
    # Generate an array.
    generated_array = generate_array(ARRAY_SIZE, IS_UNIQUE, IS_SORTED)

    print(f'Parameters of testing:\n'
          f'\tArray size: {ARRAY_SIZE}\n'
          f'\tUnique elements: {IS_UNIQUE}\n'
          f'\tArray is already sorted: {IS_SORTED}\n'
          f'\tSorting rounds: {ROUNDS}\n')
    print_array(generated_array, text=f'Array [{len(generated_array)}]')

    # Time up bubble sort.
    print('\nBubble sort...')
    array = generated_array.copy()

    start_time = time.perf_counter()
    for i in range(ROUNDS):
        bubbleSort(array.copy())
    end_time = time.perf_counter()

    bubbleSort(array)
    print_array(array, text=f'Bubble sorted array [{len(array)}]')
    print('{:>30} : {:.6f} seconds'.format(f'Elapsed time ({ROUNDS} rounds)', end_time - start_time))

    # Time up quick sort.
    print('\nQuick sort...')
    array = generated_array.copy()

    start_time = time.perf_counter()
    for i in range(ROUNDS):
        quickSort(array.copy())
    end_time = time.perf_counter()

    array = quickSort(array)
    print_array(array, text=f'Quick sorted array [{len(array)}]')
    print('{:>30} : {:.6f} seconds'.format(f'Elapsed time ({ROUNDS} rounds)', end_time - start_time))

    # Time up merge sort.
    print('\nMerge sort...')
    array = generated_array.copy()
    # print_array(array, text=f'Array [{len(array)}]')

    start_time = time.perf_counter()
    for i in range(ROUNDS):
        mergeSort(array.copy())
    end_time = time.perf_counter()

    array = mergeSort(array)
    print_array(array, text=f'Merge sorted array [{len(array)}]')
    print('{:>30} : {:.6f} seconds'.format(f'Elapsed time ({ROUNDS} rounds)', end_time - start_time))

    # # Time up Python sort.
    print('\nPython sort...')
    array = generated_array.copy()

    start_time = time.perf_counter()
    for i in range(ROUNDS):
        sorting_array = array.copy()
        sorting_array.sort()
    end_time = time.perf_counter()

    array.sort()
    print_array(array, text=f'Python sorted array [{len(array)}]')
    print('{:>30} : {:.6f} seconds'.format(f'Elapsed time ({ROUNDS} rounds)', end_time - start_time))
