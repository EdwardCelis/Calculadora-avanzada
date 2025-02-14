def get_numbers():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    return num1, num2

def main():
    num1, num2 = get_numbers()
    print("The sum is:", int(num1 + num2))

    while True:
        print("\nExtra Features:")
        print("1. Subtraction")
        print("2. Multiplication")
        print("3. Division")
        print("4. Modulus")
        print("5. Add three numbers")
        print("6. Custom operation with 3 or more numbers")
        print("7. Exit")
        
        choice = input("Choose an option: ")

        if choice in ["1", "2", "3", "4"]:
            change_numbers = input("Do you want to enter new numbers? (yes/no): ").strip().lower()
            if change_numbers == "yes":
                num1, num2 = get_numbers()

        if choice == "1":
            print("The result is:", int(num1 - num2))
        elif choice == "2":
            print("The result is:", int(num1 * num2))
        elif choice == "3":
            if num2 != 0:
                print("The result is:", int(num1 / num2))
            else:
                print("Error: Division by zero is not allowed.")
        elif choice == "4":
            if num2 != 0:
                print("The result is:", int(num1 % num2))
            else:
                print("Error: Modulus by zero is not allowed.")
        elif choice == "5":
            num3 = float(input("Enter the third number: "))
            print("The sum is:", int(num1 + num2 + num3))
        elif choice == "6":
            expression = input("Enter a mathematical expression (e.g., 2+4-3*5): ")
            try:
                result = eval(expression)
                print("The result is:", int(result))
            except:
                print("Invalid expression.")
        elif choice == "7":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
