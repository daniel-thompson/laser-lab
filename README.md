Daniel's Laser Lab
==================

*"What's cooking in the lab?"*

My laser lab is a collection of laser-cut components, cases and artwork
together with python library code that is used to parametrise some of the
designs.

Laser cutters can be used both to cut and engrave. Throughout the lab
the functional elements of a design (such as the cuts needed to make a
case for a board) are rendered geometrically in python, whilst the artistic
elements (e.g. artwork on the top of a case) are added afterwards,
extending the SVG output by the python code by drawing directly on top
using [Inkscape](https://inkscape.org). Both the underlying code and the
final machine ready art are included in this repo.

The laser library
-----------------

The laser library is at the heart of almost all the designs here. It is
basically a collection of small extensions to the svgwrite library to
reduce the amount of boiler plate needed to express a design.

The most complex component is the `util.Turtle` which allows an SVG
path to be described using turtle graphics rather than have to express
everything as X-Y coordinates and vectors. I found design elements such
as rounded edges are much easier to express using the turtle.

The other utilities are effectively just time-savers to allow various
SVG operations to be expressed more compactly.

See [laser/](laser/) for the laser library code.

Cases for 96Boards products
---------------------------

Sandwich-style cases, because they are extremely easy to manufacture 
with a laser cutter, are especially well suited as cases for [96Boards 
Consumer Edition][1] and [Iot Edition][2]. Both editions have strong 
height limits across the whole board resulting in an acceptably small 
number of layers, and resulting in a simple bolt together design.

The Consumer boards in particular have lots of connectivity options
making open side cases, possibly with a sandwich design an attractive
option.

See [96boards/](96boards/) to see all the available case options for 96Boards
products.

[1]: https://www.96boards.org/products/ce/
[2]: https://www.96boards.org/products/ie/

Miscellaneous parts
-------------------

There is a small selection of components that I have designed to "hack
something better". Many of these are components I used to improve my own
laser cutter.

Most of the parts are explained, on an individual basis, in the comments
at the top of the python file.

See [parts/](parts/) for a complete listing.

Artwork
-------

I cut most of my designs on my home laser cutter and generally do very
short runs (sometimes only one). This means my designs can be free of 
any commercial constraints imposes on (or by) laser cutting services. For 
example, many commercial cutting operations end up charging for "laser 
time". This normally makes raster engraving un-economic. In fact even 
complex raster engraving can end up having a big impact on the cutting time.

For that reason most of the designs in the rest of the lab are primarily
functional. I do add design flourishes, especially rounded corners, but
even these mostly blend function and form (sharp corners *hurt**). This
makes them suitable for commercial batch runs where applicable.

In the [art/](art/) section of the lab you can get a glimpse of the final machine
ready artwork that I actually cut. These are typically copied from 
other parts of the lab and then hand edited in Inkscape to add the 
artistic flourishes that make the designs come alive.

Note: Whilst the lab as a whole is licensed under CC BY 4.0 the art
section makes extensive use of Openclipart. The underlying clipart is
dedicated to the public domain (CC0) by its authors and can be freely
downloaded from https://openclipart.org .
