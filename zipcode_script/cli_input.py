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
            help='Used with topN and randomN function',
            dest='N',
            required=False
        )

        parser.add_argument(
            '-z', '--zipcode',
            type=str,
            help='Input the zipcode, used with matching and validation',
            required=False
        )
        

        self.parser = parser

    def get_args(self):
        return vars(self.parser.parse_args())

    def print_help(self):
        return self.parser.print_help()
