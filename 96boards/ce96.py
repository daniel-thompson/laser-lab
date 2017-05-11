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

def top(d, r=5, hdmi_cutout=True, uart_cutout=False):
	g = d.g()

	p = Turtle(d.path(('M', 0, r), **cut))

	# Top edge has an arc to allow space to connect the HDMI
	# (on Hikey960 the HDMI is fairly deep)
	p.arc(90, r)
	if hdmi_cutout:
		p.forward(w-(25+(21/2)+r))
		p.arc(90, r)
		p.left(90)
		p.forward(21)
		p.left(90)
		p.arc(90, r)
		p.forward(25-((21/2)+r))
	else:
		p.forward(w)

	p.arc(90, r)
	p.forward(h)

	# Bottom edge has a detour to make space for the uart board
	p.arc(90, r)
	if uart_cutout:
		p.forward(w - (35+42+r))
		p.arc(90, r)
		p.forward(15+r)
		p.left(90)
		p.forward(42)
		p.left(90)
		p.forward(15+r)
		p.arc(90, r)
		p.forward(35-r)
	else:
		p.forward(w)

	p.arc(90, r)

	g.add(p.close())
	g.add(drill_holes(d, r))

	return g

def top_uart(d, r=5):
	return top(d, r, uart_cutout=True)

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


if __name__ == "__main__":
	d = panel('ce96.svg', 161, 138)

	d.add(base(d))
	d.add(translate(top(d), 0, 66))

	d.add(rotate(translate(side(d), 97+64,   0   ),  90))
	d.add(rotate(translate(side(d), 97   ,   0+18), -90))
	d.add(rotate(translate(side(d), 97+64,  20   ),  90))
	d.add(rotate(translate(side(d), 97   ,  20+18), -90))
	d.add(rotate(translate(side(d), 97+64,  40   ),  90))
	d.add(rotate(translate(side(d), 97   ,  40+18), -90))
	d.add(rotate(translate(side(d), 97+64,  60   ),  90))
	d.add(rotate(translate(side(d), 97   ,  60+18), -90))
	d.add(rotate(translate(side(d), 97+64,  80   ),  90))
	d.add(rotate(translate(side(d), 97   ,  80+18), -90))
	d.add(rotate(translate(side(d), 97+64, 100   ),  90))
	d.add(rotate(translate(side(d), 97   , 100+18), -90))
	d.add(rotate(translate(side(d), 97+64, 120   ),  90))
	d.add(rotate(translate(side(d), 97   , 120+18), -90))

	d.save()

