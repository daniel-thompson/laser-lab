from laser.util import *

w = 160
h = 120
r = 5
m = 2.5

def drill_holes(d, r=5, long_pci_tab=False):
	g = d.g()

	g.add(d.circle((r+4, r+4), m/2, **cut))
	g.add(d.circle((r+w-4, r+4), m/2, **cut))
	if not long_pci_tab:
		g.add(d.circle((r+4, r+h-4), m/2, **cut))
	g.add(d.circle((r+w-4, r+h-4), m/2, **cut))

	g.add(d.circle((r+w-35.5, r+h-4), m/2, **cut))
	g.add(d.circle((r+w-4, r+h-81), m/2, **cut))
	g.add(d.circle((r+w-35.5, r+h-81), m/2, **cut))

	return g

def base(d, r=5):
	g = d.g()

	g.add(d.rect((0, 0), (w+2*r, h+2*r), r, r, **cut))
	g.add(drill_holes(d, r))

	return g

top = base

if __name__ == "__main__":
	d = panel('ee96.svg', 170, 262)

	d.add(base(d))
	d.add(translate(top(d), 0, 132))

	d.save()
