#!python
"""
In laser physics, a "white cell" is a mirror system that acts as a delay line for the laser beam. The beam enters the cell, bounces around on the mirrors, and eventually works its way back out.

The specific white cell we will be considering is an ellipse with the equation 4x2 + y2 = 100

The section corresponding to −0.01 ≤ x ≤ +0.01 at the top is missing, allowing the light to enter and exit through the hole.


The light beam in this problem starts at the point (0.0,10.1) just outside the white cell, and the beam first impacts the mirror at (1.4,-9.6).

Each time the laser beam hits the surface of the ellipse, it follows the usual law of reflection "angle of incidence equals angle of reflection." That is, both the incident and reflected beams make the same angle with the normal line at the point of incidence.

In the figure on the left, the red line shows the first two points of contact between the laser beam and the wall of the white cell; the blue line shows the line tangent to the ellipse at the point of incidence of the first bounce.

The slope m of the tangent line at any point (x,y) of the given ellipse is: m = −4x/y

The normal line is perpendicular to this tangent line at the point of incidence.

The animation on the right shows the first 10 reflections of the beam.

How many times does the beam hit the internal surface of the white cell before exiting?
"""

from math import sqrt, atan

def get_intersection(x, y, m):
	#y = mx+b, sp solve for b
	b = y-m*x
	#4xx+yy=100 => 4xx+(mx+b)(mx+b)-100=0 =>
	#4xx + mmxx +2mxb + bb - 100 = 0 =>
	#(4+mm)xx +2mb(x) + (bb-100) = 0
	#x = (-2mb +- sqrt((2mb)**2 - 4(4+mm)(bb-100)))/2a
	A = 4+m*m
	B = 2*m*b
	C = b*b-100
	xp = (-B + sqrt(B*B - 4*A*C))/(2*A)
	if abs(x-xp) < .0001:
		xp = (-B - sqrt(B*B - 4*A*C))/(2*A)
	yp = m*xp+b
	#calculate mp
	t = -4*xp/yp
	ta = (m-t)/(1+m*t)
	mp = (t-ta)/(1+ta*t)
	return (xp, yp, mp)


x, y, m = 0.0, 10.1, (-9.6-10.1)/1.4

c = 0
escaped = False
print([c, x, y, m])

while not escaped:
	c+=1
	x, y, m = get_intersection(x, y, m)
	escaped = y > 0 and x > -0.01 and x < 0.01
	print([c, x, y, m])
