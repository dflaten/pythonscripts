#!/usr/bin/env python3
import argparse
import os

from collections import ChainMap

'''
A ChainMap is a class that provides the abilityt o link multiple mappings
together such that they end up being a single unit.

When we create a chain of maps and then attempt to retrieve a value from
it ChainMap will iterate through each map in it and pass back the first
value defined for that key.
'''

def main():
    app_defaults = {"username": "admin", "password": "admin"}

    parser = argparse.ArgumentParser()
    parser.add_argument("-u", "--username")
    parser.add_argument("-p", "--password")
    args = parser.parse_args()
    # Creates a map of the command line arguments passed in by the user.
    command_line_arguments = {key: value for key, value in vars(args).items() if value}

    chain = ChainMap(command_line_arguments, os.environ, app_defaults)
    print(chain["username"])


if __name__ == "__main__":
    # The first time main is called if we passed in a username we
    # will have that printed. If we did not the app_defaul that 
    # is set will be used.
    main()
    # Now that we set an environmental variable it will be used
    # first to set the username variable to test unless one is
    # passed in by the user.
    os.environ["username"] = "test"
    main()