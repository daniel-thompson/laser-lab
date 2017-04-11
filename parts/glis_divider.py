#
# Generate a set of dividers to split an Ikea Glis box into four.
# 
# We'd actually use less acrylic if we divided the box into six
# (because that would only use two cross pieces) but that makes the
# individual compartments *way* too small.
#

from laser.util import *

d = panel('glis_divider.svg', 155+89+2, 124)

thickness = 2-0.2

def slot(p):
	p.right(90)
	p.forward(60.8/2)
	p.left(90)
	p.forward(thickness)
	p.left(90)
	p.forward(60.8/2)
	p.right(90)

def long_piece(x, y):
	p = Turtle(d.path(('M', x, y), **cut))
	p.right(90)
	p.forward(10.5)
	slot(p)
	p.forward((154.2/2)-(1.5*thickness+10.5))
	slot(p)
	p.forward((154.2/2)-(1.5*thickness+10.5))
	slot(p)
	p.forward(10.5)
	p.right(94.51)
	p.forward(55)
	p.arc(85.49, 6)
	p.forward(144.4-12)
	p.arc(85.49, 6)
	return p.close()

def cross_piece(x, y):
	p = Turtle(d.path(('M', x, y), **cut))
	p.right(90)
	p.forward(89)
	p.right(94.51)
	p.forward(55)
	p.arc(85.49, 6)
	p.forward(((79.3-12)/2) - (thickness/2))
	slot(p)
	p.forward(((79.3-12)/2) - (thickness/2))
	p.arc(85.49, 6)
	return p.close()

d.add(long_piece(0, 0))
d.add(cross_piece(0, 63))
d.add(cross_piece(89+2, 63))
d.add(cross_piece(154.2+2, 0))

d.save()
