# app/plugins/subtract/__init__.py
import logging
from app.commands import Command

class SubtractCommand(Command):
    def execute(self, a: str, b: str = None):
        """Subtracts two numbers."""
        if b is None:
            print("Error: 'subtract' command requires exactly 2 arguments.")
            logging.error("Insufficient arguments: expected 2 but got 1.")
            return
        
        try:
            a = int(a)
            b = int(b)
        except ValueError:
            logging.error("Invalid input: Please provide valid numbers.")
            print("Invalid input: Please provide valid numbers.")
            return

        result = a - b
        logging.info(f"The result of {a} - {b} is {result}")
        print(f"The result of {a} - {b} is {result}")