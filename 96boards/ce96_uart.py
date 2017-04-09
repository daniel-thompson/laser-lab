#!/usr/bin/env python3

from laser.util import *
import ce96

d = panel('ce96_uart.svg', 300, 200)
d.add(ce96.base(d))
d.add(translate(ce96.top_uart(d), 0, 66))
d.add(translate(ce96.side(d), 0, 132))
d.save()
