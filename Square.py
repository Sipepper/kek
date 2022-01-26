import math as m
import pprint as p

SideLen = int(input('Input square side length: '))

def geom(SideLen):
    Perimeter = 4 * SideLen
    Area = SideLen * SideLen
    Diagonal = round(SideLen * m.sqrt(2),4)
    return (Perimeter, Area, Diagonal)

p.pprint(geom(SideLen))