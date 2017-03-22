def outside(y=10):
    x=5
    def inside():
        print ("abc")
        print (x)
        print (y)
    return inside

myfunc=outside(7)
myfunc()
