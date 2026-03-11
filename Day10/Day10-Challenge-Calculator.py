import calculatorart
print(calculatorart.calc)

# operator functions
def addition(n1, n2):
    """Add n1 and n2"""
    return n1 + n2
def subtraction(n1, n2):
    """Subtract n1 by n2"""
    return n1 - n2
def multiplication(n1, n2):
    """Multiply n1 by n2"""
    return n1 * n2
def division(n1, n2):
    """Divide n1 by n2"""
    return n1 / n2
def exponent(n1, n2):
    """Square n1 by n2"""
    return n1**n2

# Dictionary to store and access operators, with keys referencing operator functions
operations = {
    "+": addition,
    "-": subtraction,
    "*": multiplication,
    "/": division,
    "^": exponent
}

n1 = int(input("Enter number: "))

# Allow user to continue performing calculations on a result
while True:
    print("ENTER\n'+' for addition\n"
        "'-' for subtraction\n"
        "'*' for multiplication\n"
        "'/' for division\n"
        "'^' for exponents\n")
    operator = input("Choose an operator: ")
    n2 = int(input("Enter a second number: "))

    # logic to calculate answer
    operation = operations[operator]
    answer = operation(n1, n2)

    print(answer)

    choice = input("Would you like to use the answer? ")
    if choice == "yes":
        n1 = answer
        continue
    else:
        break