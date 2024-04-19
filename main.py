from expression_parser import ExpressionParser
import sys

if __name__=='__main__':
    input_string = sys.argv[1]
    e = ExpressionParser(input_string)
    e.print_values()


    










