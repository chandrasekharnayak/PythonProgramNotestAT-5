def decore(add):
    def inner(a,b):
        mul = a*b
        return mul,add(a,b)
    return inner

@decore
def add(a,b):
    c= a+b
    return c
print(add(10,20))

