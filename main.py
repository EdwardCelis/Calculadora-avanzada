def main():

    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    print("The sum is:", num1 + num2)

    print("\nExtra Features:")
    print("1. Subtraction")
    print("2. Multiplication")
    print("3. Division")
    print("4. Modulus")
    print("5. Add three numbers")
    print("6. Custom operation with 3 or more numbers")
    
    choice = input("Choose an option (or press Enter to exit): ")
    
    if choice == "1":
        print("The result is:", num1 - num2)
    elif choice == "2":
        print("The result is:", num1 * num2)
    elif choice == "3":
        if num2 != 0:
            print("The result is:", num1 / num2)
        else:
            print("Error: Division by zero is not allowed.")
    elif choice == "4":
        if num2 != 0:
            print("The result is:", num1 % num2)
        else:
            print("Error: Modulus by zero is not allowed.")
    elif choice == "5":
        num3 = float(input("Enter the third number: "))
        print("The sum is:", num1 + num2 + num3)
    elif choice == "6":
        expression = input("Enter a mathematical expression (e.g., 2+4-3*5): ")
        try:
            result = eval(expression)
            print("The result is:", result)
        except:
            print("Invalid expression.")
    else:
        print("Exiting...")

if __name__ == "__main__":
    main()
