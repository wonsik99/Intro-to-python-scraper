operation = ' '

while operation != "exit":
    first_num = int(input("Choose a number:\n"))
    second_num = int(input("Choose another one:\n"))

    operation = input(
    "Choose an operation:\n"
    "   Options are: + , - , * or /.\n"
    "   Write 'exit' to finish.\n"
    )

    if operation == "+":
        print("Result:", first_num + second_num)
    elif operation == "-":
        print("Result:", first_num - second_num)
    elif operation == "*":
        print("Result:", first_num * second_num)
    elif operation == "/":
        print("Result:", first_num / second_num)
    else:
        print("Invalid operation. Try again")

