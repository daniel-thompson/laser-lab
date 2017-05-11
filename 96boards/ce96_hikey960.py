#!/usr/bin/env python3

from laser.util import *
from ce96 import w, h
import ce96

d = panel('ce96_hikey960.svg', 161, 138)

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
d.add(translate(top_uart(d), 0, 66))

d.add(rotate(translate(ce96.side(d), 97+64,   0   ),  90))
d.add(rotate(translate(ce96.side(d), 97   ,   0+18), -90))
d.add(rotate(translate(ce96.side(d), 97+64,  20   ),  90))
d.add(rotate(translate(ce96.side(d), 97   ,  20+18), -90))
d.add(rotate(translate(ce96.side(d), 97+64,  40   ),  90))
d.add(rotate(translate(ce96.side(d), 97   ,  40+18), -90))
d.add(rotate(translate(ce96.side(d), 97+64,  60   ),  90))
d.add(rotate(translate(ce96.side(d), 97   ,  60+18), -90))
d.add(rotate(translate(ce96.side(d), 97+64,  80   ),  90))
d.add(rotate(translate(ce96.side(d), 97   ,  80+18), -90))
d.add(rotate(translate(ce96.side(d), 97+64, 100   ),  90))
d.add(rotate(translate(ce96.side(d), 97   , 100+18), -90))
d.add(rotate(translate(ce96.side(d), 97+64, 120   ),  90))
d.add(rotate(translate(ce96.side(d), 97   , 120+18), -90))

d.save()
