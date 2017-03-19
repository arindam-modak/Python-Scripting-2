def Func(*args):
    for arg in args:
        print (arg)
       
l=[1,5,566,"abc"]
Func(1,2,3,54,"ham",l)
print ("\n")
Func(l[0],l[1],l[2],l[3])
print ("\n")
Func(*l)

