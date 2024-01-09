

import math
import os
import random
import re
import sys


import math
class Rectangle:
    base=""
    height=""

    def __init__(self,base,height):
        self.base=base
        self.height=height
    
    def area(self):
        a=float(self.base)
        b=float(self.height)
        return a*b
class Circle:
    radius=""

    def __init__(self,radius):
        self.radius=radius
    
    def area(self):
        a=float(self.radius)
        return math.pi*a*a
    

q = int(input())
queries = []
for _ in range(q):
    args = input().split()
    shape_name, params = args[0], tuple(map(int, args[1:]))
    if shape_name == "rectangle":
        a, b = params[0], params[1]
        shape = Rectangle(a, b)
    elif shape_name == "circle":
        r = params[0]
        shape = Circle(r)
    else:
        raise ValueError("invalid shape type")
    print("%.2f" % shape.area())

