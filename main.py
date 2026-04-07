import sys
from antlr4 import *
from grammer.alexer import alexer
def main():
    try:
        input_stream = FileStream('program.arabic', encoding='utf-8')
    except FileNotFoundError:
        print("Error: File 'program.arabic' not found.")
        sys.exit(1)
    lexer = alexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    token_stream.fill()
    print("=" * 50)
    print("")
