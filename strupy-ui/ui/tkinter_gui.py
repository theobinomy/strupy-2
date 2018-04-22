from tkinter import *
from tkinter import ttk

window = Tk()
window.title("Welcome to LikeGeeks app")
tab_control = ttk.Notebook(window)
tab1 = ttk.Frame(tab_control)
tab2 = ttk.Frame(tab_control)
tab_control.add(tab1, text='First')
tab_control.add(tab2, text='second')
tab_control.pack(expand=2, fill='both')
def pressed():
    print('you pressed')
but1= ttk.Button(window, text = 'press', command = pressed).pack()
entry = Entry(window)
entry.pack()
entry.insert(0,'some text')
window.configure(background = '#aa00ff')
window.mainloop()