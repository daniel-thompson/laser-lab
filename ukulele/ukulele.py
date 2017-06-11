#
# Generate layers of a ukulele
#

import math

from laser import trig
from laser.util import *

#
# TODO
#
#  * Add control cavity/sound chamber to inner layers
#  * Add control cavity cover to bottom layer
#  * Add string slots at top
#  * Add string holes on lower layers
#  * Add intersection boundaries (grey boxes: top to 280mm and 140mm to bottom)
#  * Add outlines for the tuner mounts (24x100mm)
#  * Experiment with additional body curves

# dimensions
scale=348
anchor_height=10
nut_height=5
nut_width=34
curve_height=100
body_height=curve_height+50  # body 'starts' at 12th fret (and its height includes the heel)
twelfth=43
heel_width=12
saddle=60
tailpiece_radius=10
bottom_radius=20
cutout_radius=5

# calculated Y offsets
fretboard_y = anchor_height + nut_height
bridge_y = fretboard_y + scale

d = panel('fretboard.svg', 1800, 420)

def fret(n):
	'''Position frets using a basic "rule of 18" algorithm.
	
	Might be better to replace this with a more sophisticated algorithm!
	Perhaps:
	http://www.luth.org/images/web_extras/al116/MagliariFretComp.pdf
	'''
	eighteen = 17.817153   # ;-)

	position = 0
	for i in range(n):
		position += (scale - position) / eighteen

	return position

def fretboard(num_frets=12):
	length=fret(num_frets+1)
	th = trig.theta(o=(twelfth-nut_width), a=scale)

	g = d.g()

	# Outline
	p = Turtle(d.path(('M', -nut_width/2, 0), **cut))
	p.right(90)
	p.forward(nut_width)
	p.right(90-th)
	p.forward(trig.hyp(th=th, a=length))
	p.right(90+th)
	p.forward(nut_width + (twelfth-nut_width) * (length / (scale/2)))
	p.right(90+th)
	g.add(p.close())

	# Frets
	for i in range(num_frets):
		y = fret(i+1)
		w = nut_width + (twelfth-nut_width) * (y / (scale/2))
		g.add(d.line((-w/2, y), (w/2, y), **engrave))

	# Inlays
	for i in (5, 7, 10):
		y = (fret(i) + fret(i-1)) / 2
		g.add(d.circle((0, y), 2, **engrave))

	return g

def top():
	br = bottom_radius
	th = trig.theta(o=(twelfth-nut_width), a=scale)

	g = d.g()

	# Main outline
	p = Turtle(d.path(('M', -nut_width/2, 0), **cut))
	p.right(90)
	p.forward(nut_width)
	p.right(90)
	p.forward(15)
	p.left(th)
	p.forward(trig.hyp(th=th, a=scale/2))
	p.curvexy((50, curve_height), th, (40, 60))
	p.forward(scale/2 - 100 + 50 - br)
	p.arc(90, br)
	base_width = -br+50+twelfth+50-br
	p.forward((base_width - saddle)/2 - cutout_radius)
	p.arc(90, cutout_radius)
	p.forward(2*tailpiece_radius)
	p.left(90)
	p.forward(saddle)
	p.left(90)
	p.forward(2*tailpiece_radius)
	p.arc(90, cutout_radius)
	p.forward((base_width - saddle)/2 - cutout_radius)
	p.arc(90, br)
	p.forward(scale/2 - 100 + 50 - br)
	p.curvexy((50, -curve_height), th, (60, 40))
	g.add(p.close())

	# Cutouts for tuners
	h = 80
	w = 40
	g.add(mixin(d.rect((-(w/2), -(h/2)), (w, h), w/2, w/2, **cut),
		    rotate=th,
		    translate=(-30, scale-55)))
	g.add(mixin(d.rect((-(w/2), -(h/2)), (w, h), w/2, w/2, **cut),
		    rotate=-th,
		    translate=( 30, scale-55)))

	return g

def layer(l=1):
	curve_nut = (34, 33, 28, 15)
	curve_seventh = (39, 38, 33, 25)
	br = bottom_radius

	if l == 1:
		th = trig.theta(o=(twelfth-nut_width), a=scale)
		body_correction = 0
	elif l < len(curve_nut)+1:
		th = trig.theta(o=(curve_seventh[l-1] - curve_nut[l-1])/2,
				a=(fret(7)))
		body_correction = (twelfth - curve_nut[l-1])/2 - trig.opp(th=th, a=scale/2)
	else:
		th = trig.theta(o=(twelfth-nut_width), a=scale)
		body_correction = ((twelfth - heel_width) * l/10) / 2
		top_width = twelfth - 2*body_correction

	g = d.g()

	# Main outline
	if l < len(curve_nut)+1:
		p = Turtle(d.path(('M', -nut_width/2, 0), **cut))
	else:
		p = Turtle(d.path(('M', -top_width/2, fretboard_y+scale/2), **cut))

	# top edge
	if l < len(curve_nut)+1:
		# TODO: string slots and holes
		p.right(90)
		p.forward(nut_width)
		p.right(90)
	else:
		p.right(th)
		height = heel_width/2 + 40 * (1 - math.sin(math.pi * (l-5) / 10))
		p.curvexy((top_width/2, -height), 90-th, (height, heel_width/2))
		p.curvexy((top_width/2, height), 90-th, (heel_width/2, height))

	# right edge: neck
	if l == 1:
		p.forward(fretboard_y)
		p.left(th)
		p.forward(trig.hyp(th=th, a=scale/2))
	elif l < len(curve_nut)+1:
		p.curvexy((-((nut_width - curve_nut[l-1]) / 2), fretboard_y), -th, (fretboard_y/2, fretboard_y/2))
		p.forward(trig.hyp(th=th, a=scale/2))

	# right edge: body
	p.curvexy((50+body_correction, curve_height), th, (40, 60))
	p.forward(scale/2 - 100 + 50 - br)
	p.arc(90, br)

	# bottom edge
	base_width = -br+50+twelfth+50-br
	p.forward((base_width - saddle)/2 - cutout_radius)
	p.arc(90, cutout_radius)
	p.forward(2*tailpiece_radius)
	p.left(90)
	p.forward(saddle)
	p.left(90)
	p.forward(2*tailpiece_radius)
	p.arc(90, cutout_radius)
	p.forward((base_width - saddle)/2 - cutout_radius)

	# left edge: body
	p.arc(90, br)
	p.forward(scale/2 - 100 + 50 - br)
	p.curvexy((50+body_correction, -curve_height), th, (60, 40))

	# left edge: neck
	if l == 1:
		p.forward(trig.hyp(th=th, a=scale/2))
	elif l < len(curve_nut)+1:
		p.forward(trig.hyp(th=th, a=scale/2))
		p.curvexy((-((nut_width - curve_nut[l-1]) / 2), -fretboard_y), -th, (fretboard_y/2, fretboard_y/2))
	g.add(p.close())

	# Recalcualte theta since the cut outs are based on the angles of the top layer
	th = trig.theta(o=(twelfth-nut_width), a=scale)

	# Cutouts for tuners
	h = 80
	w = 40
	if l <= 5:
		g.add(mixin(d.rect((-(w/2), -(h/2)), (w, h), w/2, w/2, **cut),
			    rotate=th,
			    translate=(-30, scale-55)))
		g.add(mixin(d.rect((-(w/2), -(h/2)), (w, h), w/2, w/2, **cut),
			    rotate=-th,
			    translate=( 30, scale-55)))
	else:
		def cutout():
			p = Turtle(d.path(('M', -w/2, -h/2), **cut))
			p.forward(10)
			p.right(90)
			p.forward(16)
			p.right(90)
			p.forward(10)
			p.left(90)
			p.forward(w/2 - 16)
			p.arc(90, w/2)
			p.forward(h-w)
			p.arc(90, w/2)
			p.forward(w/2 - 16)
			p.left(90)
			p.forward(10)
			p.right(90)
			p.forward(16)
			return p.close()

		g.add(mixin(cutout(), rotate=180+th, translate=(30, -(scale-55))))
		g.add(mixin(cutout(), rotate=-th, translate=( 30, scale-55)))

	return g

def bridge():
	g = d.g()

	# piezo will likely be 55x2.3x3mm (so is probably best to cut two bridge pieces from 3mm ply and stack
	g.add(d.rect((-saddle/2, 0), (saddle, 3), **cut))
	g.add(d.rect((-saddle/2 - 16, -8), (saddle + 32, 3+16), **cut))

	return g

def strings():
	g = d.g()

	nut_edge = 5
	nut_spacing = (nut_width - 2*nut_edge) / 3

	tailpiece_edge = 9
	tailpiece_spacing = (saddle - 2*tailpiece_edge) / 3
	tailpiece_y = scale+15+50-25

	for i in range(4):
		mul = -1.5 + i
		g.add(d.line((mul*nut_spacing, 5), (mul*tailpiece_spacing, tailpiece_y), **engrave))

	return g

def nut():
	return d.rect((-nut_width/2, 0), (nut_width, 5), **raster)

def tailpiece():
	return d.rect((-saddle/2, 0), (saddle, 2*tailpiece_radius), **raster)


# Overall diagram
d.add(translate(top(), 75, 0))
d.add(translate(layer(1), 75, 0)) # Verify layer(1) matches top()
d.add(translate(fretboard(15), 75, fretboard_y))
d.add(translate(bridge(), 75, bridge_y))
d.add(translate(nut(), 75, 10))
d.add(translate(strings(), 75, 0))
d.add(translate(tailpiece(), 75, bridge_y+50-25))

def xpos(n): 
	return 75 + 150*n

# Layered diagram (check overall shape)
for i in range(1, 11):
	d.add(translate(layer(i), xpos(1), 0))


# Component diagrams
d.add(translate(fretboard(15), xpos(2), 15))
d.add(translate(bridge(), xpos(2), bridge_y))
d.add(translate(bridge(), xpos(2), bridge_y-20))
for i in range(1, 11):
	d.add(translate(layer(i), xpos(2+i), 0))
d.save()
