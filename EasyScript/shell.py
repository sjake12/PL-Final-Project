from lexer import Lexer
from parse import Parser
from interpreter import Interpreter
from data import Data
from tokens import String

base = Data()

class Shell:
    def __init__(self):
        self.base = base

    def run(self):
        while True:
            text = input("EasyScript: ")

            tokenizer = Lexer(text)
            tokens = tokenizer.tokenize()

            parser = Parser(tokens)
            tree = parser.parse()

            if isinstance(tree, list) and tree[0].value == "say":
                # Handle say statement directly
                message = tree[1]
                if isinstance(message, String):
                    message = message.value.strip('"')
                    print(message)
                else:
                    print("Invalid say statement")
            else:
                # Interpret the rest of the code normally
                interpreter = Interpreter(tree, self.base)
                result = interpreter.interpret()

                if isinstance(result, str):  # Check if the result is a string
                    print(result)  # Print only the string message
                elif result is not None:
                    print(result)

if __name__ == "__main__":
    shell = Shell()
    shell.run()
