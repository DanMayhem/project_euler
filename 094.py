#!python
"""
It is easily proved that no equilateral triangle exists with integral length sides and integral area. However, the almost equilateral triangle 5-5-6 has an area of 12 square units.

We shall define an almost equilateral triangle to be a triangle for which two sides are equal and the third differs by no more than one unit.

Find the sum of the perimeters of all almost equilateral triangles with integral side lengths and area and whose perimeters do not exceed one billion (1,000,000,000).
"""

x = 2;
y = 1;
limit = 1000000000;
result = 0;
 
while(True):
    # b = a+1
    aTimes3 = 2 * x - 1
    areaTimes3 = y * (x - 2)
    if (aTimes3 > limit):
    	break
 
    if (aTimes3 > 0) and (areaTimes3 > 0) and (aTimes3 % 3 == 0) and (areaTimes3 % 3 == 0):
        a = aTimes3 // 3
        area = areaTimes3 // 3
        result += 3 * a + 1
 
    #b = a-1
    aTimes3 = 2 * x + 1
    areaTimes3 = y * (x + 2)
 
    if (aTimes3 > 0) and (areaTimes3 > 0) and (aTimes3 % 3 == 0) and (areaTimes3 % 3 == 0):
        a = aTimes3 // 3
        area = areaTimes3 // 3
 
        result += 3 * a - 1
 
    nextx = 2 * x + y * 3
    nexty = y * 2 + x
 
    x = nextx
    y = nexty
print(result)