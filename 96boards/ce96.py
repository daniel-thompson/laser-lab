from laser.util import *

w = 85
h = 54
h_ext = 100
r = 5

def drill_holes(d, r=5, extended=False):
	g = d.g()

	g.add(d.circle((r+4, r+18.5), 2.5/2, **cut))
	g.add(d.circle((r+81, r+18.5), 2.5/2, **cut))
	g.add(d.circle((r+4, r+50), 2.5/2, **cut))
	g.add(d.circle((r+81, r+50), 2.5/2, **cut))
	if extended:
		g.add(d.circle((r+4, r+96), 2.5/2, **cut))
		g.add(d.circle((r+81, r+96), 2.5/2, **cut))

	return g

def low_speed_connector(d, r=5):
	width = 43
	height = 6.5
	center = (2*10 + 38) / 2
	x = r + w - center - width/2
	y = r + h - 4 - height/2

	return d.rect((x, y), (width, height), **cut)

def base(d, r=5, extended=False):
	g = d.g()

	if extended:
		ht = h_ext
	else:
		ht = h

	g.add(d.rect((0, 0), (w+r+r, ht+r+r), r, r, **cut))
	g.add(drill_holes(d, r, extended))

	return g

top = base

def top(d, r=5, extended=False, hdmi_cutout=True, uart_cutout=False):
	g = d.g()

	if extended:
		ht = h_ext
	else:
		ht = h

	p = d.turtle(('M', 0, r), **cut)

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
	p.forward(ht)

	# Bottom edge has a detour to make space for the uart board
	p.arc(90, r)
	if uart_cutout:
		p.forward(w - (35+42+r))
		p.arc(90, r)
		p.forward(15)
		p.left(90)
		p.forward(42)
		p.left(90)
		p.forward(15)
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

def side(d, r=5, extra_depth=0):
	g = d.g()

	p = d.turtle(('M', 0, r), **cut)

	p.arc(90, r)
	p.right(90).forward(18.5 + r - 2.5)
	p.left(90).forward(4)
	p.arc(180, 2.5)
	p.forward(4+extra_depth)
	p.left(90).forward(50 - 18.5 - 2.5 - 2.5)
	p.left(90).forward(4+extra_depth)
	p.arc(180, 2.5)
	p.forward(4)
	p.left(90).forward(h - 50 - 2.5)
	p.left(90).forward(r)
	p.right(90).arc(180, r)
	g.add(p.close())

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

