print("Hello, World!")

# Simple Math Operations
def add(a, b):
    """Addition operation"""
    return a + b

def subtract(a, b):
    """Subtraction operation"""
    return a - b

def multiply(a, b):
    """Multiplication operation"""
    return a * b

def divide(a, b):
    """Division operation"""
    if b == 0:
        return "Error: Division by zero!"
    return a / b

def power(a, b):
    """Power operation"""
    return a ** b

def main():
    print("\n=== Simple Math Calculator ===")
    
    # Test operations
    num1, num2 = 10, 5
    
    print(f"\nNumbers: {num1} and {num2}")
    print(f"Addition: {num1} + {num2} = {add(num1, num2)}")
    print(f"Subtraction: {num1} - {num2} = {subtract(num1, num2)}")
    print(f"Multiplication: {num1} × {num2} = {multiply(num1, num2)}")
    print(f"Division: {num1} ÷ {num2} = {divide(num1, num2)}")
    print(f"Power: {num1} ^ {num2} = {power(num1, num2)}")
    
    # Additional examples
    print(f"\nSquare of 7: {power(7, 2)}")
    print(f"Cube of 3: {power(3, 3)}")
    print(f"Division by zero test: {divide(10, 0)}")

if __name__ == "__main__":
    main()
