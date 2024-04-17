#Calculator Project

def sum(x, y ):
    """
    Adds two numbers and returns the result.

    Args:
        x (int): The first number.
        y (int): The second number.

    Returns:
        int: The result of adding y and x.
    """
    return x + y

def sub(x , y):
    """
    Subtracts two numbers and returns the result.

    Args:
        x (int): The first number.
        y (int): The second number.

    Returns:
        int: The result of subtracting y from x.
    """
    return x - y

def mul(x, y):
    """
    Multiplies two numbers and returns the result.

    Args:
        x (int or float): The first number.
        y (int or float): The second number.

    Returns:
        int or float: The result of multiplying x and y.
    """
    return x * y

def div(x , y):
    """
    Divides two numbers and returns the result.

    Args:
        x(int or float): The first number.
        y(int or float): The second number.

    Returns:
        int or float: The result of dividing x by y.
    """
    return x /y

def main():
    while True:
        print('-------------------------')
        print("Select an option:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")

        choice = input("Enter a choice (1/2/3/4): ")

        if choice in ('1', '2', '3', '4'):
            try:
                num1 = float(input("Enter the first number: "))
                num2 = float(input("Enter the second number: "))
            except:
                print("Invalid Input, try again")
                continue

            if choice == '1':
                print(num1, "+", num2, "=", sum(num1, num2))
            elif choice == '2':
                print(num1, "-", num2, "=", sub(num1, num2))
            elif choice == '3':
                print(num1, "*", num2, "=", mul(num1, num2))
            elif choice == '4':
                if num2 == 0:
                    print("Cannot divide by zero")
                    continue
                print(num1, "/", num2, "=", div(num1, num2))

            next_calculation = input("Let's do next calculation? (yes/no): ")
            if next_calculation == "no":
                break
        else:
            print("Invalid Input, try again")

# Call the main function
if __name__ == "__main__":
    main()

