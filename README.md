Daniel's Laser Lab
==================

*"What's cooking in the lab?"*

My laser lab is a collection of laser-cut components, cases and artwork
together with python library code that is used to parametrise some of the
designs.

Throughout the lab the functional elements of a design (such as the cuts
needed to make a case for a board) are rendered geometrically in python.
In contrast the artistic elements (e.g. artwork on the top of a case) are
added afterwards, extending the SVG emitted by the python code by drawing
directly on top using [Inkscape](https://inkscape.org). Both the underlying
code and the final machine ready art are included in this repo.

The laser library
-----------------

The laser library is at the heart of almost all the designs here. It is
basically a collection of small extensions to the svgwrite library to
reduce the amount of boiler plate needed to express a design.

The most complex component is the `util.Turtle` which allows an SVG
path to be described using turtle graphics rather than having to express
everything as X-Y coordinates and vectors. I found design elements such
as rounded edges are much easier to express using the turtle.

The other utilities are effectively just time-savers to allow various
SVG transformation operations to be expressed more compactly.

See [laser/](laser/) for the laser library code.

Cases for 96Boards products
---------------------------

Sandwich-style cases are especially well suited as cases for [96Boards 
Consumer Edition][1] and [Iot Edition][2] and, also benefit from being
very easy to manufactures with a laser cutter. Even better both these
96Boards editions have aggressive height limits across the whole board
resulting in an acceptably small number of layers when designing a board
side protection. This results in a simple, robust and easy to handle
enclosure with a simple bolt together design.

![96Boards CE case with UART cut out](https://cdn.rawgit.com/daniel-thompson/laser-lab/364ca4d9/art/96boards_ce_top.svg)

The Consumer boards in particular have lots of connectivity options
making open sided cases (or part open sided) cases desirable. This is also
easily managed by taking care in the design of the sandwich layers.

See [96boards/](96boards/) to see all the available case options for 96Boards
products.

<a data-flickr-embed="true"  href="https://www.flickr.com/photos/daniel-thompson/33198001803/in/datetaken-public/" title="Engraved top board with a cut-out for the 96Boards-uart mezzanine."><img src="https://c1.staticflickr.com/3/2837/33198001803_3347650d15.jpg" width="500" height="375" alt="Engraved top board with a cut-out for the 96Boards-uart mezzanine."></a>

[1]: https://www.96boards.org/products/ce/
[2]: https://www.96boards.org/products/ie/

Miscellaneous parts
-------------------

There is a small selection of components that I have designed to "hack
things better". Many of these are components I used to improve my own
laser cutter.

Most of the parts are explained, on an individual basis, in the comments
at the top of the python file.

See [parts/](parts/) for a complete listing.

Artwork
-------

I cut most of my designs on my home laser cutter and generally do very
short runs (sometimes only one). This means my designs can be free of 
any commercial constraints imposed on laser cutting services. For 
example, many commercial cutting operations end up charging for "laser 
time" which often makes raster engraving (which is typically very slow)
un-economic. In fact even complex raster engraving can end up having a
big impact on the cutting time.

For that reason most of the designs found elsewhere in the lab are primarily
functional. I do add design flourishes, especially rounded corners, but
even these mostly blend function and form (sharp corners *hurt*). Elsewhere
in the lab things are utilitarian and would be suitable for commercial
runs in small(ish) batches.

![96Boards IoT case with redfelineninja artwork](https://cdn.rawgit.com/daniel-thompson/laser-lab/d9de2b67/art/iot96_carbon-art.svg)

The [art/](art/) section is different. In this corner of the lab you can
get a glimpse of the final machine ready artwork that I actually cut.
These are typically copied from other parts of the lab and then hand
edited in Inkscape to add the artistic flourishes that make the designs
come alive.

<a data-flickr-embed="true"  href="https://www.flickr.com/photos/daniel-thompson/32864214633/in/datetaken-public/" title="Laser cut acrylic case for 96Boards IoT edition"><img src="https://c1.staticflickr.com/3/2909/32864214633_e80d6c8ccb.jpg" width="500" height="378" alt="Laser cut acrylic case for 96Boards IoT edition"></a>

Note: Whilst the lab as a whole is licensed under CC BY 4.0 the art
section makes extensive use of Openclipart. The underlying clipart is
dedicated to the public domain (CC0) by its authors and can be freely
downloaded from https://openclipart.org .

License
-------

My laser lab is licensed under [CC BY 4.0](LICENSE.md).
