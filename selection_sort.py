def selection_sort(array):
    """
    Выполняет сортировку массива "выбором".

    :param array: Исходный массив
    :return: Отсортированный массив
    """
    sorted_array = []

    for i in range(len(array)):
        smallest = find_smallest_idx(array)
        sorted_array.append(array.pop(smallest))

    return sorted_array


def find_smallest_idx(array):
    """
    Ищет наименьший элемент в массиве.

    :param array:
    :return: Индекс наименьшего элемента.
    """
    smallest_idx = 0
    smallest = array[smallest_idx]
    for i in range(1, len(array)):
        if array[i] < smallest:
            smallest = array[i]
            smallest_idx = i
    return smallest_idx


if __name__ == '__main__':
    from random import randint

    numbers = [randint(0, 100) for x in range(randint(10, 100))]

    print(numbers)
    numbers = selection_sort(numbers)
    print(numbers)
