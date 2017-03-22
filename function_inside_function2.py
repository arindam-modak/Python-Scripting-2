def addone(myfunc):
    def addoneinside():        ## or def addoneinside(*argd,**kwargs):
        return myfunc() + 1    ## or return myfunc(*args,**kwargs)+1
    return addoneinside

def oldfunc():
    return 3
newfunc=addone(oldfunc)
print (oldfunc(),newfunc())

oldfunc=addone(oldfunc)     ##here we replace oldfunc without crreating newfunc
print (oldfunc())

## OR

@addone                  ## @ is decorator; this command does the exact above function
def oldfunc():           ## or def oldfunc(x=546):
    return 3             ## return x

print (oldfunc())        ## print (oldfunc(45))
