import argparse
import os


parser = argparse.ArgumentParser()
parser.add_argument('arg1')
parser.add_argument('arg2')

args = parser.parse_args()

print(f'arg1: {repr(args.arg1)}')
print(f'arg2: {repr(args.arg2)}')

pth1 = os.path.join(args.arg1, 'bar', 'baz')
pth2 = os.path.join(args.arg2, 'bar', 'baz')

print('---')
print(f'pth1: {pth1}')
print(f'pth2: {pth2}')

print('---')
print(f'repr(pth1): {repr(pth1)}')
print(f'repr(pth2): {repr(pth2)}')