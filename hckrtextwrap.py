import textwrap
def wrap(string, max_width):
    return '\n'.join(textwrap.wrap(string, max_width))

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
#NOT Install PIP
'''
    o/p:
    Input (stdin)
    Download
    ABCDEFGHIJKLIMNOQRSTUVWXYZ
    4
    Your Output (stdout)
    ABCD
    EFGH
    IJKL
    IMNO
    QRST
    UVWX
    YZ
'''
