from app.commands import CommandHandler
from app.commands.add import AddCommand
from app.commands.exit import ExitCommand
from app.commands.menu import MenuCommand
from app.commands.subtract import SubtractCommand
from app.commands.multiply import MultiplyCommand  # Import MultiplyCommand
from app.commands.divide import DivideCommand  # Import DivideCommand

class App:
    def __init__(self):  # Constructor
        self.command_handler = CommandHandler()

    def start(self):
        # Register commands here
        self.command_handler.register_command("add", AddCommand())
        self.command_handler.register_command("subtract", SubtractCommand())
        self.command_handler.register_command("multiply", MultiplyCommand())  # Register multiply command
        self.command_handler.register_command("divide", DivideCommand())  # Register divide command
        self.command_handler.register_command("exit", ExitCommand())
        self.command_handler.register_command("menu", MenuCommand(self.command_handler))  # Register menu command

        print("Type 'menu' to see the list of available commands.")
        print("Usage: <command> <num1> <num2> | eg:- add 2 3")
        print("Type 'exit' to exit.")
        
        while True:  # REPL (Read, Evaluate, Print, Loop)
            command_input = input(">>> ").strip()
            if command_input.lower() == "exit":
                raise SystemExit("Exiting...")  # Raise SystemExit to exit
            self.command_handler.execute_command(command_input)