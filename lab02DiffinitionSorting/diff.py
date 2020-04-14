
# Защита второй лабы

def bubble(array):
    N = len(array)
    for i in range(N-1):
        flag = False
        for j in range(N-i-1):
            if array[j] > array[j+1]:
                array[j],array[j+1] = array[j+1],array[j]
                flag = True
        if not flag:
            break


print("Введите массив по элементам через пробелы: \n")
array = list(map(int, input().split()))
print(array)
print("Отсортируем через пузырек с флагом: ")

bubble(array)
print(array)
