import sys

def temp_swap(a,b):
    temp = a
    a = b
    b = a
    return a,b

if __name__=='__main__':
    x = int(sys.argv[1])
    y = int(sys.argv[2])

    x,y = temp_swap(x,y)

    print(x)
    print(y)
