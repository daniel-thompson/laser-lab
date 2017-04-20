#
# Extension beam for the K40 Y-axis micro-switch
#
# The K40 laser cutter, somewhat notoriously, has a smoke vent that
# intrudes into the cutting space. Basically it sticks out beyond the
# zero point defined by the micro-switch on the Y-axis. This extension
# beam provides an alternative mount for the stopper which shifts the
# zero point by 25mm and ensures the laser head does not damage the
# smoke vent.
#

from laser.util import *

delta = 25
bar_height = 21.6
hole_to_edge = 6
hole_seperation = (11.6 + 7.6) / 2

H = bar_height + delta
W = 20
M = 2.5 / 2

d = panel('k40_y_axis_shortener.py', W, H)

d.add(d.rect((0, 0), (W, H), **cut))
d.add(d.circle((W/2 - hole_seperation/2, bar_height - hole_to_edge), M, **cut))
d.add(d.circle((W/2 + hole_seperation/2, bar_height - hole_to_edge), M, **cut))
d.add(d.circle((W/2 - hole_seperation/2, H - hole_to_edge), M, **cut))
d.add(d.circle((W/2 + hole_seperation/2, H - hole_to_edge), M, **cut))

d.save()
