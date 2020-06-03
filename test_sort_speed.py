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


if __name__ == '__main__':
    # Set up timing environment.
    rounds = 1_000  # How many rounds algorithm will sort an array.
    array_size = 500    # How many elements are in array.
    is_unique = True   # All elements are unique or can be repeated?
    is_sorted = False   # Elements in array are in sorted or unsorted order?

    array = generate_array(array_size, is_unique, is_sorted)

    print_array(array, text=f'Array [{len(array)}]')

    # Time up bubble sort.
    start_time = time.perf_counter()
    for i in range(rounds):
        bubbleSort(array)
    end_time = time.perf_counter()
    bubble_time = end_time - start_time
    bubbled_array = bubbleSort(array)

    # Time up quick sort.
    start_time = time.perf_counter()
    for i in range(rounds):
        quickSort(array)
    end_time = time.perf_counter()
    quick_time = end_time - start_time
    quicked_array = quickSort(array)

    # Time up merge sort.
    start_time = time.perf_counter()
    for i in range(rounds):
        mergeSort(array)
    end_time = time.perf_counter()
    merge_time = end_time - start_time
    merged_array = mergeSort(array)

    # Summary.
    print_array(bubbled_array, text=f'Bubble sorted array [{len(bubbled_array)}]')
    print('{:>30} : {:.6f} seconds'.format(f'Elapsed time ({rounds} rounds)', bubble_time))
    print_array(bubbled_array, text=f'Quick sorted array [{len(quicked_array)}]')
    print('{:>30} : {:.6f} seconds'.format(f'Elapsed time ({rounds} rounds)', quick_time))
    print_array(bubbled_array, text=f'Merge sorted array [{len(merged_array)}]')
    print('{:>30} : {:.6f} seconds'.format(f'Elapsed time ({rounds} rounds)', merge_time))