#!/usr/bin/env python3

from laser.util import *
from ce96 import w, h
import ce96

d = panel('ce96_hikey960.svg', w + 10 + 60, 2 * (h+10) +2)

def top(d, r=5):
	g = ce96.top(d, r, uart_cutout=True)

	# Add a cut-out for the boot jumpers
	g.add(d.rect((w + r - 6, 48 + r - 9), (6, 9), **cut))

	return g

d.add(ce96.base(d))
d.add(translate(top(d), 0, h + 12))

for i in range(0, 60, 20):
	d.add(translate(ce96.side(d), w + 12 + i, 0))
	d.add(translate(ce96.side(d), w + 12 + i, h + 12))
	d.add(rotate(translate(ce96.side(d), w + 12 + 18 + i, 64), 180))
	d.add(rotate(translate(ce96.side(d), w + 12 + 18 + i, 64 + h + 12), 180))

d.save()
