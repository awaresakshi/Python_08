#step 1.fine your custom exception class
class MyCustomError(Exception):
    """A basic custom exception."""
    pass

# Step 2: Use the custom exception in your code
def check_positive(number):
    if number < 0:
        raise MyCustomError("Number must be positive!")
    return number

# Step 3: Handle the custom exception
try:
    check_positive(-5)
except MyCustomError as e:
    print("Caught a custom error:", e)