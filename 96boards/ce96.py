from laser.util import cut

w = 85
h = 54
r = 5

def base(d, r=5):
	g = d.g()

	g.add(d.rect((0, 0), (w+r+r, h+r+r), r, r, **cut))
	g.add(d.circle((r+4, r+18.5), 2.5/2, **cut))
	g.add(d.circle((r+4, r+50), 2.5/2, **cut))
	g.add(d.circle((r+81, r+18.5), 2.5/2, **cut))
	g.add(d.circle((r+81, r+50), 2.5/2, **cut))

	return g

top = base

def top_uart(d, r=5):
	g = d.g()

	p = d.path(('M', 0, r), **cut)
	p.push_arc((r, -r), 0, r, large_arc=False)
	p.push('l', w, 0)
	p.push_arc((r, r), 0, r, large_arc=False)
	p.push('l', 0, h)
	p.push_arc((-r, r), 0, r, large_arc=False)

	# Bottom edge has a detour to make space for the uart board
	p.push('l', -w + (35+42), 0)
	p.push('l', 0, 44-(h+2*r))
	p.push('l', -42, 0)
	p.push('l', 0, (h+2*r)-44)
	p.push('l', -35, 0)

	p.push_arc((-r, -r), 0, r, large_arc=False)
	p.push('z')
	g.add(p)

	g.add(d.circle((r+4, r+18.5), 2.5/2, **cut))
	g.add(d.circle((r+4, r+50), 2.5/2, **cut))
	g.add(d.circle((r+81, r+18.5), 2.5/2, **cut))
	g.add(d.circle((r+81, r+50), 2.5/2, **cut))

	return g

def side(d, r=5):
	g = d.g()

	p = d.path(('M', 0, r), **cut)
	p.push_arc((2*r, 0), 0, r, large_arc=False)
	p.push('l', -r, 0) 
	p.push('l', 0, 18.5 - 2.5)
	p.push('l', 4, 0)
	p.push_arc((0, 5), 0, 2.5, large_arc=False)
	p.push('l', -4, 0)
	p.push('l', 0, 50 - 18.5 - 2.5 - 2.5)
	p.push('l', 4, 0)
	p.push_arc((0, 5), 0, 2.5, large_arc=False)
	p.push('l', -4, 0)
	p.push('l', 0, (h+r) - 50 - 2.5)
	p.push_arc((-r, -r), 0, r, large_arc=False)
	p.push('z')
	g.add(p)

	g.add(d.circle((r+4, r+18.5), 2.5/2, **cut))
	g.add(d.circle((r+4, r+50), 2.5/2, **cut))

	return g

