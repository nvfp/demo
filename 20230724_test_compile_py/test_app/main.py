import base64

your_code = base64.b64encode(b"""

def main():
    print('123 abc')


if __name__ == '__main__':
    main()
""")

exec(base64.b64decode(your_code))