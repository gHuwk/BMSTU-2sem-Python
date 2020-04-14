from tkinter import *
from tkinter import messagebox
import time
from random import *

def authorInfo():
    # GUI - Информация об авторе
    msg = 'Автор: Шиленков Алексей ИУ7-25Б.'
    messagebox.showinfo(title='Автор', message=msg)

def exInfo():
    # GUI - Информация о задании
    msg = 'Программа выводит значения времени выполнения сортировки вставками с барьером в сравнении со стандартным методом .sort() .'
    messagebox.showinfo(title='Задание', message=msg)
    
def menuAboutExAuthor(window):
    # GUI - Верхняя шапка
    mainmenu = Menu(window)
    window.config(menu=mainmenu)
    mainmenu.add_command(label='Задание', command=exInfo)
    mainmenu.add_command(label='Автор', command=authorInfo)
    

def warningError(what):
    msg = """Произошла ошибка.
            Пожалуйста проверьте вводимые данные.
            В задании указано, что нужно вводить неотрицательное количество элементов.
            Если у Вас возникли какие-то вопросы - пишите на почту :
            thelatunmask@gmail.com
            =======================
            Характер ошибки:
            
            """
    if what == 0:
        msg_bottom = "Есть пустые поля"
    elif what == 1:
        msg_bottom = "Проверьте правильность написания чисел"
    elif what == 2:
        msg_bottom = "Проблема в значениях. Проверьте, чтобы числа были правильно введены"
    messagebox.showerror(title='Внимание!', message=msg + msg_bottom)

        
#------------------------------------------------------------------------------
def geoWindow(window):
    # GUI - Расположение окна программы
    w = window.winfo_screenwidth() # ширина экрана
    h = window.winfo_screenheight() # высота экрана
    w = w//2 # середина экрана
    h = h//2 
    w = w - 188 # смещение от середины
    h = h - 153
    window.geometry('700x400+{}+{}'.format(w,h))
    

def outBlock(window): # Вывод ответа. Пока что просто данные, введенные в Entry
    outer = Label(window, bg='black', fg='white', width=25)
    outer.place(x = 100, y = 100)
    return outer

def frontendOwn(window, oldOwnArray, ownArray, ownTime):
    oldOwnArray = ' '.join(list(map(str, oldOwnArray)))
    ownArray = ' '.join(list(map(str, ownArray)))
    Label(window, bg='#cdcdcd', fg='black', width=len(oldOwnArray), text=oldOwnArray).place(x=200, y=0) # нужен #f0f0f0
    Label(window, bg='#cdcdcd', fg='black', width=len(ownArray), text=ownArray).place(x=200, y =30)
    Label(window, fg='black', text='Изначальный массив: ').place(x = 0, y = 0)
    Label(window, fg='black', text='Отсортированный массив: ').place(x = 0, y = 30)


def frontendTable(window):
    Label(window, fg='black', text='Произвольный: ').place(x = 0, y = 130)
    Label(window, fg='black', text='Упорядоченый: ').place(x = 0, y = 190)
    Label(window, fg='black', text='Обратный: ').place(x = 0, y = 250)
    Label(window, fg='black', text='Метод sort(): ').place(x = 0, y = 310)
    


#-------------------------------------------------------------------------------
def GUI():
    # GUI main - Основная подпрограмма для графического интерфейса
    def pasteData(window, data1, data2, data3):
        lb1_1 = Label(window, bg='#cdcdcd', fg='black', text="{:.5g}".format(data1[0]))
        lb1_1.place(x = 190, y = 130)
        lb1_2 = Label(window, bg='#cdcdcd', fg='black', text="{:.5g}".format(data1[1]))
        lb1_2.place(x = 190, y = 190)
        lb1_3 = Label(window, bg='#cdcdcd', fg='black', text="{:.5g}".format(data1[2]))
        lb1_3.place(x = 190, y = 250)
        lb1_4 = Label(window, bg='#cdcdcd', fg='black', text="{:.5g}".format(data1[3]))
        lb1_4.place(x = 190, y = 310)

        lb2_1 = Label(window, bg='#cdcdcd', fg='black', text="{:.5g}".format(data2[0]))
        lb2_1.place(x = 420, y = 130)
        lb2_2 = Label(window, bg='#cdcdcd', fg='black', text="{:.5g}".format(data2[1]))
        lb2_2.place(x = 420, y = 190)
        lb2_3 = Label(window, bg='#cdcdcd', fg='black', text="{:.5g}".format(data2[2]))
        lb2_3.place(x = 420, y = 250)
        lb2_4 = Label(window, bg='#cdcdcd', fg='black', text="{:.5g}".format(data2[3]))
        lb2_4.place(x = 420, y = 310)

        Label(window, bg='#cdcdcd', fg='black', text="{:.5g}".format(data3[0])).place(x = 600, y = 130)
        Label(window, bg='#cdcdcd', fg='black', text="{:.5g}".format(data3[1])).place(x = 600, y = 190)
        Label(window, bg='#cdcdcd', fg='black', text="{:.5g}".format(data3[2])).place(x = 600, y = 250)
        Label(window, bg='#cdcdcd', fg='black', text="{:.5g}".format(data3[3])).place(x = 600, y = 310)


    
    def clearFunc():
        entryN1.delete(0,END)
        entryN2.delete(0,END)
        entryN3.delete(0,END)
        entryLocationFrom.delete(0,END)
        entryLocationTo.delete(0,END)
        entryN1.place()
        entryN2.place()
        entryN3.place()
        entryLocationFrom.place()
        entryLocationTo.place()
        lb1_1['text'] = ''
        #outer['text'] = ''

    def answer():
        From = entryLocationFrom.get()
        To = entryLocationTo.get()
        print(From, '*', To)
        n1 = entryN1.get()
        n2 = entryN2.get()
        n3 = entryN3.get()
        print(n1,n2,n3,sep="*")
        if len(From) * len(To) * len(n1) * len(n2) * len(n3) != 0:
            if len(From.split())==1 and len(To.split())==1 and len(n1.split())==1 and len(n2.split())==1 and len(n3.split())==1:
                cache = From + To + n1 + n2 + n3
                flag = 1
                count = 0
                for cell in cache:
                    if cell in "0123456789-":
                        if '-' in cell:
                            count += 1
                    else:
                        flag = 0
                if count > 2:
                    c = 0
                    for cell in From:
                        if '-' in cell:
                            c+=1
                    if c > 1:
                        flag = 0
                    elif c < 1:
                        flag = 0

                        
                if flag:
                    if int(From) < int(To) and int(n1) > 0 and int(n2) > 0 and int(n3) > 0:
                        print("Passed")
                        data1, data2, data3 = backendTable(window,From,To,n1,n2,n3)
                        pasteData(window, data1, data2, data3)
                    else:
                        warningError(2)
                        # N меньше нуля. Так нельзя
                else:
                    warningError(1)
                    print("Hello")
                    
            else:
                warningError(1)
                #Больше одного числа
        else:
            warningError(0)
            #Пусто
    
    window = Tk()
    window.title('Table')
    window.resizable(False, False)
    geoWindow(window)
    menuAboutExAuthor(window)
    oldOwnArray, ownArray, ownTime = backendOwn(window)
    frontendOwn(window, oldOwnArray, ownArray, ownTime)

    entryN1 = Entry(width = 10)
    Label(window, fg='black', text='N1: ').place(x = 180, y = 100)
    entryN1.place(x = 210, y = 100)

    entryN2 = Entry(width = 10)
    Label(window, fg='black', text='N2: ').place(x = 370, y = 100)
    entryN2.place(x = 400, y = 100)

    entryN3 = Entry(width = 10)
    Label(window, fg='black', text='N3: ').place(x = 560, y = 100)
    entryN3.place(x = 590, y = 100)

    Label(window, fg='black', text='Занесите требуемые значения в таблицу:     Диапазон:  От').place(x = 0, y = 70)
    entryLocationFrom = Entry(width = 10)
    entryLocationTo = Entry(width = 10)
    entryLocationFrom.place(x = 330, y = 70)
    Label(window, fg='black', text ='До').place(x = 400, y = 70)
    entryLocationTo.place(x = 420, y = 70)
    
    

    
    answerButton = Button(window, text='Обновить',width = 20, command=answer)
    answerButton.place(x=500, y = 30)

    clearButton = Button(window, text='Очистить ввод',width = 20,command=clearFunc)
    clearButton.place(x=500, y=0)
    
    frontendTable(window)
    
    window.mainloop()

def backendTable(window,From,To,n1,n2,n3):
    From = int(From)
    To = int(To)
    n1 = int(n1)
    n2 = int(n2)
    n3 = int(n3)
    data1 = [0,0,0,0]
    data2 = [0,0,0,0]
    data3 = [0,0,0,0]
    
    arrayOne = [ randint(From,To) for ite in range(n1) ]
    arrayOneOld = arrayOne
    
    times = time.time() # Рандомный
    arrayOne = ins_with_bars(arrayOne)
    times = time.time() - times
    data1[0] = times
    
    times = time.time() # Упорядоченный
    arrayOne = ins_with_bars(arrayOne)
    times = time.time() - times
    data1[1] = times

    arrayOne = arrayOne[::-1] # Реверс
    times = time.time()
    arrayOne = ins_with_bars(arrayOne)
    times = time.time() - times
    data1[2] = times

    times = time.time() # .sort()
    arrayOneOld.sort()
    times = time.time() - times
    data1[3] = times

    print(data1)

    arrayTwo = [ randint(From,To) for ite in range(n2) ]
    arrayTwoOld = arrayTwo
    
    times = time.time() # Рандомный
    arrayTwo = ins_with_bars(arrayTwo)
    times = time.time() - times
    data2[0] = times
    
    times = time.time() # Упорядоченный
    arrayTwo = ins_with_bars(arrayTwo)
    times = time.time() - times
    data2[1] = times

    arrayTwo = arrayTwo[::-1] # Реверс
    times = time.time()
    arrayTwo = ins_with_bars(arrayTwo)
    times = time.time() - times
    data2[2] = times

    times = time.time() # .sort()
    arrayTwoOld.sort()
    times = time.time() - times
    data2[3] = times

    print(data2)

    arrayThree = [ randint(From,To) for ite in range(n3) ]
    arrayThreeOld = arrayThree
    
    times = time.time() # Рандомный
    arrayThree = ins_with_bars(arrayThree)
    times = time.time() - times
    data3[0] = times
    
    times = time.time() # Упорядоченный
    arrayThree = ins_with_bars(arrayThree)
    times = time.time() - times
    data3[1] = times

    arrayThree = arrayThree[::-1] # Реверс
    times = time.time()
    arrayThree = ins_with_bars(arrayThree)
    times = time.time() - times
    data3[2] = times

    times = time.time() # .sort()
    arrayThreeOld.sort()
    times = time.time() - times
    data3[3] = times

    print(data3)

    return data1, data2, data3

    
    
############ outer['text'] = ' '.join(string) Вот так вот вывод в лейбл


def listToStr(cache): # Перевод полученного массива в обратно в число.
    out = ''
    for i in range(len(cache)):
        out += str(cache[i])
    return out

def backendOwn(window): # Задание с собственным массивом
    ownArray = [ randint(-100, 100) for ite in range(10) ]
    oldOwnArray = ownArray
    ownTimeBegin = time.time()
    ownArray = ins_with_bars(ownArray)
    ownTime = time.time() - ownTimeBegin
    return oldOwnArray, ownArray, ownTime
    
    
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
    initial = array[1:]
    return initial

GUI()
