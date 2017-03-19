def func(*args):
    for arg in args:
        
        print (arg)
    print
    for arg in args:
        for i in arg:
            print (i)

l=[[1,2],[3,4]]
func(*l)
