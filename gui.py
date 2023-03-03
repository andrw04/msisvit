from tkinter import *
from tkinter import ttk
from tkinter import filedialog


def read_from_file():
    file_path = filedialog.askopenfilename()
    text_editor.delete("1.0", END)
    if file_path != "":
        with open(file_path, "r") as file:
            txt = file.read()
            text_editor.insert("1.0", txt)


def start():
    # Создание нового окна
    window = Tk()
    window.title("Result")

    # Создание таблицы
    columns = ("j","operator","f1","i","operand","f2")
    table = ttk.Treeview(window, columns=columns, show="headings")
    table.pack(fill=BOTH, expand=1)

    # Отделяем заголовки
    table.heading("j",text="j")
    table.heading("operator", text="Оператор")
    table.heading("f1",text="f[1,j]")
    table.heading("i",text="i")
    table.heading("operand",text="Операнд")
    table.heading("f2",text="f[2,i]")

    # Получение текста
    txt = text_editor.get("1.0", "end")


root = Tk()
root.title("Holstead metrics")
root.grid_rowconfigure(index=0, weight=1)
root.grid_columnconfigure(index=0, weight=2)
root.grid_columnconfigure(index=1, weight=1)

text_editor = Text()
text_editor.grid(row=0, column=0, columnspan=2)

start_btn = Button(text="Start", command=start)
start_btn.grid(row=1,column=0)

read_btn = Button(text="Read from file", command=read_from_file)
read_btn.grid(row=1, column=1)

root.mainloop()
