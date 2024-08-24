#100 Days of Python Day 10 

"""#learning about function outputs
def format_name(first_name, last_name):
    if first_name == "" or last_name == "":
        return "You didn't provide valid inputs"
    first_name = first_name.capitalize()
    last_name = last_name.capitalize()
    return f"{first_name} {last_name}"
print(format_name('ian', 'leBlanc'))
"""

#######################################
#Calculator 

#define functions with inputs n1 an n2 and make whole code recursive with calculator function.
def calculator():
    def add(n1, n2):
        return n1 + n2
    def subtract(n1,n2):
        return n1 - n2
    def multiply(n1,n2):
        return n1 * n2
    def divide(n1,n2):
        return n1 / n2

    #dictionary of operations with functions as values
    operations = {
        '+': add,
        '-': subtract,
        '*': multiply,
        '/': divide
        }

    n1 = float(input("What is the first number?\n"))

    #generate printed list of operations for user to pick from

    for index in operations:
        print(index)


    operation_symbol = input("What operation would you like to perform from the list above?\n")
    n2 = float(input("What is the second number?\n"))

    #call operations dictionary with operation symbol as an index input
    #then call function with first two numbers as input to be inputs in calculator function

    calculation = operations[operation_symbol]
    first_answer = calculator(n1,n2)
    print(f"{n1} {operation_symbol} {n2} = {first_answer}")


    # start of second operation while loop
    keep_going = input("Would you like to keep going? Y or N?\n").lower()
    while keep_going == "y":
        operation_symbol = input("Pick an operation\n")
        n3 = float(input("Pick another number\n"))
        calculation = operations[operation_symbol]
        second_answer = calculation(first_answer,n3)
        print(f"{first_answer} {operation_symbol} {n3} = {second_answer}")
        first_answer = second_answer
        keep_going = input("Would you like to keep going? Y or N?\n ").lower()
    if keep_going == "n":
        print("Reset")
        calculator()
calculator()