import os

pth = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
print(f'pth: {repr(pth)}')

dir = os.path.join(pth, 'arch_temp')
print(f'dir: {repr(dir)}')

os.mkdir(dir)
with open(os.path.join(dir, 'foobarbaz321.txt'), 'w') as f:
    f.write('hello mom!')