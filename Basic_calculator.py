def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Division by zero is not allowed."

def calculator():
    while True:
        print("\nBasic Calculator")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        
        choice = input("Select an operation (1-5): ")

        if choice in ["1", "2", "3", "4"]:
            try:
                num1 = float(input("Enter the first number: "))
                num2 = float(input("Enter the second number: "))

                if choice == "1":
                    print(f"Result: {add(num1, num2)}")
                elif choice == "2":
                    print(f"Result: {subtract(num1, num2)}")
                elif choice == "3":
                    print(f"Result: {multiply(num1, num2)}")
                elif choice == "4":
                    print(f"Result: {divide(num1, num2)}")
            except ValueError:
                print("Invalid input! Please enter numeric values.")
        else:
            print("Invalid choice. Please select a valid operation.")

if __name__ == "__main__":
    calculator()


Output:
Basic Calculator
1. Addition
2. Subtraction
3. Multiplication
4. Division
Select an operation (1-5): 1
Enter the first number: 45
Enter the second number: 15
Result: 60.0

Basic Calculator
1. Addition
2. Subtraction
3. Multiplication
4. Division
Select an operation (1-5): 2
Enter the first number: 100
Enter the second number: 55
Result: 45.0

Basic Calculator
1. Addition
2. Subtraction
3. Multiplication
4. Division
Select an operation (1-5): 3
Enter the first number: 400
Enter the second number: 3
Result: 1200.0

Basic Calculator
1. Addition
2. Subtraction
3. Multiplication
4. Division
Select an operation (1-5): 4
Enter the first number: 400
Enter the second number: 20
Result: 20.0

