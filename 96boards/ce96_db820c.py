#!/usr/bin/env python3

from laser.util import *
from ce96 import w, h_ext
import ce96

h = h_ext

d = panel('ce96_db820c.svg', 2 * (w+10) + 2, h+10)

def top(d, r=5):
	g = d.g()

	p = d.turtle(('M', 0, r), **cut)
	p.arc(90, r)
	# Top edge has an arc to allow space to connect the HDMI
	# (on Hikey960 the HDMI is fairly deep)
	p.forward(w-(25+(21/2)+r))
	p.arc(90, r)
	p.left(90)
	p.forward(21)
	p.left(90)
	p.arc(90, r)
	p.forward(25-((21/2)+r))
	p.arc(90, r)
	p.forward(h)
	p.arc(90, r)

	# Bottom edge has a detour to make space for the RJ45 connector
	# (17mm wide RJ45 is 10mm from edge of board (so we use 9 and 19 as
	# our step sizes)
	p.forward(9-r)
	p.arc(90, r)
	p.forward(17)
	p.left(90)
	p.forward(19)
	p.left(90)
	p.forward(17)
	p.arc(90, r)
	p.forward(w - (9+19+r))
	p.arc(90, r)

	g.add(p.close())
	g.add(ce96.drill_holes(d, r, extended=True))
	g.add(ce96.low_speed_connector(d, r))

	return g

d.add(ce96.base(d, extended=True))
d.add(translate(top(d), w + 12, 0))

d.save()
