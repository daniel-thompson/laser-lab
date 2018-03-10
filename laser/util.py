import math
import svgwrite
import sys
import types

cut = { 'fill': 'none', 'stroke': 'red', 'stroke-width': 0.5 }
engrave = { 'fill': 'none', 'stroke': 'blue', 'stroke-width': 0.5 }
raster = { 'fill': 'black' }

class Turtle(object):
	def __init__(self, path):
		self.p = path
		self.position = (0, 0)
		self.direction = 0

	def _vector(self, angle):
		d = math.radians(angle)
		return (round(math.sin(d), 6), round(-1*math.cos(d),6))

	def forward(self, length):
		v = [ i*length for i in self._vector(self.direction) ]
		self.p.push('l', v[0], v[1])

		return self

	def backward(self, length):
		right(180)
		forward(length)
		left(180)

		return self
	
	def right(self, angle):
		self.direction += angle

		return self
	
	def left(self, angle):
		self.direction -= angle

		return self

	def move(self, angle, length):
		self.right(angle)
		self.forward(length)

		return self

	def arc(self, angle, radius):
		if angle > 0:
			turn = 90
			angle_dir = '+'
		else:
			turn = -90
			angle_dir = '-'

		centre = [ i*radius for i in self._vector(self.direction + turn) ]
		rim =  [ i*radius for i in self._vector(self.direction + angle - turn) ]
		end = [ sum(i) for i in zip(centre, rim) ]

		self.p.push_arc(end, self.direction, radius, abs(angle) > 180, angle_dir)
		self.direction += angle

		return self

	def arcto(self, length, radius, large_arc=True, angle_dir = '+'):
		end = [ i*length for i in self._vector(self.direction) ]
		self.p.push_arc(end, self.direction, radius, large_arc, angle_dir)

		return self

	def curve(self, movement, angle, control_points):
		d1 = [ i*movement[0] for i in self._vector(self.direction) ]
		d2 = [ i*movement[1] for i in self._vector(self.direction + 90) ]
		d = [ i+j for i, j in zip(d1, d2) ]
		self.curvexy(d, angle, control_points)

	
	def curvexy(self, movement, angle, control_points):
		d = movement

		c1 = [ i*control_points[0] for i in self._vector(self.direction) ]
		self.direction += angle
		c2 = [ i*control_points[1] for i in self._vector(self.direction+180) ]
		c2 = [ i+j for i, j in zip(d, c2) ]

		self.p.push('c', c1[0], c1[1], c2[0], c2[1], d[0], d[1])


	def slot(self, depth, thickness, cut_width=0.2, radius=0):
		self.forward(cut_width/2)
		self.right(90)
		self.forward(depth - cut_width/2 - radius)
		if radius:
			self.arc(-90, radius)
		else:
			self.left(90)
		self.forward(thickness - cut_width - 2*radius)
		if radius:
			self.arc(-90, radius)
		else:
			self.left(90)
		self.forward(depth - cut_width/2 - radius)
		self.right(90)
		self.forward(cut_width/2)
	
	def close(self):
		self.p.push('z')
		return self.p

def trapez(self, insert=(0, 0), size=(1, 1), lx=0.1, rx=0.1, **extra):
	return self.path(
			('M', insert[0]+lx, insert[1],
			 'l', size[0]-lx-rx, 0,
			 'l', rx, size[1],
			 'l', -size[0], 0,
			 'z'), **extra)



def bind_method(obj, m):
	obj.__dict__[m.__name__] = types.MethodType(m, obj)

def panel(name, w, h):
	if len(sys.argv) >= 2:
		name = sys.argv[1]

	w = svgwrite.Drawing(name,
			size=('{}mm'.format(w), '{}mm'.format(h)),
			viewBox=('0, 0, {}, {}'.format(w, h)))
	bind_method(w, trapez)

	return w

def mixin(g, rotate=None, center=None, translate=None):
	if rotate:
		g.rotate(rotate, center)
	if translate:
		g.translate(translate[0], translate[1])
	return g

def rotate(g, angle, center=None):
	g.rotate(angle, center)
	return g

def translate(g, x, y):
	g.translate(x, y)
	return g

