#!/usr/bin/env python3

from laser.util import *
from ce96 import w, h
import ce96

d = panel('ce96_hikey960.svg', w + 10 + 60, 2 * (h+10) +2)

def top_uart(d, r=5):
	g = d.g()

	p = Turtle(d.path(('M', 0, r), **cut))
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
	# Bottom edge has a detour to make space for the uart board
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
	g.add(ce96.drill_holes(d, r))

	return g

d.add(ce96.base(d))
d.add(translate(top_uart(d), 0, h + 12))

for i in range(0, 60, 20):
	d.add(translate(ce96.side(d), w + 12 + i, 0))
	d.add(translate(ce96.side(d), w + 12 + i, h + 12))
	d.add(rotate(translate(ce96.side(d), w + 12 + 18 + i, 64), 180))
	d.add(rotate(translate(ce96.side(d), w + 12 + 18 + i, 64 + h + 12), 180))

d.save()
