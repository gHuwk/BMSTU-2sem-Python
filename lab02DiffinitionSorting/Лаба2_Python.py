from tkinter import *
from time import *
from random import *

def ins_with_bars(initial):
    array = [0] + initial
    for i in range(1,len(array)):
        if array[i-1] > array[i]:
            array[0] = array[i]
            j = i - 1
            while array[j] > array[0]:
                array[j+1] = array[j]
                j -= 1
            array[j+1] = array[0]
            #print(array)
    initial = array[1:]
    return initial

tm = perf_counter() # Время, когда началось высчитывание


#random.randrange(start, stop, step) - возвращает случайно выбранное число из последовательности.
#random.randint(A, B) - случайное целое число N, A ≤ N ≤ B.
