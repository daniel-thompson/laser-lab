#
# Generate a shim that can be used to ensure coolant tubing is not
# crushed by the lid of a 9 litre Really Useful Box.
#

from laser.util import *

d = panel('really_useful_wedge.svg', 116, 21)

# Outline
p = Turtle(d.path(('M', 0, 0), **cut))

def groove(p):
    p.move(90, 10)
    p.move(-90, 5)
    p.move(-90, 10)
    p.right(90)

def mousehole(p):
    p.move(90, 6)
    p.arc(-180, 6)
    p.forward(6)
    p.right(90)

p.right(90) # start top edge
p.forward(30)
groove(p) # forward 5
p.forward(46)
groove(p) # forward 5
p.forward(30)

p.move(90, 21)

p.right(90) # start bottom edge
p.forward(15)
mousehole(p) # forward 12
p.forward(25)
mousehole(p) # forward 12
p.forward(25)
mousehole(p) # forward 12
p.forward(15)

d.add(p.close())

d.save()
