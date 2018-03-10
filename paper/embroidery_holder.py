#
# Tri-fold greeting card that can be used to mount embroidery.
#
# The embroidery is sandwiched between the centre and right sections
# and can be held in place with glue or tape.
#

from laser.util import *

X = 0
Y = 1
A4 = (297, 210)

# Removing 20mm makes it easier to locate on an A4 sheet
W = A4[X]-20
# This is the width of the card (the effect of the + (2/3) is to make the
# fold over section 2mm narrower than the rest of the card).
S = (W / 3) + (2/3)
B = 15
# H is calculated so as to make the aperture exactly square
H = S + B

d = panel('embroidary_holder.svg', W, H)

d.add(d.rect((S+B, B), (S-2*B, H-3*B), B/2, B/2, **cut))
d.add(d.line((S, 0), (S, H), **engrave))
d.add(d.line((2*S, 0), (2*S, H), **engrave))

# Like rect but with rounded corners to highlight each fold
#d.add(d.rect((0, 0), (W, H), **cut))
p = d.turtle(('M', 0, B/2), **cut)
p.arc(90, B/2)
p.forward(S-B)
p.arc(90, B/2)
p.right(180)
p.arc(90, B/2)
p.forward(S-B)
p.arc(90, B/2)
p.right(180)
p.arc(90, B/2)
p.forward(S-B-2)
p.arc(90, B/2)
p.forward(H-B)
p.arc(90,B/2)
p.forward(S-B-2)
p.arc(90, B/2)
p.right(180)
p.arc(90, B/2)
p.forward(S-B)
p.arc(90, B/2)
p.right(180)
p.arc(90, B/2)
p.forward(S-B)
p.arc(90, B/2)
d.add(p.close())

d.save()
