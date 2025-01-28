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