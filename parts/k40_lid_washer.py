from laser.util import *


d = panel('k40_lid_washer.svg', 10, 21)

def washer(d, x, y):
    d.add(d.circle((x, y), 5/2, **cut))
    d.add(d.circle((x, y), 9.5/2, **cut))
bind_method(d, washer)

d.washer(5, 5)
d.washer(5, 16)

d.save()
