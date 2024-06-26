# printx

printx is a Python package that provides a convenient print-like function for logging messages with various log levels, making it easy to integrate logging into your projects.

## Installation

You can install printx via pip:

```sql
pip install printx
```

## Usage

```python
from printx import printx_configure, printx

# Configure logging (optional: specify a custom log filename)
printx_configure()

# Use the printx function
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
```

## Configuration

The `printx_configure` function allows you to configure the logging settings. By default, it logs messages to a file named after the script that uses the `printx` function and to the console.

### To configure logging:

```python
from printx import printx_configure
```

### Configure logging with default settings

```python
printx_configure()
```

### Configure logging with a custom log filename

```python
printx_configure(log_filename='custom_log.log')
```

### Configure logging with a different log level

```python
printx_configure(level=logging.WARNING)
```

The `printx_configure` function accepts the following parameters:

- `log_filename` (str, optional): The name of the log file. If not provided, the default is the script's name with a `.log` extension.
- `level` (int, optional): The logging level. Default is `logging.DEBUG`.


## License

This project is licensed under the MIT License.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request.

## Author

[Javer Valino](https://github.com/phintegrator)

## Acknowledgments

- Thanks to the open-source community for providing the tools and inspiration for this project.
- Special thanks to all contributors and users of the package.