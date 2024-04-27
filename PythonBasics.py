import random

# Объявление пуситого списка
randomList = []
# Цикл на 100 итераций
for i in range(100):
    # Добавление в список случайных чисел в диапозоне от 0 до 1000
    randomList.append(random.randint(0, 1000))


# Алгоритм сортировки вставками (Insertion Sort)
# Объявление функции insertionSort
def insertion_sort(arr):
    # Проходим по каждому элементу, начиная со второго
    for i in range(1, len(arr)):
        key = arr[i]  # Текущий элемент, который нужно вставить в отсортированную часть
        j = i - 1  # Индекс последнего элемента в отсортированной части

        # Перемещаем все элементы больше key на одну позицию вперед
        # пока не найдем место, куда нужно вставить key
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        # Вставляем key в правильную позицию
        arr[j + 1] = key
    # Возврат результата работы фунуции
    return arr


# Задествуем функцию сортировки
sortedList = insertion_sort(randomList)

# Объявление переменных для суммы и количества чётных и нечётных элементов
summEven = 0
countEven = 0
summOdd = 0
countOdd = 0

# Проходим по элементам массива
for numm in sortedList:
    # Если чётное
    if numm % 2 == 0:
        summEven += numm
        countEven += 1
    # Если не чётное
    else:
        summOdd += numm
        countOdd += 1

# Вычесление среднее арифметическое для чётных и нечётных чисел (учитываем деление на 0)
avgEven = summEven / countEven if countEven > 0 else 0
avgOdd = summOdd / countOdd if countOdd > 0 else 0

# Вывод результат в консоль
print("Average for even is:", avgEven)
print("Average for odd is:", avgOdd)
