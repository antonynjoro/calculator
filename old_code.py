# My original calculate function
def calculate():
    global calculation_dict

    first_num = int("".join(calculation_dict["first_num"]))
    second_num = int("".join(calculation_dict["second_num"]))

    if calculation_dict["operator"] == "-":
        calculation_dict["result"] = str(first_num - second_num)
        print(calculation_dict)
    elif calculation_dict["operator"] == "+":
        calculation_dict["result"] = str(first_num + second_num)
        print(calculation_dict)
    elif calculation_dict["operator"] == "×":
            calculation_dict["result"] = str(first_num * second_num)
            print(calculation_dict)
    elif calculation_dict["operator"] == "÷":
            calculation_dict["result"] = str(first_num / second_num)
            print(calculation_dict)