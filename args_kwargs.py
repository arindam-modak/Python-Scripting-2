def func(*args,**kwargs):
    for arg in args:
        print (arg)
    for item in kwargs.items():
        print (item)

func(12,x=234,y=43)
