#!/usr/bin/env python3

from laser.util import *
import iot96

d = panel('iot96_carbon.svg', 300, 200)
d.add(iot96.base(d, 3))
d.add(translate(iot96.top(d, 3), 0, 38))
d.add(rotate(translate(iot96.side(d, 3), 0, 76+66), -90))
d.add(rotate(translate(iot96.side(d, 3), 0+12, 76+66+12), -90))
d.add(rotate(translate(iot96.side(d, 3), 0+24, 76+66+24), -90))
d.add(rotate(translate(iot96.pillar(d, 3), 0+36-7, 76+36+10), -90))
d.add(rotate(translate(iot96.pillar(d, 3), 0+36-7, 76+36+10+12), -90))
d.add(rotate(translate(iot96.pillar(d, 3), 0+36-7, 76+36+10+24), -90))

d.save()
