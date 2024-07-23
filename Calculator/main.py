from function import make_root, make_display, make_label, make_buttons
from calculadora import CalculatorGui

def main():
    root = make_root()
    display = make_display(root, row=1, column=0, columnspan=5, sticky='news')
    display.grid_configure(pady=(0, 10))
    label = make_label(root, row=0, column=0, columnspan=5, sticky='news')
    buttons = make_buttons(root, starting_row=2)

    def do_calculate(expression: str) -> str:
        try:
            return str(eval(expression))  # Simplistic calculation logic for demo purposes
        except Exception:
            return "Error"

    calculator_gui = CalculatorGui(root, label, display, buttons, do_calculate)
    calculator_gui.start()

if __name__ == '__main__':
    main()
