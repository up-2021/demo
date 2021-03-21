import sys

#proba
#proba 2, neka izmena
def temp_swap(a,b):
    temp = a
    a = b
    b = a
    return a,b

def xor_swap(a,b):
    a = a ^ b
    b = a ^ b
    a = a ^ b
    return a,b

if __name__=='__main__':
    x = int(sys.argv[1])
    y = int(sys.argv[2])

    x,y = temp_swap(x,y)
    x,y = xor_swap(a,b)

    print(x)
    print(y)
