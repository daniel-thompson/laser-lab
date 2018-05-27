#
# Simple window to display 6x4 photos (with a boarder) in a 7x5 frame.
#

from laser.util import *

IN_TO_MM = 25.4

d = panel('7x5_to_6x4.svg', 2 + 7*IN_TO_MM, 2 + 5*IN_TO_MM)

d.add(d.rect((1, 1), (7*IN_TO_MM, 5*IN_TO_MM), **cut))
d.add(d.rect((1+0.5*IN_TO_MM, 1+0.5*IN_TO_MM), (6*IN_TO_MM, 4*IN_TO_MM), **cut))

d.save()
