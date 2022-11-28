from tkinter import *
from tkinter import ttk
from tkinter import messagebox


window = Tk()
window.geometry("400x400")
window.title("Нолики-Крестики")

lbl = ttk.Label(window, text="Игра началась: ")
lbl.grid(column=1, row=0)

char = "X"
x_pos = []
o_pos = []

win_comb = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    [0, 4, 8],
    [2, 4, 6],
]

buttons = []


def click(i):
    global char

    if char == "X" and (i not in o_pos):
        buttons[i].configure(text=char)
        x_pos.append(i)
        char = "O"

    elif char == "O" and (i not in x_pos):
        buttons[i].configure(text=char)
        o_pos.append(i)
        char = "X"

    if len(x_pos) > 2 or len(o_pos) > 2:
        for pl_pos in (x_pos, o_pos):
            for w_comb in win_comb:
                if all(pos in pl_pos for pos in w_comb):
                    if char == "0":
                        messagebox.showinfo("Победитель", "O Победил")
                        window.quit()
                    else:
                        messagebox.showinfo("Победитель", "X Победил")
                        window.quit()


for idx in range(9):
    buttons.append(ttk.Button(text=" ", command=lambda i=idx: click(i)))
    buttons[idx].grid(column=int(idx % 3), row=int(idx / 3) + 1)

window.mainloop()
