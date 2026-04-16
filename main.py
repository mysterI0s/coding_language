import sys
from antlr4 import *
from grammar.alexerParser import alexerParser
from grammar.alexerLexer import alexerLexer
from custom_visitor import CustomASTVisitor

def main():  
    try:
        input_stream = FileStream('program.arabic', encoding='utf-8')
    except FileNotFoundError:
        print(" لم يتم العثور على الملف : خطأ program.arabic")
        sys.exit(1)
    lexer = alexerLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = alexerParser(token_stream)
    parse_tree = parser.program()
    visitor = CustomASTVisitor()
    ast = visitor.visit(parse_tree)
    print("="*50)
    print("شجرة القواعد المجردة (AST) الناتجة:")
    print("="*50)
    import pprint
    print(pprint.pformat(ast))
if __name__ == '__main__':
    main()