from tkinter import *
from math import sqrt


class Main(Frame):
    def __init__(self, calc):
        super(Main, self).__init__(calc)
        self.build()

    def build(self):
        self.formula = "0"
        self.lbl = Label(text=self.formula, font=("Times New Roman", 21, "bold"), bg="black", fg="white")
        self.lbl.place(x=46, y=50)

        btns = [
            "C", "DEL", "%", "/",
            "7", "8", "9", "x",
            "4", "5", "6", "-",
            "1", "2", "3", "+",
            "X^2", "0", "sqrt", "="
        ]

        x = 2
        y = 140
        for bt in btns:
            com = lambda x=bt: self.logicalc(x)
            try:
                if int(bt):
                    col = "white"
            except ValueError:
                    col = "orange"
            Button(text=bt, bg="black", fg=col, borderwidth=0,
                   font=("Roboto", 15), command=com).place(x=x, y=y, width=100, height=79)
            x += 107
            if x > 400:
                x = 2
                y += 81

    def logicalc(self, operation):
        if operation == "C":
            self.formula = ""
        elif operation == "DEL":
            self.formula = self.formula[0:-1]
        elif operation == "%":
            self.formula = str(eval(self.formula)*0.01)
        elif operation == "X^2":
            self.formula = str((eval(self.formula))**2)
        elif operation == "sqrt":
            self.formula = str(sqrt(eval(self.formula)))
        elif operation == "=":
            self.formula = str(eval(self.formula))
        else:
            if self.formula == "0":
                self.formula = ""
            if operation == "x":
                self.formula += "*"
            else:
                self.formula += operation
        self.update()

    def update(self):
        if self.formula == "":
            self.formula = "0"
        self.lbl.configure(text=self.formula)


if __name__ == '__main__':
    calc = Tk()
    calc["bg"] = "black"
    calc.geometry("425x550")
    calc.title("Калькулятор")
    calc.resizable(False, False)
    app = Main(calc)
    app.pack()
    calc.mainloop()