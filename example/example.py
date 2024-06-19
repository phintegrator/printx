from printx import  printx_configure,printx

# Configure logging (optional: specify a custom log filename)
printx_configure()

# Use the printx function with different log levels
printx("This is a default info message")
printx("This is a debug message", log_level='debug')
printx("This is an info message", log_level='info')
printx("This is a warning message", log_level='warning')
printx("This is an error message", log_level='error')
printx("This is a critical message", log_level='critical')

def example_function():
    try:
        printx("Starting the function")
        printx("Performing an action")
        error_condition = True  # Simulate an error condition
        if error_condition:
            raise ValueError("An error occurred")
        printx("Function finished")
    except Exception as e:
        printx(f"Exception occurred: {e}", log_level='error')

example_function()
