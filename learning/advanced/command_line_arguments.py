#!/usr/bin/env python3
import argparse

def get_args():
    '''
    Gets the arguments from the command line. If executed with command like:
    `python3 command_line_arguments.py -h`
    The program will print out the description, how to get help and the
    example usage we have defined.
    '''
    parser = argparse.ArgumentParser(
        description="A simple argument parser",
        epilog="python3 command_line_arguments.py -x YES -y oh_right",
    )
    parser.add_argument(
        #defining metavar here takes out the extra variable definition 
        "-x","--execute", action="store", required=True, help="Help text for option X", metavar=("\b")
    )
    parser.add_argument("-y","--yesoption", help="Help text for option Y", default=False)
    parser.add_argument("-z", help="Help text for option Z", type=int)
    return parser.parse_args()
def main():
    args = get_args()
    execute = args.execute
    yarg = args.yesoption
    print(execute)
    print(yarg)

if __name__== "__main__":
    main()