from matplotlib import *
from tkinter import *
from random import *
from math import *

def Function(x):
    #Нужная функция
    return x - x ** 3 + 7
    
def GUI():
    #Ввод - Отрезок, точность, шаг, количество итераций
    #Вывод - таблица значений, график через метод
    root = Tk()
    eps = 0.0001
    sig = 0.001
    iters = 100
    begin = -1
    end = 1
    Back(root,eps,sig,iters,begin,end)

def Back(root,eps,sig,iters,begin,end):
    #Метод половинного деления.
    #eps - точность
    #sig - шаг
    #iters - количество итераций
    #begin - начало отрезка
    #end - конец отрезка
    a = begin
    b = end
    left = a
    right = b
    midle = 0.5*(left+right)
    while abs(Function(midle)) >= eps:
        if Function(midle) * Function(left) < 0:
            right = midle
            print("right")
        if Function(midle) * Function(right) < 0:
            left = midle
            print("left")
        midle = 0.5*(left+right)
        print(Function(midle), midle, right, left, eps, sep=" | ")

GUI()
