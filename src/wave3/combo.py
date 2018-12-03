from tkinter import *
from tkinter import ttk
import glob


def get_list():
    ls = glob.glob("./*.png")
    for i in range(len(ls)):
        ls[i] = ls[i][2:]
    return ls


def button1_clicked():
    ('v1.%s' % v1.get())
    quit()


def cb_selected(event):
    print('v1 = %s ' % v1.get())


if __name__ == '__main__':
    root = Tk()
    root.title('Combobox 1')

    # Frame
    frame1 = ttk.Frame(root, padding=10)
    frame1.grid()

    # Combobox
    v1 = StringVar()
    cb = ttk.Combobox(frame1, textvariable=v1)
    cb.bind('<<ComboboxSelected>>', cb_selected)
    lst = tuple(get_list())
    cb['values'] = lst
    cb.set("ファイルを選択してください")
    cb.grid(row=0, column=0)

    # Button
    button1 = ttk.Button(frame1, text='OK', command=button1_clicked)
    button1.grid(row=0, column=1)

    root.mainloop()
