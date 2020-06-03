import unittest
import random

from bubble_sort import bubbleSort
from quick_sort import quickSort
from merge_sort import mergeSort


def generate_array(array_size, is_unique=True, is_sorted=False):
    if is_unique:
        array = [x for x in range(array_size)]
        if not is_sorted:
            random.shuffle(array)
    else:
        array = [random.randint(0, 100) for _ in range(array_size)]
        if is_sorted:
            array.sort()
    return array


class BubbleSortTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.empty_array = []
        self.array_1 = [random.randint(0, 100)]
        self.array_2 = generate_array(array_size=2)
        self.array_100_unique_sorted = generate_array(array_size=100, is_unique=True, is_sorted=True)
        self.array_100_non_unique_sorted = generate_array(array_size=100, is_unique=False, is_sorted=True)
        self.array_100_unique_not_sorted = generate_array(array_size=100, is_unique=True, is_sorted=False)
        self.array_100_non_unique_not_sorted = generate_array(array_size=100, is_unique=False, is_sorted=False)
        self.array_500 = generate_array(array_size=500)

    def test_sort_empty_array(self):
        self.assertEqual(bubbleSort(self.empty_array), [])

    def test_sort_array_1(self):
        self.assertEqual(bubbleSort(self.array_1), self.array_1)

    def test_sort_array_2(self):
        self.assertEqual(bubbleSort(self.array_2), sorted(self.array_2))

    def test_sort_array_100_unique_sorted(self):
        self.assertEqual(bubbleSort(self.array_100_unique_sorted), sorted(self.array_100_unique_sorted))

    def test_sort_array_100_non_unique_sorted(self):
        self.assertEqual(bubbleSort(self.array_100_non_unique_sorted), sorted(self.array_100_non_unique_sorted))

    def test_sort_array_100_unique_not_sorted(self):
        self.assertEqual(bubbleSort(self.array_100_unique_not_sorted), sorted(self.array_100_unique_not_sorted))

    def test_sort_array_100_non_unique_not_sorted(self):
        self.assertEqual(bubbleSort(self.array_100_non_unique_not_sorted), sorted(self.array_100_non_unique_not_sorted))

    def test_sort_array_500(self):
        self.assertEqual(bubbleSort(self.array_500), sorted(self.array_500))

    def test_many_sorts(self):
        for i in range(1_000):
            with self.subTest(i=i):
                array = generate_array(array_size=10)
                self.assertEqual(bubbleSort(array), sorted(array))


class QuickSortTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.empty_array = []
        self.array_1 = [random.randint(0, 100)]
        self.array_2 = generate_array(array_size=2)
        self.array_100_unique_sorted = generate_array(array_size=100, is_unique=True, is_sorted=True)
        self.array_100_non_unique_sorted = generate_array(array_size=100, is_unique=False, is_sorted=True)
        self.array_100_unique_not_sorted = generate_array(array_size=100, is_unique=True, is_sorted=False)
        self.array_100_non_unique_not_sorted = generate_array(array_size=100, is_unique=False, is_sorted=False)
        self.array_500 = generate_array(array_size=500)

    def test_sort_empty_array(self):
        self.assertEqual(quickSort(self.empty_array), [])

    def test_sort_array_1(self):
        self.assertEqual(quickSort(self.array_1), self.array_1)

    def test_sort_array_2(self):
        self.assertEqual(quickSort(self.array_2), sorted(self.array_2))

    def test_sort_array_100_unique_sorted(self):
        self.assertEqual(quickSort(self.array_100_unique_sorted), sorted(self.array_100_unique_sorted))

    def test_sort_array_100_non_unique_sorted(self):
        self.assertEqual(quickSort(self.array_100_non_unique_sorted), sorted(self.array_100_non_unique_sorted))

    def test_sort_array_100_unique_not_sorted(self):
        self.assertEqual(quickSort(self.array_100_unique_not_sorted), sorted(self.array_100_unique_not_sorted))

    def test_sort_array_100_non_unique_not_sorted(self):
        self.assertEqual(quickSort(self.array_100_non_unique_not_sorted), sorted(self.array_100_non_unique_not_sorted))

    def test_sort_array_500(self):
        self.assertEqual(quickSort(self.array_500), sorted(self.array_500))

    def test_many_sorts(self):
        for i in range(1_000):
            with self.subTest(i=i):
                array = generate_array(array_size=10)
                self.assertEqual(quickSort(array), sorted(array))


class MergeSortTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.empty_array = []
        self.array_1 = [random.randint(0, 100)]
        self.array_2 = generate_array(array_size=2)
        self.array_100_unique_sorted = generate_array(array_size=100, is_unique=True, is_sorted=True)
        self.array_100_non_unique_sorted = generate_array(array_size=100, is_unique=False, is_sorted=True)
        self.array_100_unique_not_sorted = generate_array(array_size=100, is_unique=True, is_sorted=False)
        self.array_100_non_unique_not_sorted = generate_array(array_size=100, is_unique=False, is_sorted=False)
        self.array_500 = generate_array(array_size=500)

    def test_sort_empty_array(self):
        self.assertEqual(mergeSort(self.empty_array), [])

    def test_sort_array_1(self):
        self.assertEqual(mergeSort(self.array_1), self.array_1)

    def test_sort_array_2(self):
        self.assertEqual(mergeSort(self.array_2), sorted(self.array_2))

    def test_sort_array_100_unique_sorted(self):
        self.assertEqual(mergeSort(self.array_100_unique_sorted), sorted(self.array_100_unique_sorted))

    def test_sort_array_100_non_unique_sorted(self):
        self.assertEqual(mergeSort(self.array_100_non_unique_sorted), sorted(self.array_100_non_unique_sorted))

    def test_sort_array_100_unique_not_sorted(self):
        self.assertEqual(mergeSort(self.array_100_unique_not_sorted), sorted(self.array_100_unique_not_sorted))

    def test_sort_array_100_non_unique_not_sorted(self):
        self.assertEqual(mergeSort(self.array_100_non_unique_not_sorted), sorted(self.array_100_non_unique_not_sorted))

    def test_sort_array_500(self):
        self.assertEqual(mergeSort(self.array_500), sorted(self.array_500))

    def test_many_sorts(self):
        for i in range(1_000):
            with self.subTest(i=i):
                array = generate_array(array_size=10)
                self.assertEqual(mergeSort(array), sorted(array))


if __name__ == '__main__':
    unittest.main()
