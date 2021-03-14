from numpy import nan
from sys import argv


def say_hello():
    if len(argv) < 2:
        usage()
        return
    print(f'Hello {argv[1]}')


def usage():
    print('You did not supply your name')
    print('please invoke using something like - howdy NAME')


if __name__ == '__main__':
    say_hello()
