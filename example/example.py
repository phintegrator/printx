import logging

from printx import printx_configure, printx


def demonstrate_levels():
    printx("This is a default info message")
    printx("This is a debug message", log_level='debug')
    printx("This is an info message", log_level='info')
    printx("This is a warning message", log_level='warning')
    printx("This is an error message", log_level='error')
    printx("This is a critical message", log_level='critical')


def demonstrate_custom_configuration():
    reset_logging()
    printx_configure(log_filename="custom-example.log", level=logging.WARNING)
    printx("Now logging only warnings and above", log_level='warning')
    printx("This debug message is suppressed", log_level='debug')
    printx("This info message is suppressed", log_level='info')
    printx("This error still shows up", log_level='error')


def example_function():
    try:
        printx("Starting the function")
        printx("Performing an action")
        error_condition = True  # Simulate an error condition
        if error_condition:
            raise ValueError("An error occurred")
        printx("Function finished")
    except Exception as exc:
        printx(f"Exception occurred: {exc}", log_level='error')


def reset_logging():
    for handler in logging.root.handlers[:]:
        logging.root.removeHandler(handler)
    logging.root.setLevel(logging.NOTSET)


def main():
    # Without an explicit filename this will log to example.log (auto-derived from this script)
    printx_configure()
    demonstrate_levels()
    example_function()

    # Demonstrate providing a custom log filename and level threshold
    demonstrate_custom_configuration()


if __name__ == "__main__":
    main()
