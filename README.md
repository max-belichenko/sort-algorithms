# sort-algorithms

<h1>Bubble sort</h1>
<h3>bubble_sort.py</h3>
Реализован алгоритм сортировки массива "пузырковым" методом.<br>
Данные на входе: массив произвольной длины из элементов, поддерживающих сравнение между собой.<br>
Данные на выходе: отсортированный по возрастанию массив элементов.<br>
<u>Сложность алгоритма:</u> O(n*n)<br><br>

<h1>Quick sort</h1>
<h3>quick_sort.py</h3>
Реализован алгоритм "быстрой сортировки" массива.<br>
Данные на входе: массив произвольной длины из элементов, поддерживающих сравнение между собой.<br>
Данные на выходе: отсортированный по возрастанию массив элементов.<br>
<u>Сложность алгоритма:</u> O(n log(n))<br><br>

<h1>Merge sort</h1>
<h3>merge_sort.py</h3>
Реализован алгоритм сортировки массива "слиянием".<br>
Данные на входе: массив произвольной длины из элементов, поддерживающих сравнение между собой.<br>
Данные на выходе: отсортированный по возрастанию массив элементов.<br>
<u>Сложность алгоритма:</u> O(n log(n))<br><br>

<hr>
<h1>Тестирование скорости сортировки</h1>
<h3>test_sorting_speed.py</h3>
Производит сравнительное измерение времени сортировки различными алгоритмами.<br>
<br>
Параметры измерения:<br>
<ul>
<li>Количество элементов в массиве</li>
<li>Элементы массива уникальны/могут повторяться</li>
<li>Массив изначально отсортирован/не отсортирован</li>
<li>Количество раундов сортировки в тесте</li>
</ul>