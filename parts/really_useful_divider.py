#
# Generate a set of dividers to split an 9l Really Useful Box into five
# half height compartments.
# 

import math
from laser.util import *

depth = 135 / 2
width = 214

long_length = 238
short_length = 104.5
length = long_length + short_length

overhang = 10
thickness = 4

# Delta between the long and short edges to match the angle of the box
# sides
toe_in = 1.5
toe_radius = 2
toe_angle  = math.degrees(math.acos(toe_in/depth))
toe_depth = math.sqrt(toe_in**2 + depth**2)

d = panel('really_useful_divider.py', 300, 200)

def side_piece(d, x, y, length):
	p = Turtle(d.path(('M', x, y), **cut))
	p.right(90)
	p.forward(toe_in)
	p.forward(length - (thickness/2))
	p.slot(depth/2, thickness)
	p.arc(90, overhang)
	p.forward(depth - overhang)
	p.right(90)
	p.forward(overhang+length+(thickness/2)-toe_radius)
	p.arc(toe_angle, toe_radius)
	return p.close()
bind_method(d, side_piece)

def cross_piece(d, x, y):
	p = Turtle(d.path(('M', x, y), **cut))
	p.right(90)
	p.forward(2*toe_in + width)
	p.right(180-toe_angle)
	p.forward(toe_depth-toe_radius)
	p.arc(toe_angle, toe_radius)

	# complex bottom edge
	p.forward(width/3 - (thickness/2) - toe_radius)
	p.slot(depth/2, thickness)
	p.forward((width/2) - (width/3) - thickness)
	p.slot(depth/2, thickness)
	p.forward((width/2) - (width/3) - thickness)
	p.slot(depth/2, thickness)
	p.forward(width/3 - (thickness/2) - toe_radius)

	p.arc(toe_angle, toe_radius)
	return p.close()
bind_method(d, cross_piece)

d.add(d.side_piece(0, 0, long_length))
d.add(d.side_piece(0, depth+2, long_length))

# Second sheet
d.add(d.cross_piece(0, 200))
d.add(d.side_piece(0, 200+depth+2, short_length))

d.save()
