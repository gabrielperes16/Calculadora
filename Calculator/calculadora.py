import tkinter as tk
from typing import List, Callable
import re
import math

class CalculatorGui:
    """ Manages tkinter """

    def __init__(
        self,
        root: tk.Tk,
        label: tk.Label,
        display: tk.Entry,
        button_list: List[List[tk.Button]],
        do_calculate: Callable[[str], str]
    ) -> None:
        self.root = root
        self.label = label
        self.display = display
        self.button_list = button_list
        self.do_calculate = do_calculate

    def start(self) -> None:
        """Start the gui"""
        self._config_display()
        self._config_buttons()
        self.root.mainloop()

    def _config_display(self) -> None:
        """Display configs"""
        self.display.bind('<Return>',self.calculate)
        self.display.bind('<KP_Enter>',self.calculate)

    def fixed_text(self,text):
        text=re.sub(r'[^\d\.\/\*\-\+\^e]',r'', text)
        text=re.sub(r'([\.\+\/\-\*\^])\1',r'\1',text)
        text=re.sub(r'\*?\(\)','',text)
        return text



    def _config_buttons(self) -> None:
        """All button configs"""
        buttons_list = self.button_list
        for row in buttons_list:
            for button in row:
                button_text = button['text']

                if button_text == 'C':
                    button.bind('<Button-1>', self.clear_display)
                    button.config(bg='#00977f', fg='#fff')

                if button_text in '0123456789.+-/*()^':
                    button.bind('<Button-1>', self.add_text_to_display)
                    button.config(bg='#40E0D0', fg='#fff')

                if button_text == '=':
                    button.bind('<Button-1>', self.calculate)
                    button.config(bg='#007963', fg='#fff')
                for item in buttons_list:
                    button.config(fg='#000000')

    def calculate(self, event=None) -> None:
        fixed_text=self.fixed_text(self.display.get())
        equations=self.get_equations(fixed_text)
        try:
            if len(equations)==1:
                result=eval(self.fixed_text(equations[0]))
            else:
                result=eval(self.fixed_text(equations[0]))
                for equation in equations[1:]:
                    result=math.pow(result,eval(self.fixed_text(equation)))
            self.display.delete(0,'end')
            self.display.insert('end',result)
            self.label.config(text=f'{fixed_text}={result}')
        except OverflowError:
            self.label.config(text='Valor muito alto!, Calculo não Realizado!')
        except Exception:
            self.label.config(text='Conta inválida!')
        


    def get_equations(self,text):
        return re.split(r'\^',text,0)


    def add_text_to_display(self, event=None) -> None:
       self.display.insert('end',event.widget['text'])
    def clear_display(self, event=None) -> None:
        """Clear display"""
        self.display.delete(0, 'end')
