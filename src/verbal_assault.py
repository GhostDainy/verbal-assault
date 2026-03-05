import tkinter as tk
from pathlib import Path
from random import randint, choice
from tkinter import messagebox

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_FILE = BASE_DIR / "data" / "words.txt"

# def AddWord():
#     value = EnterText.get()
#     if value != '':
#
#         with open('How.txt', 'a+', encoding = 'utf-8') as file:
#             file.write(value + '\n')
#         EnterText.delete(0, 'end')
#     else:
#         tk.messagebox.showinfo('Error', ('Empty writing field. '))

def AddWord():
    value = EnterText.get()

    if value != "":
        with open(DATA_FILE, "a", encoding="utf-8") as file:
            file.write(value + "\n")

        EnterText.delete(0, 'end')

    else:
        tk.messagebox.showinfo("Error", "Empty writing field")

def RandomWord():
    with open(DATA_FILE, "r", encoding="utf-8") as file:
        lines = file.readlines()
        tk.messagebox.showinfo('Idea', (choice(lines)))

def EnterClick(r):
    AddWord()

window = tk.Tk()

window.resizable(width = False, height = False)

window.title('VERBAL ASSAULT')

window.geometry('720x360')

window['bg'] = "blue"

idea = tk.Label(window, text = "Add word", font = ('Arial Bold', 20), fg = "red", bg = "blue")
idea.place(x = 290, y = 25)

EnterText = tk.Entry(fg = "green", bg = "white", width = 47)
EnterText.place(x = 220, y = 65)

btn = tk.Button(window, text = 'Add', command = AddWord, width = '40', height = '2', fg = 'red', bg = 'blue')
btn.place(x = 220, y = 110)

window.bind('<Return>', EnterClick)

GiveWord = tk.Label(window, text = 'Generate a word', font = ('Arial Bold', 20), fg = "red", bg = "blue")
GiveWord.place(x = 260, y = 170)

btn = tk.Button(window, text = 'Show word', command = RandomWord, width = '40', height = '2', fg = 'red', bg = 'blue')
btn.place(x = 220, y = 210)

window.mainloop()

