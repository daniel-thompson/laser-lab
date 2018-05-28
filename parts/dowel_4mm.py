#
# Create rectangular "dowels" from 4mm ply.
#

from laser.util import *

l = 100
w = 3.9
n = 6

# These must be tuned for the optics on your cutter... on my
# K40 these settings produce *tight* dowels (we need a hammer
# to move the dowel if we have >4 sheets to join)
cut_width_top = 0.2
cut_width_bottom = 0.4

# The dowels are drawn with a tiny gap between the horizontal and
# vertical lines. This convinces (some) routing algorithms to cut
# *all* the horizontal lines first and the vertical lines second.
# This should be as small as possible, and must be smaller than the
# cut width of your machine otherwise the dowels won't be fully
# cut out.
force_cut_order = 0.1

W = w + cut_width_top
d = panel('dowel_4mm.svg', l, n*W)

W = w + cut_width_top
for y in range(1, n):
    d.add(d.line((force_cut_order, W*y), (l-2*force_cut_order, W*y), **cut))
d.add(d.rect((0, 0), (l, n*W), **cut))

W = w - cut_width_top
T = cut_width_top - cut_width_bottom

d.add(rotate(translate(d.trapez((0, 0), (W, W), T/2, T/2, **cut), -2*w, -2*w), 45))

d.save()
