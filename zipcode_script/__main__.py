from .cli_input import Input
from .zipcode import Zipcode
import sys

def main():
    inp = Input()
    options = inp.get_args()

    zip = Zipcode()

    # functionCalled = eval(options['function'])
    
    # print(functionCalled)
    # functionCalled()
    print(options['function'])
    print(type(options['function']))
    op = 'zip.' + options['function'] + '()'
    print(eval(op))




if __name__ == '__main__':
    main()