from laser.util import *

r = 2

d = panel('k40_lid_liner.svg', 290, 19)

# Outline
p = d.turtle(('M', 0, 17), **cut)
p.forward(17-r) # left side
p.arc(90, r)
p.forward(290-2*r) # top
p.arc(90, r)
p.forward(19-r) # right side
d.add(p.close())

# Screw holes
d.add(d.circle((6, 5.5), 2.0, **cut))
d.add(d.circle((6+258, 5.5), 2.0, **cut))

d.save()
