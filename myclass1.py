class myclass(object):
    def __init__(self):
        self.x=5

TypeClass= type("TypeClass",(object,),{"x":5})   

m=myclass()
t=TypeClass()

print (m.x)
print (t.x)
