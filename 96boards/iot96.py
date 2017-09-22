from laser.util import *

w = 60
h = 30

def drill_holes(d, r=5):
	g = d.g()

	g.add(d.circle((r+4, r+4), 2.5/2, **cut))
	g.add(d.circle((r+4, r+26), 2.5/2, **cut))
	g.add(d.circle((r+56, r+4), 2.5/2, **cut))
	g.add(d.circle((r+56, r+26), 2.5/2, **cut))

	return g

def low_speed_connector(d, r=5, gpio_3v3=False):
	if gpio_3v3:
		# TODO: this cutout *may* be 0.5mm to wide
		return d.rect((r+7.5, r+0.35), (41.0, 7.3), 0, 0, **cut)

	width = 43
	height = 6.5
	center = (2*10 + 38) / 2
	x = r + center - width/2
	y = r + 4 - height/2

	return d.rect((x, y), (width, height), **cut)

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

	g.add(drill_holes(d, r))

	return g

def top(d, r=5):
	# TODO: Cutout is probably tailored for the 15x2 connector
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

if __name__ == "__main__":
	d = panel('iot96_carbon.svg', 300, 200)

	d.add(base(d, 3))
	d.add(translate(top(d, 3), 0, 38))

	d.add(rotate(translate(side(d, 3), 0, 76+66), -90))
	d.add(rotate(translate(side(d, 3), 0+12, 76+66+12), -90))
	d.add(rotate(translate(side(d, 3), 0+24, 76+66+24), -90))
	d.add(rotate(translate(pillar(d, 3), 0+36-7, 76+36+10), -90))
	d.add(rotate(translate(pillar(d, 3), 0+36-7, 76+36+10+12), -90))
	d.add(rotate(translate(pillar(d, 3), 0+36-7, 76+36+10+24), -90))

	d.save()
