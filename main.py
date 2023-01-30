from tkinter import *
import operator

num_list = []

calculation_dict = {"first_num": "", "second_num": "", "operator": "", "result": None}


#calculate function rewritten with gpt's help see old function in the "old.py" file
def calculate():
    """Performs the calculation"""
    # dictionary containing the operator and its corresponding function
    operator_dict = {
        "+": operator.add,
        "-": operator.sub,
        "×": operator.mul,
        "÷": operator.truediv
    }
    # try to convert the first number to an int, if not possible convert to float
    try:
        first_num = int("".join(calculation_dict["first_num"]))
    except ValueError:
        first_num = float("".join(calculation_dict["first_num"]))
    # try to convert the second number to an int, if not possible convert to float
    try:
        second_num = int("".join(calculation_dict["second_num"]))
    except ValueError:
        second_num = float("".join(calculation_dict["second_num"]))
    # perform the calculation based on the operator and store the result in calculation_dict
    calculation_dict["result"] = operator_dict[calculation_dict["operator"]](first_num, second_num)



def add_character(character:str):
    """accepts a character as a string and displays it to the user and assigns it for calculation"""
    global num_list
    # check if character is a digit or '.'
    if character.isdigit() or character == ".":
        # append character to num_list
        num_list.append(character)
        # update the calc_area with the new number
        calc_area.config(text="".join(num_list))
    # check if character is an operator
    elif character in("÷", "×","-","+",):
        # if num_list is empty, return
        if len(num_list) == 0:
            return
        # if first_num in calculation_dict is empty, store the current number in first_num and operator
        elif len(calculation_dict["first_num"]) == 0:
            calculation_dict["first_num"] = "".join(num_list)
            calculation_dict["operator"] = character
        # if first_num is not empty, store the current number in second_num, perform calculation and update first_num and operator
        else:
            calculation_dict["second_num"] = "".join(num_list)
            calculate()
            calculation_dict["operator"] = character
            calculation_dict["first_num"] = str(calculation_dict["result"])
            calculation_dict["result"] = None
            calc_area.config(text=calculation_dict["first_num"])
        # empty the num_list
        num_list = []
    # check if character is '='
    elif character == "=":
        # if num_list is empty, return
        if len(num_list) == 0:
            return
        # store the current number in second_num, perform calculation and update calc_area with the result
        calculation_dict["second_num"] = "".join(num_list)
        calculate()
        num_list = ""
        calc_area.config(text=calculation_dict["result"])



def clear_input():
    global num_list
    num_list = []
    calc_area.config(text="0")




def clear_everything():
    global num_list
    num_list = []
    calc_area.config(text="0")
    calculation_dict["second_num"] = ""
    calculation_dict["first_num"] = ""

FONT_LG = ("Lato", 32, "bold")
FONT_MD = ("Lato", 24, "normal")
BTN_HEIGHT = 0
BTN_WIDTH = 1
TOP_ROWSPAN = 1

# calculation

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
    button.config(command=lambda x=text: add_character(x))
    button.grid(column=i % 4, row=TOP_ROWSPAN + 1 + i // 4, sticky=E + W + N + S)
    buttons[text] = button

buttons["+"].grid(rowspan=2)
buttons["="].grid(columnspan=2, row=TOP_ROWSPAN + 5, column=2)

buttons["C"].config(command=clear_input)
buttons["CE"].config(command=clear_everything)

window.mainloop()
