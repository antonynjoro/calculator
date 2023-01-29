from tkinter import *

def add_number(numeral:str):
    calc_area.config(text=numeral)

FONT_LG = ("Lato", 32, "bold")
FONT_MD = ("Lato", 24, "normal")
BTN_HEIGHT = 0
BTN_WIDTH = 1
TOP_ROWSPAN = 1

# Colors
LIGHT_BG = "#2C3647"
DARK_BG = "#293241"
ORANGE = "#EE6C4D"
LIGHT_ORANGE = "#EAE2B7"
LIGHT_BLUE = "#E0FBFC"

window = Tk()
window.minsize(height=500, width=300)
window.title("Calculator")
window.config(padx=18, pady=18, bg=DARK_BG)
for i in range(4):
    window.columnconfigure(i, weight=1)

for i in range(7):
    window.rowconfigure(i, weight=1)

calc_area = Label(text="0", font=(FONT_LG), anchor="se")
calc_area.config(justify="right", bg=LIGHT_BG, fg=LIGHT_ORANGE, pady=10, padx=10)
calc_area.grid(column=0, row=0, rowspan=TOP_ROWSPAN + 1, columnspan=4, sticky=E + W + N + S, pady=10)

# Define a list of button text values
button_text = ["C", "CE", "÷", "×", "1", "2", "3", "-", "4", "5", "6", "+", "7", "8", "9", "=", "0", ".", ]

buttons = {}
# Use a loop to create the buttons (Created with Chat GPT)
for i, text in enumerate(button_text):
    button = Button(text=text)
    button.config(height=BTN_HEIGHT, width=BTN_WIDTH, font=(FONT_MD), bg=ORANGE)
    button.config(command=lambda x=text: add_number(x))
    button.grid(column=i % 4, row=TOP_ROWSPAN + 1 + i // 4, sticky=E + W + N + S)
    buttons[text] = button

buttons["+"].grid(rowspan=2)
buttons["="].grid(columnspan=2, row=TOP_ROWSPAN + 5, column=2)

window.mainloop()
