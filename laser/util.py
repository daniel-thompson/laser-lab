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

	def slot(self, depth, thickness, cut_width=0.2):
		self.forward(cut_width/2)
		self.right(90)
		self.forward(depth - cut_width/2)
		self.left(90)
		self.forward(thickness - cut_width)
		self.left(90)
		self.forward(depth - cut_width/2)
		self.right(90)
		self.forward(cut_width/2)
	
	def close(self):
		self.p.push('z')
		return self.p

def bind_method(obj, m):
	obj.__dict__[m.__name__] = types.MethodType(m, obj)

def panel(name, w, h):
	if len(sys.argv) >= 2:
		name = sys.argv[1]
	return svgwrite.Drawing(name,
			size=('{}mm'.format(w), '{}mm'.format(h)),
			viewBox=('0, 0, {}, {}'.format(w, h)))

def rotate(g, angle, center=None):
	g.rotate(angle, center)
	return g

def translate(g, x, y):
	g.translate(x, y)
	return g

