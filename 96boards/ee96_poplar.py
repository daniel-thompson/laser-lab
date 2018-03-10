#!/usr/bin/env python3

from laser.util import *
from ee96 import w, h
import ee96

def top_poplar(d, r=5, access_spdif=False):
	g = d.g()

	p = d.turtle(('M', 0, r), **cut)

	p.arc(90, r)
	p.forward(73-r)
	if access_spdif:
		p.arc(90, r)
		p.forward(9)
		p.left(90)
		p.forward(12)
		p.left(90)
		p.forward(9)
		p.arc(90, r)
	else:
		p.forward(12+2*r)
	p.forward(w-(73+12+r))
	p.arc(90, r)
	p.forward(h)
	p.arc(90, r)
	p.forward(w-(22+16+r))
	p.arc(90, r)
	p.forward(16)
	p.left(90)
	p.forward(16)
	p.left(90)
	p.forward(16)
	p.arc(90, r)
	p.forward(22-r)
	p.arc(90, r)

	g.add(p.close())
	if not access_spdif:
		g.add(d.rect((r+71.5, r-0.5), (12, 9.5), **cut)) # SPDIF
	#g.add(d.rect((r+22, r+h-16), (16, 16), **cut)) # USB 2.0
	g.add(ee96.drill_holes(d, r, long_pci_tab=True))

	return g

def pci_standoff(d, top_standoff=15, base_standoff=8):
	pci_height=0

	p = d.turtle(('M', 0, 0), **cut)

	p.right(90)
	p.forward(18) # depth
	p.right(90)
	p.forward(top_standoff + base_standoff + 1.6) # long side
	p.right(90)
	p.forward(18) # depth
	p.right(90)
	p.forward(base_standoff)
	p.slot(13, 1.6)
	p.forward(7)

	p.arc(90, 0.3)
	p.forward(10.5)
	p.arc(90, 0.3)
	p.left(90)
	p.forward(2.5)
	p.left(90)
	p.forward(2.5)
	p.left(90)
	p.forward(2.5)
	p.left(90)
	p.arc(90, 0.3)
	p.forward(10.5)
	p.arc(90, 0.3)

	return p.close()

d = panel('ce96_uart.svg', 200, 300)

d.add(ee96.base(d))
d.add(translate(top_poplar(d), 0, 132))
d.add(translate(pci_standoff(d), 172, 0))

d.save()
