from laser.util import *


d = panel('k40_lid_washer.svg', 10, 21)

d.add(d.washer((5, 5), 5/2, 9.5/2, cut_width=0, **cut))
d.add(d.washer((5, 16), 5/2, 9.5/2, cut_width=0, **cut))

d.save()
