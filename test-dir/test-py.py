import argparse


parser = argparse.ArgumentParser()
parser.add_argument('arg1')
parser.add_argument('arg2')

args = parser.parse_args()

print(f'arg1: {repr(args.arg1)}')
print(f'arg2: {repr(args.arg2)}')