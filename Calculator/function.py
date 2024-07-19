import tkinter as tk
def make_root() -> tk.Tk:
   root= tk.Tk()
   root.title('Calculator')
   root.config(padx=10,pady=10,border=10, background='#68E5EA')  #(Pady) configurar borda das laterais
   root.resizable(False, False)## Sem redimencionada!
   return root

def make_label(root) -> tk.Label:
   label= tk.Label(
      root, text='Sem Nunhum Calculo!',
      anchor='e', justify='right',background='#000000'               #anchor'E'  e  #justifyt=== alinhamento a direita 
   )
   label.grid(row=0, column=0, columnspan=5,sticky='news')
   return label


def make_display(root) -> tk.Entry:
    display = tk.Entry(root)
    display.grid(row=1, column=0, columnspan=5, sticky='news', pady=(0, 10))  # distancia dos botoes
    display.config(
        font=('Helvetica', 40, 'bold'),
        justify='right',
        bd=1,
        relief='flat',
        highlightthickness=1,
        highlightcolor='#cccccc'  # Valid hex color code
    )