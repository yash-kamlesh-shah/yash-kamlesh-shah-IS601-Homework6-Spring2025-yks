"""Tests for commands."""

# import pytest
from app.plugins.add import AddCommand  # Import AddCommand
from app.plugins.multiply import MultiplyCommand  # Import MultiplyCommand
from app.plugins.divide import DivideCommand  # Import DivideCommand
from app.plugins.subtract import SubtractCommand  # Import SubtractCommand

def test_add_command(capfd):
    """Test the add command to ensure it correctly adds two numbers."""
    command = AddCommand()
    command.execute('2', '3')  # Directly pass the arguments to execute
    out, _ = capfd.readouterr()  # Capture the output
    assert out == "The result of 2 + 3 is 5\n", "AddCommand should output the correct result."

def test_add_command_invalid_input(capfd):
    """Test the add command with invalid input."""
    command = AddCommand()
    command.execute('two', 'three')  # Passing non-numeric values
    out, _ = capfd.readouterr()  # Capture the output
    assert out == "Invalid input: Please provide valid numbers.\n", "AddCommand should handle invalid input."

def test_add_command_insufficient_arguments(capfd):
    """Test the add command with insufficient arguments."""
    command = AddCommand()
    command.execute('2')  # Only one argument
    out, _ = capfd.readouterr()  # Capture the output
    assert out == "Error: 'add' command requires exactly 2 arguments.\n", "AddCommand should notify about insufficient arguments."

def test_add_command_too_many_arguments(capfd):
    """Test the add command with too many arguments."""
    command = AddCommand()
    command.execute('1', '2', '3')  # Three arguments
    out, _ = capfd.readouterr()  # Capture the output
    assert out == "Error: 'add' command requires exactly 2 arguments.\n", "AddCommand should notify about too many arguments."

def test_subtract_command(capfd):
    """Test the subtract command to ensure it correctly subtracts two numbers."""
    command = SubtractCommand()
    command.execute('5', '3')  # Directly pass the arguments to execute
    out, _ = capfd.readouterr()  # Capture the output
    assert out == "The result of 5 - 3 is 2\n", "SubtractCommand should output the correct result."

def test_subtract_command_invalid_input(capfd):
    """Test the subtract command with invalid input."""
    command = SubtractCommand()
    command.execute('five', 'three')  # Passing non-numeric values
    out, _ = capfd.readouterr()  # Capture the output
    assert out == "Invalid input: Please provide valid numbers.\n", "SubtractCommand should handle invalid input."

def test_subtract_command_insufficient_arguments(capfd):
    """Test the subtract command with insufficient arguments."""
    command = SubtractCommand()
    command.execute('5')  # Only one argument
    out, _ = capfd.readouterr()  # Capture the output
    assert out == "Error: 'subtract' command requires exactly 2 arguments.\n", "SubtractCommand should notify about insufficient arguments."

def test_multiply_command(capfd):
    """Test the multiply command to ensure it correctly multiplies two numbers."""
    command = MultiplyCommand()
    command.execute('2', '3')  # Directly pass the arguments to execute
    out, _ = capfd.readouterr()  # Capture the output
    assert out == "The result of 2 * 3 is 6\n", "MultiplyCommand should output the correct result."

def test_multiply_command_invalid_input(capfd):
    """Test the multiply command with invalid input."""
    command = MultiplyCommand()
    command.execute('two', 'three')  # Passing non-numeric values
    out, _ = capfd.readouterr()  # Capture the output
    assert out == "Invalid input: Please provide valid numbers.\n", "MultiplyCommand should handle invalid input."

def test_multiply_command_insufficient_arguments(capfd):
    """Test the multiply command with insufficient arguments."""
    command = MultiplyCommand()
    command.execute('2')  # Only one argument
    out, _ = capfd.readouterr()  # Capture the output
    assert out == "Error: 'multiply' command requires exactly 2 arguments.\n", "MultiplyCommand should notify about insufficient arguments."

def test_multiply_command_too_many_arguments(capfd):
    """Test the multiply command with too many arguments."""
    command = MultiplyCommand()
    command.execute('2', '3', '4')  # Passing three arguments
    out, _ = capfd.readouterr()  # Capture the output
    assert out == "Error: 'multiply' command requires exactly 2 arguments.\n", "MultiplyCommand should notify about too many arguments."

def test_divide_command(capfd):
    """Test the divide command to ensure it correctly divides two numbers."""
    command = DivideCommand()
    command.execute('6', '3')  # Directly pass the arguments to execute
    out, _ = capfd.readouterr()  # Capture the output
    assert out == "The result of 6 / 3 is 2.0\n", "DivideCommand should output the correct result."

def test_divide_command_invalid_input(capfd):
    """Test the divide command with invalid input."""
    command = DivideCommand()
    command.execute('six', 'three')  # Passing non-numeric values
    out, _ = capfd.readouterr()  # Capture the output
    assert out == "Invalid input: Please provide valid numbers.\n", "DivideCommand should handle invalid input."

def test_divide_by_zero(capfd):
    """Test the divide command to ensure it handles division by zero."""
    command = DivideCommand()
    command.execute('6', '0')  # Directly pass the arguments to execute
    out, _ = capfd.readouterr()  # Capture the output
    assert out == "Error: Division by zero.\n", "DivideCommand should output an error for division by zero."