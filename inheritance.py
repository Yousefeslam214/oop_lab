class base :
    def __init__(self):
        self._name = "yousef" #protect

class Derived(base):
    def __init__(self):
        base.__init__(self)
        print("czajfklajfsf")
        print(self._name)

obj1 = Derived()
obj2 = base()
#print(obj2._name)
print()
print()
print()
class member :
    def __init__ (self,name):
        self.__name = name   #private
        
one = member('ahafjs') 
print(one._member__name)


