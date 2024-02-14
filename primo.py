print("Hello world")

print(10*10)

from math import sqrt
import math
print(sqrt((10.123**2)+(30.456**2)))


from math import sin
from math import cos
from math import asin
from math import sqrt
from math import radians

A = radians(59.9)
A1 = radians(10.8)
B = radians(49.3)
B1 = radians(-123.1)
r = 6371

el1 = sin (1 / 2 * (B - A)) **2
el2 = cos (A) * cos (B) * sin (1 / 2 * (B1 - A1))**2

d = r * 2 * asin(sqrt((el1 + el2)))

d1 = 2*r*asin(sqrt(sin(1/2*(B-A))**2+cos(A)*cos(B)*sin(1/2*(B1-A1))**2))

print (d1)