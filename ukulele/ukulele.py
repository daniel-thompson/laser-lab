#
# Generate layers of a ukulele
#

import math

from laser import trig
from laser.util import *

# dimensions
scale=348
anchor_height=10
nut_height=5
nut_width=34
curve_height=100
body_height = scale/2 + 50 # body 'starts' at 12th fret (and its height includes the heel)
twelfth=43
body_wing=53.5
heel_width=12
saddle=60
tailpiece_radius=14
bottom_radius=15
cutout_radius=5
thickness=4

# calculated Y offsets
fretboard_y = anchor_height + nut_height
bridge_y = fretboard_y + scale

d = panel('fretboard.svg', 2100, 420)

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
	p = d.turtle(('M', -nut_width/2, 0), **cut)
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

def layer(l=1):
	curve_nut = (34, 33, 28, 15)
	curve_seventh = (39, 38, 33, 25)
	br = bottom_radius
	cutout_th = trig.theta(o=(twelfth-nut_width), a=scale)

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
		p = d.turtle(('M', -nut_width/2, 0), **cut)
	else:
		p = d.turtle(('M', -top_width/2, fretboard_y+scale/2), **cut)

	# top edge
	if l < len(curve_nut)+1:
		nut_edge = 5
		nut_spacing = (nut_width - 2*nut_edge) / 3

		slot_width = 1
		if l == len(curve_nut):
			slot_width=3
		half_width = slot_width / 2
		slot_depth = 3.5 + half_width

		p.right(90)
		p.forward(nut_edge - half_width)
		p.slot(slot_depth, slot_width, cut_width=0, radius=half_width)
		p.forward(nut_spacing - slot_width)
		p.slot(slot_depth, slot_width, cut_width=0, radius=half_width)
		p.forward(nut_spacing - slot_width)
		p.slot(slot_depth, slot_width, cut_width=0, radius=half_width)
		p.forward(nut_spacing - slot_width)
		p.slot(slot_depth, slot_width, cut_width=0, radius=half_width)
		p.forward(nut_edge - half_width)
		#p.forward(nut_width)
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
	p.curvexy((body_wing+body_correction, curve_height), th, (40, 60))
	p.forward(body_height - curve_height - br)
	p.arc(90, br)

	base_width = -br+body_wing+twelfth+body_wing-br

	# control cavity
	if l == 1 or l == 10:
		cc_depth = 0
		cc_lip = 0
	elif l == 2 or l == 9:
		cc_depth = thickness
		cc_lip = 0
	elif l == 3 or l == 8:
		cc_depth = 40
		cc_lip = thickness
	else:
		cc_depth = 40
		cc_lip = 0
	cc_width = (base_width - saddle)/2 - cutout_radius
	cc_width -= 2*cc_lip

	p.right(90)
	p.forward(cc_lip)
	p.left(90)
	p.forward(cc_lip)
	p.right(90)
	p.forward(cc_depth-cc_lip)
	if cc_depth > 4:
		p.arc(-90, 5)
		p.forward(cc_width - 10)
		p.arc(-90, 5)
	else:
		p.left(90)
		p.forward(cc_width)
		p.left(90)
	p.forward(cc_depth-cc_lip)
	p.right(90)
	p.forward(cc_lip)
	p.left(90)
	p.forward(cc_lip)
	p.right(90)

	# bottom edge
	if l <= 6:
		if l <= 3:
			adj = abs(l-3)
		else:
			adj = l-4
		# Enlarge the top and bottom sheet slightly... these will be sanded to give an angled edge
		if adj == 2:
			adj += 1
		adj *= 4 # we're cutting from 4mm ply
		depth = tailpiece_radius + trig.opp(h=tailpiece_radius, a=adj)

		p.arc(90, cutout_radius)
		p.forward(depth)
		p.left(90)
		p.forward(saddle)
		p.left(90)
		p.forward(depth)
		p.arc(90, cutout_radius)
		p.forward((base_width - saddle)/2 - cutout_radius)
	else:
		x = 11-3.5
		y = 65
		depth = 70

		p.arc(90, cutout_radius)
		p.curvexy((-x, -y), -cutout_th, (45, 15))
		p.forward(depth)
		p.left(90 - cutout_th)
		p.forward(saddle - 2*x - 2*trig.opp(h=depth, th=cutout_th))
		p.left(90 - cutout_th)
		p.forward(depth)
		p.curvexy((-x, y), -cutout_th, (15, 45))
		p.arc(90, cutout_radius)
		p.forward((base_width - saddle)/2 - cutout_radius)

	# left edge: body
	p.arc(90, br)
	p.forward(body_height - curve_height - br)
	p.curvexy((body_wing+body_correction, -curve_height), th, (60, 40))

	# left edge: neck
	if l == 1:
		p.forward(trig.hyp(th=th, a=scale/2))
	elif l < len(curve_nut)+1:
		p.forward(trig.hyp(th=th, a=scale/2))
		p.curvexy((-((nut_width - curve_nut[l-1]) / 2), -fretboard_y), -th, (fretboard_y/2, fretboard_y/2))
	g.add(p.close())

	# Recalcualte theta since the cut outs are based on the angles of the top layer
	th = cutout_th

	# Cutouts for tuners
	h = 80
	w = 40
	if l <= 5:
		g.add(mixin(d.rect((-(w/2), -(h/2)), (w, h), w/2, w/2, **cut),
			    rotate=th,
			    translate=(-(body_wing-20), scale-55)))
		g.add(mixin(d.rect((-(w/2), -(h/2)), (w, h), w/2, w/2, **cut),
			    rotate=-th,
			    translate=( (body_wing-20), scale-55)))
	else:
		def cutout():
			p = d.turtle(('M', -w/2, -h/2), **cut)
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

		g.add(mixin(cutout(), rotate=180+th, translate=(body_wing-20, -(scale-55))))
		g.add(mixin(cutout(), rotate=-th, translate=( body_wing-20, scale-55)))

	# Alignment dowels and bridge sound chanber
	if l <= 4:
		g.add(d.circle((0, body_height-180), 2.5, **cut))
		g.add(d.circle((0, body_height-100), 2.5, **cut))
	g.add(d.circle((0, body_height-20), 2.5, **cut))
	if l > 1 and l < 4:
		# The translate doesn't work... it ends up overriding
		# the translate applied to the group. Currently we workaround
		# this by drawing the bridge in the main draw loop.
		g.add(translate(bridge(saddle_cutout=False), 0, bridge_y))
	else:
		g.add(d.circle((-30-8, bridge_y+1.5), 2.5, **cut))
		g.add(d.circle((30+8, bridge_y+1.5), 2.5, **cut))
	if l > 1 and l < 7:
		g.add(d.circle((0, body_height+70), 2.5, **cut))

	
	return g

def bridge(saddle_cutout=True):
	g = d.g()

	# piezo will likely be 55x2.3x3mm (so is probably best to cut
        # two bridge pieces from 3mm ply and stack)
	if saddle_cutout:
		g.add(d.rect((-saddle/2, 0), (saddle, 3), **cut))
	g.add(d.rect((-saddle/2 - 16, -8), (saddle + 32, 3+16), **cut))

	return g

def tuner_mount():
	g = d.g()

	g.add(d.rect((0, 0), (20, 100), **cut))
	g.add(d.circle((10, 25+7), 9.6/2, **cut))
	g.add(d.circle((10, 75+7), 9.6/2, **cut))

	return g

def control_cavity_cover():
	g = d.g()
	
	base_width = -bottom_radius+body_wing+twelfth+body_wing-bottom_radius
	cc_width = (base_width - saddle)/2 - cutout_radius

	g.add(d.rect((0, 0), (cc_width, 32), **cut))
	g.add(d.circle((cc_width/2, 16), 4, **cut))

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


def xpos(n):
	return 75 + 160*n

# Overall diagram
d.add(translate(layer(1), xpos(0), 0))
d.add(translate(fretboard(15), xpos(0), fretboard_y))
d.add(translate(bridge(), xpos(0), bridge_y))
d.add(translate(nut(), xpos(0), 10))
d.add(translate(strings(), xpos(0), 0))
d.add(translate(tailpiece(), xpos(0), bridge_y+42-25))

# Layered diagram (check overall shape)
for i in range(1, 11):
	d.add(translate(layer(i), xpos(1), 0))
d.add(translate(bridge(), xpos(1), bridge_y))

# Add some tuner mounts
for i in range(7, 11):
	d.add(translate(tuner_mount(), xpos(2+i)+5, 0))
	d.add(translate(tuner_mount(), xpos(2+i)-25, 0))
d.add(translate(control_cavity_cover(), xpos(2+6), 0))

# Component diagrams
d.add(translate(fretboard(15), xpos(2), 15))
d.add(translate(bridge(), xpos(2), bridge_y))
d.add(translate(bridge(), xpos(2), bridge_y-30))
outline = { 'fill': 'none', 'stroke': 'lightgrey', 'stroke-width': 0.5 }
for i in range(1, 11):
	d.add(translate(layer(i), xpos(2+i), 0))
	if i > 4:
		d.add(d.rect((xpos(2+i)-80, 140), (160, 280), **outline))
	elif i % 2 == 0:
		d.add(d.rect((xpos(2+i)-80, 0), (160, 280), **outline))
		d.add(d.rect((xpos(2+i)-80, 280), (160, 140), **outline))
	else:
		d.add(d.rect((xpos(2+i)-80, 0), (160, 140), **outline))
		d.add(d.rect((xpos(2+i)-80, 140), (160, 280), **outline))


d.save()
