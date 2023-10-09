class Triangle:
    base=""
    height=""

    def __init__(self,base,height):
        self.base=base
        self.height=height
    
    def calculate_area(self):
        a=float(self.base)
        b=float(self.height)
        return .5*a*b

t1=Triangle(10,20)
t2=Triangle(20,30)
print(t1.calculate_area())
print(t2.calculate_area())

                
    