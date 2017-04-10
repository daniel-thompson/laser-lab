#!/usr/bin/env python3

from laser.util import *
import ce96

d = panel('ce96_uart.svg', 161, 138)

d.add(ce96.base(d))
d.add(translate(ce96.top_uart(d), 0, 66))

d.add(rotate(translate(ce96.side(d), 97+64,   0   ),  90))
d.add(rotate(translate(ce96.side(d), 97   ,   0+18), -90))
d.add(rotate(translate(ce96.side(d), 97+64,  20   ),  90))
d.add(rotate(translate(ce96.side(d), 97   ,  20+18), -90))
d.add(rotate(translate(ce96.side(d), 97+64,  40   ),  90))
d.add(rotate(translate(ce96.side(d), 97   ,  40+18), -90))
d.add(rotate(translate(ce96.side(d), 97+64,  60   ),  90))
d.add(rotate(translate(ce96.side(d), 97   ,  60+18), -90))
d.add(rotate(translate(ce96.side(d), 97+64,  80   ),  90))
d.add(rotate(translate(ce96.side(d), 97   ,  80+18), -90))
d.add(rotate(translate(ce96.side(d), 97+64, 100   ),  90))
d.add(rotate(translate(ce96.side(d), 97   , 100+18), -90))
d.add(rotate(translate(ce96.side(d), 97+64, 120   ),  90))
d.add(rotate(translate(ce96.side(d), 97   , 120+18), -90))

d.save()
