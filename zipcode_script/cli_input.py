import argparse


class Input():
    """Class to keep all the arguments for the CLI"""
    def __init__(self):
        parser = argparse.ArgumentParser(
            description="Query India zipcode"
        )
    
        parser.add_argument(
            'function',
            type=str,
            help='Function to execute',
        )

        parser.add_argument(
            '-n',
            type=str,
            help='Used with listTopN and listRandomN function',
            required=False,
            default='834001',
        )

        parser.add_argument(
            '--zipcode','-z',
            type=str,
            help='Input the zipcode, used with matching and validate',
            required=False,
            default='3',
            dest='zipcode'
        )
        

        self.parser = parser

    def get_args(self):
        return vars(self.parser.parse_args())

    def print_help(self):
        return self.parser.print_help()
