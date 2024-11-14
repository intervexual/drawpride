# drawpride

Drawing Pride Flags in Python using the drawsvg library.

See examples.ipynb for examples of how to make flags. :)

## Basic drawing
Support for drawing:

Stripes:
* Horizontal lines
* Vertical lines
* Diagonal lines in the style of the Disability Pride Flag
* Seychelles-style lines
* Starburst-type lines
* Concentric bezier curves in the style of the Mental Health Flag
* Concentric infinity symbols in the style of the Autistic Pride Day logo
* Concentric vees in the style of the varsex flag
* Concentric tees in the style of the tgirl/tboy flags
* Concentric rectangles, ellipses, and circles

Rings:
* Standard Carpenter intersex flag ring
* Concentric rings
* Segmented rings
* Insetting a flag inside a Carpenter ring

And other possible flag elements:
* Text (e.g. the original polyamory flag)
* Piles (the triangle that goes on the left-hand side of the Demisexual flag)
* Nested piles (like in the Progress Pride flag)
* Crosses
* Squares
* Half-squares (cut along diagonal, useful for endosex/dyadic flags)
* Rhombii (squares rotated 45 degrees)
* Hearts
* Inverted triangles like in the Pink Triangle flag
* The Rubber Zigzag
* BDSM Triskelion
* The Pocketgender Hourglass
* Ally A/chevron
* Closet symbols
* Perisex symbols
* Altersex symbols
* Autism spectrum nautilus symbols
* Inner triangles in the style of the Bissu flag
* Métis-style lemniscates

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