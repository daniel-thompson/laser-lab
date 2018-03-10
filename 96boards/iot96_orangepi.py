from laser.util import *
from iot96 import w, h
import iot96

#
# The case for the orange pi ends up with a *lot* of customization 
# compared to a regular IoT edition case. This is a combination of
# making space to store the WiFi antenna inside the case, accommodating
# the reset button in west edge, cutouts for the tall components and
# wells for components that otherwise interfere with the casing.
#
# Note that most of the customization could be avoided by having the
# case honour the height limits in the spec but that would result in
# a case nearly as wide as it is tall and we can do better than that!
#

def base(d, r=5):
	g = d.g()

	t = d.turtle(('M', 0, r), **cut)
	t.arc(90, r)
	t.forward(w)
	t.arc(90, r)
	t.forward(h+5) # Add an extra 5mm to house the WiFi antenna
	t.arc(90, r)
	t.forward(w-(26+9))
	t.arcto(18, 14, large_arc=False, angle_dir='-')
	t.forward(26-9)
	t.arc(90, r)
	g.add(t.close())

	g.add(translate(iot96.drill_holes(d, r), 0, 5))

	# Create a well to accommodate a large inductor on the underside
	# of the board
	g.add(d.rect((4+r, 20+r), (5, 5), **raster))

	return g

def top(d, r=5):
	g = d.g()

	t = d.turtle(('M', 0, r), **cut)
	t.arc(90, r)
	t.forward(w)
	t.arc(90, r)
	t.forward(h+5) # Add an extra 5mm to house the WiFi antenna
	t.arc(90, r)

	# Bottom edge
	t.forward(7-r)# 7-r
	t.arc(90, r)	# 7 
	t.forward(16)
	t.left(90)
	t.forward(14.5)   # 7+14.5
	t.left(90)
	t.forward(16)
	t.arc(90, r)    # 7+14.5+r
	# thumb dimple centre point is at 26 (so 26+-9 is coordinate)
	t.forward(w - (26+9) - (7+14.5+r))
	t.arcto(18, 14, large_arc=False, angle_dir='-')
	t.forward(26-9)
	t.arc(90, r)
	g.add(t.close())

	g.add(translate(iot96.low_speed_connector(d, r), 0, 5))
	g.add(translate(iot96.drill_holes(d, r), 0, 5))
	g.add(translate(d.rect((6.5, 24.8), (7.5, 5.2), **cut), r, r+5))

	return g


def pillar(d, r=5, resister_well=False):
	hole_support = 3

	g = d.g()

	t = d.turtle(('M', r, r+4+hole_support), **cut)
	t.left(90)
	t.arc(90, r)
	t.forward(4+hole_support-r)
	t.arc(90, r)
	t.forward(4+hole_support-r)
	t.arc(90, hole_support)
	t.forward(4+hole_support-r)
	t.arc(90, r)
	g.add(t.close())
	
	if resister_well:
		g.add(d.rect((2*r, r+2-1.5), (4, 1.5), **raster))

	g.add(d.circle((r+4, r+4), 2.5/2, **cut))

	return g

def side(d, r=5, side_switch=False):
	hole_support = 3

	g = d.g()

	t = d.turtle(('M', 0, r), **cut)
	t.arc(90, r)
	t.forward(w) # top
	t.arc(90, r)
	t.forward(h+5) # right side
	t.arc(90, r)
	t.forward(4+hole_support-r) # bottom edge
	t.arc(90, r)
	if side_switch:
		# We need a small notch to avoid the switch actuating part of the side
		# panel from getting stuck on the USB housing.
		t.right(90)
		t.forward(0.5)
		t.arc(-180, 0.5)
		t.forward(0.5)
		t.right(90)
		t.forward(3)
	else:
		t.forward(4)
	t.arc(90, hole_support)
	t.forward(4)
	t.move(-90, h - 8 - 2*hole_support) # inner right side
	t.move(-90, 4)
	t.arc(180, hole_support)
	#t.forward(4)
	#t.right(90)
	t.forward(4)
	t.left(90)
	t.forward(5-2+4-hole_support)
	#t.left(90)
	t.arc(-90, 2)
	t.forward(r+4-2)
	t.right(90)
	t.move(-90, w - 8 - 2*hole_support) # inner top

	# antenna notch
	t.forward(r+4-2)
	t.arc(-90, 2)
	t.forward(5-2+4-hole_support)
	t.left(90)
	t.forward(4)
	t.arc(180, hole_support)

	t.forward(4+hole_support-r)
	t.arc(90, r)
	g.add(t.close())

	g.add(d.circle((r+4, r+4+5), 2.5/2, **cut))
	g.add(d.circle((r+56, r+4+5), 2.5/2, **cut))
	if side_switch:
		g.add(d.rect((r+56-1.25, r+26+5-1.25), (3.5, 2.5), 1.25, 1.25, **cut))
	else:
		g.add(d.circle((r+56, r+26+5), 2.5/2, **cut))

	return g

if __name__ == "__main__":
	d = panel('iot96_orangepi.svg', 300, 200)

	d.add(base(d, 3))
	d.add(translate(top(d, 3), 0, 43))

	d.add(rotate(translate(side(d, 3), 0, 86+66), -90))
	d.add(rotate(translate(side(d, 3, side_switch=True), 0+17, 86+66+12), -90))
	d.add(rotate(translate(side(d, 3, side_switch=True), 0+34, 86+66+24), -90))
	d.add(rotate(translate(pillar(d, 3, resister_well=True), 0+51+7, 86+36+10), -180))
	d.add(rotate(translate(pillar(d, 3), 0+51+7, 86+36+10+12), -180))
	d.add(rotate(translate(pillar(d, 3), 0+51+7, 86+36+10+24), -180))

	d.save()
