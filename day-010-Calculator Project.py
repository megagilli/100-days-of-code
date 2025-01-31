from art import logo

def add(n1, n2):
    return n1 + n2
#TODO: Write out the other 3 functions - subtract, multiply and divide.

def sub(n1,n2):
    return n1-n2

def multiply(n1,n2):
    return n1*n2

def divide(n1,n2):
    return n1/n2

#TODO: Add these 4 functions into a dictionary as the values. Keys = "+", "-", "*", "/"

operations={"+":add,
            "-":sub,
            "*":multiply,
            "/":divide}
#TODO: Use the dictionary operations to perform the calculations. Multiply 4 * 8 using the dictionary.

# print(operations["*"](4,8))
def calculator():
    print(logo)
    should_accumulate=True
    num1=float(input("what is the first number?: "))
    while should_accumulate:
        for symbol in operations:
            print(symbol)

        operation=input("pick an operation: ")
        num2=float(input("what is the second number?: "))
        answer=(operations[operation](num1,num2)) #function that is picked will be corresponding to the operation
        print(f"{num1} {operation} {num2} = {answer}")
        choice= input(f"Type 'y' to continue working with {answer}, Type 'n' to start new calculation: ").lower()
        if choice=="y":
            num1=answer
        else:
            should_accumulate=False
            print("\n"*20)
            calculator()


calculator()