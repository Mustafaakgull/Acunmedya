import math

# /*toplama metodu*/
def add(a: float, b: float) -> float:
    return math.fsum([a, b])

# /*çıkarma metodu*/
def subtraction(a: float, b: float) -> float:
    return a - b

# /*çarpma metodu*/
def multiply(a: float, b: float) -> float:
    return math.prod([a, b])

# /*bölme metodu*/
def division(a: float, b: float) -> float:
    if b == 0:
        raise ValueError("Division by zero is not allowed!")
    return a / b

# /*girilen değeri kontrol et metodu*/
def validate_number(value):
    try:
        return float(value)
    except ValueError:
        raise ValueError(f"Invalid input: {value} is not a number.")


# /*çalıştırma metodu*/
def perform_operation():
    try:
        input1 = input("Enter the first number: ")
        num1 = validate_number(input1)

        input2 = input("Enter the second number: ")
        num2 = validate_number(input2)

        print("Choose an operation: add, subtract, multiply, divide")
        operation = input("Enter your choice: ").strip().lower()

        if operation == "add":
            print("Result:", add(num1, num2))
        elif operation == "subtract":
            print("Result:", subtraction(num1, num2))
        elif operation == "multiply":
            print("Result:", multiply(num1, num2))
        elif operation == "divide":
            try:
                print("Result:", division(num1, num2))
            except ValueError as e:
                print(e)
        else:
            print("Invalid operation selected!")
    except ValueError as e:
        print(e)


if __name__ == "__main__":
    perform_operation()