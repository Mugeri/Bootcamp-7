def funky(a, b):
    if type(a)== int and type (b)== int:
        return (a + b)
    elif type (a)== float and type (b)== float:
        return (a + b)
    elif type (a)== str and type (b)== str:
        return (a + b)
    elif type (a)== str or type (b)== str:
        return str(a) + str(b)
    elif type (a)== list and type (b)== list:
        return (a + b)
    elif type (a)== dict and type (b)== dict:
        dictionary = dict(a.items() + b.items())
        return dictionary
    else:
        print "NO CAN DO"

print funky(5,6)
print funky(7.8, 9.9)
print funky("hello","murugi")
print funky([4, 5, 6], [7,3,9])
x = {1:"one"}
y = {2:"two"}
print funky(x,y)
print funky("hi ",10)
