# drawpride

Drawing Pride Flags in Python using the drawsvg library.

See examples.ipynb for examples of how to make flags. :)

## Basic drawing
Support for drawing:

Stripes:
* Horizontal lines
* Vertical lines
* Diagonal lines in the style of the Disability Pride Flag
* Reverse diagonal lines like in anarchist flags
* Seychelles-style lines
* Starburst-type patterns
* Concentric bézier curves in the style of the Mental Health Flag
* Concentric infinity symbols in the style of the Autistic Pride Day logo
* Concentric vees in the style of the varsex flag
* Concentric tees in the style of the tgirl/tboy flags
* Concentric rectangles, ellipses, and circles

Rings:
* Standard Carpenter intersex flag ring
* Concentric rings
* Segmented rings
* Insetting a flag inside a Carpenter ring

Piles and other triangles:
* Piles (the triangle that goes on the left-hand side of the Demisexual flag)
* Nested piles (like in the Progress Pride flag)
* Asymmetric piles (like in the tricolour Polyamory flag)
* Inverted triangles like in the Pink Triangle flag
* Ally A (upside-down chevron)
* Inner triangles in the style of the Bissu flag

And other possible flag elements:
* Text (e.g. the original Polyamory flag)
* Crosses (like in the Ipsogender flag)
* X-crosses (like in the Crossdresser flag)
* Squares (like in the Dyadic and Endosex flags)
* Half-squares (cut along diagonal, useful for endosex/dyadic flags)
* Rhombii (squares rotated 45 degrees, used in an Altersex flag)
* Hearts (like in the Biromantic flag)
* The Rubber Zigzag
* BDSM Triskelion
* The Pocketgender Flag
* Closet symbols
* Perisex symbols
* Altersex symbols
* Autism spectrum nautilus symbols
* Métis-style lemniscates
* Equals symbols like in the alternate Androgyne flag

## Examples of use
A Jupyter notebook of examples is available in this directory (examples.ipynb).

Many of the same examples are also available in drawflags/examples.py for even more illustrative examples. Here are just two:
```
intersex_yellow = '#FDD70A'
intersex_purple = '#7A01AA'
trans_pink = '#F5A9B8'
trans_blue = '#5BCEFA'
trans_stripes = [trans_pink, trans_blue, 'white', trans_blue, trans_pink]

d = draw.Drawing(500, 300)
draw_inset_into_intersex(d, trans_stripes, intersex_yellow, intersex_purple, orientation=HORIZONTAL)
d.save_svg(outdir + 'intersextrans.svg')
```
![Intersex-Trans](output/examples/intersextrans.png)

```
d = draw.Drawing(500, 300)
draw_reverse_diagonal_stripes(d, ['#626eb7', '#c7d6ff'])
draw_square(d, 'black')
draw_diagonal_cut_square(d, 'white')
d.save_svg(outdir + 'endosex.svg')
```
![Endosex](output/examples/endosex.png)


## TODOS
Orientation support
- Vees
- Chevrons
- Seychelles
- Concentric Beziers
- Tees
- Square cutting
- Nautilus (beyond vertical/horiz)

Position support
- basically everything right now defaults to putting it in the centre

Colour
- get the colour palette of a flag ordered by volume of flag
- get the colour palette of a flag ordered alphabetically in the style of Wikimedia Commons' flag categorization

Double check
- positioning of the dots in the triskelion