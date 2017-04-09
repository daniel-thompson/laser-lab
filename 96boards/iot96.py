from laser.util import *

w = 60
h = 30

def base(d, r=5):
	g = d.g()

	#g.add(d.rect((0, 0), (w+r+r, h+r+r), r, r, **cut))
	p = d.path(('M', 0, r), **cut)
	t = Turtle(p)
	t.arc(90, r)
	t.forward(w)
	t.arc(90, r)
	t.forward(h)
	t.arc(90, r)
	t.forward(w-(26+10))
	t.arcto(20, 16, large_arc=False, angle_dir='-')
	t.forward(26-10)
	t.arc(90, r)
	t.close()
	g.add(p)

	g.add(d.circle((r+4, r+4), 2.5/2, **cut))
	g.add(d.circle((r+4, r+26), 2.5/2, **cut))
	g.add(d.circle((r+56, r+4), 2.5/2, **cut))
	g.add(d.circle((r+56, r+26), 2.5/2, **cut))

	return g

def top(d, r=5):
	g = base(d, r)
	g.add(d.rect((r+7.5, r+0.35), (41.0, 7.3), 0, 0, **cut))

	return g

def pillar(d, r=5):
	hole_support = 3

	g = d.g()

	t = Turtle(d.path(('M', r, r+4+hole_support), **cut))
	t.left(90)
	t.arc(90, r)
	t.forward(4+hole_support-r)
	t.arc(90, r)
	t.forward(4)
	t.arc(90, hole_support)
	t.forward(4+hole_support-r)
	t.arc(90, r)
	g.add(t.close())
	
	g.add(d.circle((r+4, 2.5), 2.5/2, **cut))

	return g

def side(d, r=5):
	hole_support = 3

	g = d.g()

	t = Turtle(d.path(('M', 0, r), **cut))
	t.arc(90, r)
	t.forward(w) # top
	t.arc(90, r)
	t.forward(h) # right side
	t.arc(90, r)
	t.forward(4+hole_support-r) # bottom edge
	t.arc(90, r)
	t.forward(4)
	t.arc(90, hole_support)
	t.forward(4)
	t.move(-90, h - 8 - 2*hole_support) # inner right side
	t.move(-90, 4)
	t.arc(90, hole_support)
	t.forward(4)
	t.move(-90, w - 8 - 2*hole_support) # inner top
	t.move(-90, 4)
	t.arc(90, hole_support)
	t.forward(4+hole_support-r)
	t.arc(90, r)
	g.add(t.close())

	g.add(d.circle((r+4, r+4), 2.5/2, **cut))
	g.add(d.circle((r+56, r+4), 2.5/2, **cut))
	g.add(d.circle((r+56, r+26), 2.5/2, **cut))

	return g
