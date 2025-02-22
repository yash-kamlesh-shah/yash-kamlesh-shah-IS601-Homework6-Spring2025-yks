from app.commands import Command

class SubtractCommand(Command):
    def execute(self, a: str, b: str):
        """Subtracts two numbers."""
        a = int(a)
        b = int(b)
        result = a - b
        print(f"The result of {a} - {b} is {result}")