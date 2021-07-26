from .cli_input import Input
from .zipcode import Zipcode
import sys

def main():
    inp = Input()
    options = inp.get_args()
    
    function = options['function']
    n = options['n']
    zipcode = options['zipcode']

    zip = Zipcode()
    functionCall = 'print(zip)'

    if function == 'listAll' or function == 'random':
        functionCall = f'zip.{function}()'
    if function == 'matching' or function == 'validate':
        functionCall = f'zip.{function}("{zipcode}")'
    if function == 'listRandomN' or function == 'listTopN':
        functionCall = f'zip.{function}({n})'

    print(functionCall)
    return str(eval(functionCall))


if __name__ == '__main__':
    main()