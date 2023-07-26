import os

pth = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(f'pth: {repr(pth)}')

with open(os.path.join(pth, 'foobarbaz321.txt'), 'w') as f:
    f.write('hello mom!')