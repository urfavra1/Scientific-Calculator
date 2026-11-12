import math
import tkinter as tk


class ScientificCalculator:

  def __init__(self, root):
    self.root = root
    self.root.title("Scientific Calculator")
    self.root.geometry("400x550")
    self.root.resizable(False, False)
    self.root.configure(bg="#1e1e1e")

    self.expression = ""
    self.text_input = tk.StringVar()
    self.last_ans = 0.0

    # Display Screen Frame
    display_frame = tk.Frame(self.root, bg="#1e1e1e", bd=10)
    display_frame.pack(side=tk.TOP, fill=tk.BOTH)

    self.text_display = tk.Entry(
        display_frame,
        font=("Arial", 26, "bold"),
        textvariable=self.text_input,
        bd=5,
        bg="#2d2d2d",
        fg="#ffffff",
        justify="right",
        insertbackground="white",
    )
    self.text_display.pack(expand=True, fill=tk.BOTH)

    # Buttons Grid Frame
    btn_frame = tk.Frame(self.root, bg="#1e1e1e")
    btn_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True, padx=5, pady=5)

    # Button layout definition: (Text, row, col, background color)
    buttons = [
        ("C", 0, 0, "#d9534f"),
        ("(", 0, 1, "#333333"),
        (")", 0, 2, "#333333"),
        ("⌫", 0, 3, "#f0ad4e"),
        ("/", 0, 4, "#f0ad4e"),
        ("sin", 1, 0, "#252526"),
        ("7", 1, 1, "#3c3c3c"),
        ("8", 1, 2, "#3c3c3c"),
        ("9", 1, 3, "#3c3c3c"),
        ("*", 1, 4, "#f0ad4e"),
        ("cos", 2, 0, "#252526"),
        ("4", 2, 1, "#3c3c3c"),
        ("5", 2, 2, "#3c3c3c"),
        ("6", 2, 3, "#3c3c3c"),
        ("-", 2, 4, "#f0ad4e"),
        ("tan", 3, 0, "#252526"),
        ("1", 3, 1, "#3c3c3c"),
        ("2", 3, 2, "#3c3c3c"),
        ("3", 3, 3, "#3c3c3c"),
        ("+", 3, 4, "#f0ad4e"),
        ("sqrt", 4, 0, "#252526"),
        ("0", 4, 1, "#3c3c3c"),
        (".", 4, 2, "#3c3c3c"),
        ("pi", 4, 3, "#252526"),
        ("=", 4, 4, "#5cb85c"),
        ("log", 5, 0, "#252526"),
        ("ln", 5, 1, "#252526"),
        ("^", 5, 2, "#252526"),
        ("e", 5, 3, "#252526"),
        ("ans", 5, 4, "#252526"),
    ]

    for text, row, col, color in buttons:
      cmd = lambda x=text: self.on_button_click(x)
      btn = tk.Button(
          btn_frame,
          text=text,
          font=("Arial", 14, "bold"),
          bg=color,
          fg="#ffffff",
          activebackground="#555555",
          activeforeground="#ffffff",
          bd=0,
          relief=tk.FLAT,
          command=cmd,
      )
      btn.grid(row=row, column=col, sticky="nsew", padx=3, pady=3)

    # Configure grid weights for responsive resizing
    for i in range(6):
      btn_frame.rowconfigure(i, weight=1)
    for i in range(5):
      btn_frame.columnconfigure(i, weight=1)

  def on_button_click(self, char):
    if char == "C":
      self.expression = ""
      self.text_input.set("")
    elif char == "⌫":
      self.expression = self.expression[:-1]
      self.text_input.set(self.expression)
    elif char == "=":
      try:
        # Prepare expression for safe evaluation
        expr = self.expression
        expr = expr.replace("^", "**")

        # Safe evaluation context with trigonometric conversions (Degrees)
        safe_dict = {
            "__builtins__": None,
            "math": math,
            "sin": lambda x: math.sin(math.radians(x)),
            "cos": lambda x: math.cos(math.radians(x)),
            "tan": lambda x: math.tan(math.radians(x)),
            "sqrt": math.sqrt,
            "log": math.log10,
            "ln": math.log,
            "pi": math.pi,
            "e": math.e,
            "ans": self.last_ans,
        }

        result = eval(expr, safe_dict)
        self.last_ans = result
        self.text_input.set(str(result))
        self.expression = str(result)
      except Exception:
        self.text_input.set("Error")
        self.expression = ""
    else:
      # Append functions with opening parenthesis automatically
      if char in ["sin", "cos", "tan", "sqrt", "log", "ln"]:
        self.expression += char + "("
      else:
        self.expression += str(char)
      self.text_input.set(self.expression)


if __name__ == "__main__":
  root = tk.Tk()
  app = ScientificCalculator(root)
  root.mainloop()