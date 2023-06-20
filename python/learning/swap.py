#Method:1
a=1
b=2

def swap(x,y):
    return y,x


#Method:2
a=1
b=2


def swap(x,y):
    x=x+y
    y=x-y
    x=x-y
    return x,y
