import math

def theta(a=0, o=0, h=0, degrees=True):
	#           On
	# Soldiers       Horseback
	if not a:
		t = math.asin(o/h)
	#            A       
	# Called         Hal
	elif not o:
		t = math.acos(a/h)
	#           Our
	# To             Advance
	elif not h:
		t = math.atan(o/a)
	else:
		raise ArithmeticError("Too many arguments")

	if degrees:
		t = math.degrees(t)
	
	return t

def adj(th=0, o=0, h=0, degrees=True):
	if degrees:
		th = math.radians(th)

	if not th:
		return math.sqrt(h**2 - o**2) 
	elif not o:
		return math.cos(th) * h
	elif not h:
		return o / math.tan(th)
	else:
		raise ArithmeticError("Too many arguments")



def opp(th=0, a=0, h=0, degrees=True):
	if degrees:
		th = math.radians(th)

	if not th:
		return math.sqrt(h**2 - a**2) 
	elif not a:
		return math.sin(th) * h
	elif not h:
		return math.tan(th) * a
	else:
		raise ArithmeticError("Too many arguments")

def hyp(th=0, a=0, o=0, degrees=True):
	if degrees:
		th = math.radians(th)

	if not th:
		return math.sqrt(o**2 + a**2)
	elif not a:
		return o / math.sin(th)
	elif not o:
		return a / math.cos(th)
	else:
		raise ArithmeticError("Too many arguments")

