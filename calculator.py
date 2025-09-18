
import tkinter as tk

class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("電卓")
        self.geometry("400x500")
        self.resizable(False, False)

        self.expression = ""
        self.display_var = tk.StringVar()

        self._create_widgets()

    def _create_widgets(self):
        # Display Screen
        display_frame = tk.Frame(self)
        display_frame.pack(expand=True, fill="both")
        
        display_screen = tk.Entry(
            display_frame,
            textvariable=self.display_var,
            font=("Arial", 24),
            bg="#eee",
            bd=0,
            justify="right",
            state="readonly"
        )
        display_screen.pack(expand=True, fill="both", ipady=10, padx=10, pady=10)

        # Buttons Frame
        buttons_frame = tk.Frame(self)
        buttons_frame.pack(expand=True, fill="both")

        buttons = [
            ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
            ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
            ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
            ("0", 4, 0), (".", 4, 1), ("C", 4, 2), ("+", 4, 3),
            ("=", 5, 0, 4)
        ]

        for (text, row, col, *span) in buttons:
            if text == "=":
                btn = tk.Button(
                    buttons_frame,
                    text=text,
                    font=("Arial", 18),
                    command=self._on_equal,
                    bg="#4CAF50",
                    fg="white"
                )
                btn.grid(row=row, column=col, columnspan=span[0], sticky="nsew", padx=5, pady=5)
            elif text == "C":
                btn = tk.Button(
                    buttons_frame,
                    text=text,
                    font=("Arial", 18),
                    command=self._on_clear,
                    bg="#f44336",
                    fg="white"
                )
                btn.grid(row=row, column=col, sticky="nsew", padx=5, pady=5)
            else:
                btn = tk.Button(
                    buttons_frame,
                    text=text,
                    font=("Arial", 18),
                    command=lambda t=text: self._on_button_click(t)
                )
                btn.grid(row=row, column=col, sticky="nsew", padx=5, pady=5)

        for i in range(5):
            buttons_frame.grid_rowconfigure(i, weight=1)
        for i in range(4):
            buttons_frame.grid_columnconfigure(i, weight=1)
        buttons_frame.grid_rowconfigure(5, weight=1)


    def _on_button_click(self, char):
        self.expression += str(char)
        self.display_var.set(self.expression)

    def _on_clear(self):
        self.expression = ""
        self.display_var.set("")

    def _on_equal(self):
        try:
            # A simple way to evaluate, but be cautious with eval in real-world apps
            # For this controlled calculator, it's acceptable.
            result = str(eval(self.expression))
            self.display_var.set(result)
            self.expression = result
        except (SyntaxError, ZeroDivisionError, NameError):
            self.display_var.set("Error")
            self.expression = ""

if __name__ == "__main__":
    app = Calculator()
    app.mainloop()
