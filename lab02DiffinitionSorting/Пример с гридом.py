from tkinter import *
root = Tk()
Button(root, text = '1').grid(row = 1, column = 1)
Button(root, text = '2').grid(row = 1, column = 3)
Button(root, text = '3').grid(row = 2, column = 1, columnspan = 2)
root.mainloop()
