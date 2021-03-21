import sys


def xor_swap(a,b):
    a = a ^ b
    b = a ^ b
    a = a ^ b
    return a,b

if __name__=='__main__':
    x = int(sys.argv[1])
    y = int(sys.argv[2])

    x,y = xor_swap(a,b)

    print(x)
    print(y)
