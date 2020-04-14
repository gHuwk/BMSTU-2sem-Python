from tkinter import *
from tkinter import messagebox
import matplotlib
matplotlib.use("TkAgg")
from matplotlib import pyplot as plt
import math as m
"""
def findDots():
    retrieved = getEntries()

    for 
    return dots 
    
"""


# 1 - PLOT // 2 - HELP // 3 - CODES
#  большое количество итераций
#  деление на ноль
#  несколько корней на одном промежутке
#  ГЛАДКИЙ ГРАФИК / ТОЧКИ И ОШИБКИ
#  x**5 - x**4 - x**3


def F(x):
    return x**5 - x**4 - x**3

def ff(x):
	return 20*x**3 - 12*x**2 - 6*x

def hordeMethod(a, b, eps, n, F, i=0):
    left,right = a,b
    while abs(F(a) > eps):
        fl = F(left)
        fr = F(right)
        left = left - fl / (fl - fr) * (left - right)
        i += 1
        if abs(F(left)) < eps or i > n:
            break
    return left, i

def clearEntries():
    #entries = (entry1, entry2, entry3, entry4)
    entries = (dxEntry, iterEntry, intervEntry, epsEntry)
    for entry in entries:
	    entry.delete(first=0, last=len(entry.get()))
    tableEntry.delete(index1=1.0, index2=END)
    pass

def intervParser(entry):
    string = entry.get()
    string.replace(' ','')
    ans = string.split(',')
    return ans

def getEntries():
    entries = (dxEntry, iterEntry, epsEntry, intervEntry)
    retrieved = ['∆', '∆', '∆', '∆']
    for i in range(3):
        retrieved[i] = entries[i].get()
    retrieved[3] = intervParser(entries[3])
    print(retrieved)
    return retrieved
    
def tableShow():
    retrieved = getEntries()
    for el in retrieved:
        if el == '' or el == ['','']:
            emptyMessage()
            return 1
    h = float(retrieved[0])
    eps = float(retrieved[2])
    maxIter = float(retrieved[1])
    beg = float(retrieved[3][0])
    end = float(retrieved[3][1])
    a = beg
    iteration = 0
    N = 0
    string  = '------------------------------------------------------------\n'
    string += '|  N  |    Отрезок    |    ~x    |    f(~x)    |  I  |Code|\n'
    string += '------------------------------------------------------------\n'
    while int(iteration) < maxIter - 1 and N < int((end - beg) / h):
        a += N * h
        appX, iteration =  hordeMethod(a, a+h, eps, maxIter, F, i=0)
        appFx = F(appX)
        ib = a
        ie = a+h
        N += 1
        code = ''
        string += ('|{:^5d}|{:^7.4g};{:^7.4g}|{:^10.4g}|{:^13.4g}|{:^5d}|{:^4}|\n').format(N, ib, ie, appX, appFx, int(iteration), code)
        string += '------------------------------------------------------------\n'
    print(string)
    tableEntry.insert(index=END, chars=string)
    pass

def plotShow():
    retrieved = getEntries()
    for el in retrieved:
        if el == '' or el == ['','']:
            emptyMessage()
            return 1
    xMin = xx = float(retrieved[3][0])
    xMax = xX = float(retrieved[3][1])
    dx = float(retrieved[0])
    eps = float(retrieved[2])
    maxIter = float(retrieved[1])
    roots = []
    N = 0
    a = xMin
    iteration = 0
    while iteration < maxIter and N < (xMax - xMin) // dx:
        a += N * dx
        appX, iteration =  hordeMethod(a, a+dx, eps, maxIter, ff, i=0)
        N += 1
        roots.append(appX)
    xList = []

    while xx < xX:
        xList.append(m.ceil(xx*100)/100)
        xx+=dx
    yList = [F(x) for x in xList]
    plt.plot (xList, yList)
    #roots = [-1.1, 1.0]
    print(xList)
    #mark = [xList.index(i) for i in roots]
    #plt.plot(xList,yList,markevery=mark, ls="", marker="o", label="points")
    grid1 = plt.grid(True)
    plt.show()

def emptyMessage():
    messagebox.showinfo('Введите все параметры','Вы ввели не все необходимые параметры.\n Проверьте ваш ввод.' )

def showAbout():
	messagebox.showinfo('О приложении', 'Приложение выводит таблицу корней уравнения и строит график функции этого уравнения.\nАвтор: Гимадеев Карим ИУ7-25Б')
	pass


HEIGHT = 600
WIDTH = 600
WHITE = '#FFFFFF'
YELLOW = '#EECC00'
FONT = 'Menlo'
LABELW = 150/WIDTH
LABELH = 30/HEIGHT
DX = 25

root = Tk()
root.resizable(width=False, height=False)
canvas = Canvas(root, height=HEIGHT, width=WIDTH, bg=YELLOW)
canvas.pack()

menuBar = Menu(root)
appmenu = Menu(menuBar, name='apple')
menuBar.add_cascade(menu=appmenu)
appmenu.add_command(label='О приложении', command=showAbout)
appmenu.add_separator()
root['menu'] = menuBar

dxLabel = Label(canvas, font=FONT, text='Шаг')
dxLabel.place(x=50, y=50, relwidth=LABELW, relheight=LABELH)

dxEntry = Entry(canvas, font=FONT)
dxEntry.place(x=50+25+150, y=50, relwidth=LABELW, relheight=LABELH)


iterLabel = Label(canvas, font=FONT, text='Предел итераций')
iterLabel.place(x=50, y=85, relwidth=LABELW, relheight=LABELH)

iterEntry = Entry(canvas, font=FONT)
iterEntry.place(x=50+DX+150, y=85, relwidth=LABELW, relheight=LABELH)

intervLabel = Label(canvas, font=FONT, text='Интервал')
intervLabel.place(x=50, y=120, relwidth=LABELW, relheight=LABELH)

intervEntry = Entry(canvas, font=FONT)
intervEntry.place(x=50+DX+150, y=120, relwidth=LABELW, relheight=LABELH)

epsLabel = Label(canvas, font=FONT, text='Точность')
epsLabel.place(x=50, y=155, relwidth=LABELW, relheight=LABELH)

epsEntry = Entry(canvas, font=FONT)
epsEntry.place(x=50+DX+150, y=155, relwidth=LABELW, relheight=LABELH)

tableEntry = Text(canvas, font=FONT)
scroll = Scrollbar(tableEntry)
scroll.pack(side=RIGHT, fill=Y)
tableEntry.place(x=50, y=200, relwidth=5/6, relheight=35/60)

clearButton = Button(canvas, font=FONT, text='Очистить поля')
clearButton.bind('<Button-1>', lambda event:clearEntries())
clearButton.place(x=50+2*(DX+150), y=85, relwidth=LABELW, relheight=LABELH) 

tableButton = Button(canvas, font=FONT, text='Вывод таблицы')
tableButton.bind('<Button-1>', lambda event:tableShow())
tableButton.place(x=50+2*(DX+150), y=120, relwidth=LABELW, relheight=LABELH) 

plotButton = Button(canvas, font=FONT, text='Вывод графика')
plotButton.bind('<Button-1>', lambda event:plotShow())
plotButton.place(x=50+2*(DX+150), y=155, relwidth=LABELW, relheight=LABELH) 

root.mainloop()