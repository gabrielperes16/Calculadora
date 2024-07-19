import tkinter as tk
from typing import List

def make_root() -> tk.Tk:
    root = tk.Tk()
    root.title('Calculator')
    root.config(padx=10, pady=10, background='#84D5CA')
    root.resizable(False,False)
    return root

def make_label(root) -> tk.Label:
    label = tk.Label(
        root, text='Sem Nenhum Calculo!',
        anchor='e', justify='right', background='#000000'
    )
    label.grid(row=0, column=0, columnspan=5, sticky='news')
    return label

def make_display(root) -> tk.Entry:
    display = tk.Entry(root)
    display.grid(row=1, column=0, columnspan=5, sticky='news', pady=(0, 10))
    display.config(
        font=('Helvetica', 40, 'bold'),
        justify='right',
        bd=1,
        relief='flat',
        highlightthickness=1,
        highlightcolor='#ccc'
    )
    display.bind('<Control-a>', display_control_a)
    return display

def display_control_a(event=None):
    event.widget.select_range(0, 'end')
    event.widget.icursor('end')
    return 'break'

def make_buttons(root) -> List[List[tk.Button]]:
    button_texts = [
        ['7', '8', '9', '/','C'],
        ['4', '5', '6', '*','-'],
        ['1', '2', '3', '^','+'],
        ['0', '.', '(', ')','=']
    ]
    buttons = []
    for row_position, row_value in enumerate(button_texts, start=2):
        button_row = []
        for col_position, col_value in enumerate(row_value):
            btn = tk.Button(root, text=col_value)
            btn.grid(row=row_position, column=col_position, sticky='news', padx=5, pady=5)
            btn.config(
                font=('Helvetica', 15, 'normal'),
                pady=40,
                width=1,
                background='#f1f2f3',
                bd=0,
                cursor='hand2',
                highlightthickness=0,
                highlightcolor='#ccc',
                highlightbackground='#ccc',
                activebackground='#ccc'
            )
            button_row.append(btn)
        buttons.append(button_row)
    return buttons
