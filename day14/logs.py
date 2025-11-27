# Step 1: New Python file
import logging

# Step 3: Configure logging settings
logging.basicConfig(
    filename="calculator.log",level=logging.INFO,format="%(asctime)s - %(levelname)s - %(message)s"
)


# Step 2: Calculator function (API simulation)
def calculator(a, b, operation):
    logging.info(f"Calculator called with a={a}, b={b}, operation={operation}")

    try:
        if operation == "add":
            result = a + b
        elif operation == "subtract":
            result = a - b
        elif operation == "multiply":
            result = a * b
        elif operation == "divide":
            if b == 0:
                raise ZeroDivisionError("Cannot divide by zero")
            result = a / b
        else:
            raise ValueError("Invalid operation selected")

        logging.info(f"Operation successful: Result = {result}")
        return result

    except ZeroDivisionError as e:
        logging.error(f"Error occurred: {e}")
        return f"Error: {e}"

    except Exception as e:
        logging.error(f"Unexpected Error: {e}")
        return f"Error: {e}"


# Step 5: Test calculations
print(calculator(5, 3, "add"))
print(calculator(15, 5, "divide"))
print(calculator(10, 0, "divide"))      # zero division test
print(calculator(12, 4, "multiply"))
print(calculator(7, 2, "unknown"))      # invalid operation
