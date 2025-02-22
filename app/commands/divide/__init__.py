from app.commands import Command

class DivideCommand(Command):
    def execute(self, a: str, b: str):
        """Divides two numbers."""
        a = int(a)
        b = int(b)
        if b == 0:
            print("Error: Division by zero.")
            return
        result = a / b
        print(f"The result of {a} / {b} is {result}")