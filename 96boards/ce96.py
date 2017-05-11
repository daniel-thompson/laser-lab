from laser.util import *

w = 85
h = 54
r = 5

def drill_holes(d, r=5):
	g = d.g()

	g.add(d.circle((r+4, r+18.5), 2.5/2, **cut))
	g.add(d.circle((r+4, r+50), 2.5/2, **cut))
	g.add(d.circle((r+81, r+18.5), 2.5/2, **cut))
	g.add(d.circle((r+81, r+50), 2.5/2, **cut))

	return g

def base(d, r=5):
	g = d.g()

	g.add(d.rect((0, 0), (w+r+r, h+r+r), r, r, **cut))
	g.add(drill_holes(d, r))

	return g

top = base

def top_uart(d, r=5):
	g = d.g()

	p = Turtle(d.path(('M', 0, r), **cut))
	p.arc(90, r)
	p.forward(w)
	p.arc(90, r)
	p.forward(h)
	p.arc(90, r)
	p.forward(w - (35+42))
	p.right(90)
	p.forward(15+r)
	p.left(90)
	p.forward(42)
	p.left(90)
	p.forward(15+r)
	p.right(90)
	p.forward(35)
	p.arc(90, r)

	g.add(p.close())
	g.add(drill_holes(d, r))

	return g

def side(d, r=5):
	g = d.g()

	p = d.path(('M', 0, r), **cut)
	p.push_arc((2*r, 0), 0, r, large_arc=False)
	p.push('l', -r, 0) 
	p.push('l', 0, 18.5 - 2.5)
	p.push('l', 4, 0)
	p.push_arc((0, 5), 0, 2.5, large_arc=False)
	p.push('l', -4, 0)
	p.push('l', 0, 50 - 18.5 - 2.5 - 2.5)
	p.push('l', 4, 0)
	p.push_arc((0, 5), 0, 2.5, large_arc=False)
	p.push('l', -4, 0)
	p.push('l', 0, (h+r) - 50 - 2.5)
	p.push_arc((-r, -r), 0, r, large_arc=False)
	p.push('z')
	g.add(p)

	g.add(d.circle((r+4, r+18.5), 2.5/2, **cut))
	g.add(d.circle((r+4, r+50), 2.5/2, **cut))

	return g

