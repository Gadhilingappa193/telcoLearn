# Step 1: Create a new file
import logging

# Step 3: Configure logging settings
logging.basicConfig(
    filename="decorator_logs.log",
    level=logging.INFO,
    format="%(asctime)s - %(message)s"
)

# Step 4: Create a decorator
def auto_log(func):
    def wrapper(*args, **kwargs):
        logging.info(f"Function '{func.__name__}' called with args={args} kwargs={kwargs}")
        result = func(*args, **kwargs)  # run the function
        logging.info(f"Function '{func.__name__}' returned {result}")
        return result
    return wrapper


# Step 2: Create a sample function (Calculator example)
@auto_log   # Step 5: Apply decorator
def add(a, b):
    return a + b

@auto_log
def multiply(a, b):
    return a * b


# Step 6: Test functions
print(add(5, 3))
print(multiply(4, 2))

print("\nCheck 'decorator_logs.log' file for logs.")
