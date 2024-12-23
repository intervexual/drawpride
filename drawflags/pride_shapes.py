"""
Draw shapes that are neither lines nor rings.

draw_square is unlike the others in this file

"""
import drawsvg

from stars_and_hearts import *


def draw_text(d, text_to_add, primary_colour, secondary_colour='none', name='ch',
              wid=UNSPECIFIED, hei=UNSPECIFIED, x_start=0, y_start=0,
              size_ratio = 1.0, stretch_ratio=1.0, thick_ratio=1.0, orientation=HORIZONTAL):
    """
    Add text to the flag
    :param d: Drawing object
    :param primary_colour: the colour of the text
    :param text_to_add: str text to be added to centre of flag
    :param wid: width that makes up the area that is being drawn into (in pixels)
    :param hei: height that makes up the area that is being drawn into (in pixels)
    :param size_ratio: scaling factor
    :return: none
    >>> d = draw.Drawing(500, 300)
    >>> draw_text(d, RAINBOW[0], 'hi')
    >>> len(d.elements) == 1 and d.elements[-1].args['fill'] == RAINBOW[0]
    True
    >>> type(d.elements[0])
    <class 'drawsvg.elements.Text'>
    """
    if type(primary_colour) == list:
        primary_colour = primary_colour[0]
    wid, hei = get_effective_dimensions(d, wid, hei)
    textsize = size_ratio*(hei/3)
    y_coord = (hei/2) + (textsize/5) + y_start
    d.append(draw.Text(text_to_add, textsize, wid / 2, y_coord, fill=primary_colour,
                       text_anchor='middle', dominant_baseline='middle', font_family='Times New Roman'))  # 8pt text at (-10, -35)


def draw_side_bump(d, primary_colour, secondary_colour='none',
              wid=UNSPECIFIED, hei=UNSPECIFIED, x_start=0, y_start=0,
              size_ratio = 1.0, stretch_ratio=1.0, thick_ratio=1.0, orientation=HORIZONTAL):
    """
    Add a bump to the left side of a flag like in the perioriented flag
    :param d: Drawing object
    :param primary_colour: fill of the bump (str hex code)
    :param secondary_colour: outline of the bump (str hex code)
    :param wid: width of the area we are working with
    :param hei: height of the area we are working with
    :param size_ratio: used to scale the size (width) of the pile
    :param stretch_ratio: scaling factor used to affect concavity
    :return: none
    """
    wid, hei = get_effective_dimensions(d, wid, hei)

    x_dist = ((wid/3) * size_ratio)+x_start # a third of the width by default

    leftmost = x_start
    bar_width = wid*0.265
    left_bump = leftmost + bar_width
    topmost = y_start
    rightmost = left_bump + 0.92*bar_width
    bottommost = topmost+hei
    cy = topmost + 0.175*hei*stretch_ratio
    p = draw.Path(fill=primary_colour, stroke=secondary_colour)
    p.M(leftmost, topmost)
    p.L(left_bump, topmost)
    p.C(rightmost, topmost+cy, rightmost, bottommost-cy, left_bump, bottommost)
    p.L(left_bump, bottommost)
    p.L(leftmost, bottommost).L(leftmost, topmost)
    p.Z()
    d.append(p)


def draw_pile(d, primary_colour, secondary_colour='none',
              wid=UNSPECIFIED, hei=UNSPECIFIED, x_start=0, y_start=0,
              size_ratio = 1.0, stretch_ratio=1.0, thick_ratio=1.0, orientation=HORIZONTAL):
    """
    Add a triangle to the left side like in the demisexual flag
    (it's called a pile: https://en.wikipedia.org/wiki/Glossary_of_vexillology )
    :param d: Drawing object
    :param primary_colour: fill of the pile (str hex code)
    :param secondary_colour: outline of the pile (str hex code)
    :param wid: width of the area we are working with
    :param hei: height of the area we are working with
    :param size_ratio: used to scale the size (width) of the pile
    :return: none
    >>> d = draw.Drawing(500, 300)
    >>> draw_pile(d, RAINBOW[0])
    >>> len(d.elements) == 1 and d.elements[-1].args['fill'] == RAINBOW[0]
    True
    >>> type(d.elements[0])
    <class 'drawsvg.elements.Path'>
    """
    wid, hei = get_effective_dimensions(d, wid, hei)

    x_dist = ((wid/3) * size_ratio)+x_start # a third of the width by default

    leftmost = x_start
    topmost = 0
    p = draw.Path(fill=primary_colour, stroke=secondary_colour)
    p.M(leftmost, topmost)
    p.L(x_dist, hei / 2)
    p.L(leftmost, hei)
    p.L(leftmost, topmost).Z()
    d.append(p)




def draw_corners(d, primary_colour, secondary_colour='none',
              wid=UNSPECIFIED, hei=UNSPECIFIED, x_start=0, y_start=0,
              size_ratio = 1.0, stretch_ratio=1.0, thick_ratio=1.0, orientation=HORIZONTAL):
    """
    Add diagonal corners in the style of the disability pride flag
    :param d: Drawing object
    :param primary_colour: fill of the corners (str hex code)
    :param wid: width of the area we are working with
    :param hei: height of the area we are working with
    :param size_ratio: used to scale the size of the added corners
    :return: none
    >>> d = draw.Drawing(500, 300)
    >>> draw_corners(d, RAINBOW[0])
    >>> len(d.elements) == 2 and d.elements[-1].args['fill'] == RAINBOW[0]
    True
    >>> type(d.elements[0])
    <class 'drawsvg.elements.Path'>
    """
    wid, hei = get_effective_dimensions(d, wid, hei)

    # bottom left
    p = draw.Path(fill=primary_colour, stroke=primary_colour)

    upper_height = (1/3)*hei*size_ratio
    lefter_width = (1/3)*wid*size_ratio
    p.M(0, hei).L(0, upper_height).L(wid-lefter_width, hei).Z()
    d.append(p)

    # upper right
    p = draw.Path(fill=primary_colour)
    p.M(wid, 0).L(wid, hei-upper_height).L(lefter_width, 0).Z()
    d.append(p)



def draw_topbottom(d, primary_colour, secondary_colour='none',
              wid=UNSPECIFIED, hei=UNSPECIFIED, x_start=0, y_start=0,
              size_ratio = 1.0, stretch_ratio=1.0, thick_ratio=1.0, orientation=HORIZONTAL):
    """
    Add stripes to top and bottom. Used for mashup flags.
    :param d: Drawing object
    :param primary_colour: fill colour
    :param wid: width of the area we are working with
    :param hei: height of the area we are working with
    :param size_ratio: scaling factor
    :return: none
    >>> d = draw.Drawing(500, 300)
    >>> draw_topbottom(d, RAINBOW[0])
    >>> len(d.elements) == 2 and d.elements[-1].args['fill'] == RAINBOW[0]
    True
    >>> type(d.elements[0])
    <class 'drawsvg.elements.Path'>
    """
    wid, hei = get_effective_dimensions(d, wid, hei)

    # bottom left
    p = draw.Path(fill=primary_colour, stroke=primary_colour)
    upper_height = (1/3)*hei*size_ratio

    # top
    p.M(0, 0).L(0, upper_height).L(wid, upper_height).L(wid, 0).L(0,0).Z()
    d.append(p)

    # bottom
    p = draw.Path(fill=primary_colour)
    p.M(0, hei).L(0, hei-upper_height).L(wid, hei-upper_height).L(wid, hei).L(0,hei).Z()
    d.append(p)


def draw_perisex(d, primary_colour, secondary_colour='none',
              wid=UNSPECIFIED, hei=UNSPECIFIED, x_start=0, y_start=0,
              size_ratio = 1.0, stretch_ratio=1.0, thick_ratio=1.0, orientation=HORIZONTAL):
    """
    Draws an abstract scale/balance thing with f and m ends
    :param d: drawing image
    :param primary_colour: colour of the lines
    :param wid: width of the area we are working with
    :param hei: height of the area we are working with
    :param size_ratio: size scaling
    :return: none
    >>> d = draw.Drawing(500, 300)
    >>> draw_perisex(d, RAINBOW[0])
    >>> len(d.elements) == 6 and d.elements[-1].args['stroke'] == RAINBOW[0]
    True
    >>> type(d.elements[0])
    <class 'drawsvg.elements.Line'>
    """
    wid, hei = get_effective_dimensions(d, wid, hei)
    sw = (hei / 24) * size_ratio
    down = (hei / 3) * size_ratio

    h = (hei / 2) - down / 2
    l = wid * (1 / 3) * (1 / size_ratio)  # left side of line
    r = wid - l  # right side, symmetry
    arm = down / 3
    arm_x = h + down - arm
    hangar = down / 3

    fudge = sw
    fem_end = arm_x  # -1.5*fudge
    d.append(draw.Line(l, h, r, h, stroke=primary_colour, stroke_width=sw, stroke_linecap='round'))
    d.append(draw.Line(l, h, l, fem_end, stroke=primary_colour, stroke_width=sw, stroke_linecap='round'))
    d.append(draw.Line(r, h, r, h + down, stroke=primary_colour, stroke_width=sw, stroke_linecap='round'))

    # fem
    # d.append(draw.Line(l-arm, arm_x, l+arm, arm_x, stroke=fill, stroke_width=sw, stroke_linecap='round'))
    p = draw.Path(stroke=primary_colour, stroke_width=sw, fill=primary_colour, stroke_linecap='round')
    arm_low = h + down + (fudge / 4)
    f_arm = arm * 1.5
    arm_m = arm_x

    fudge = sw/3
    p.M(l-arm, h+down+fudge).L(l, arm_m).L(l+arm, h+down+fudge).Z()
    #p.M(l-arm, arm_m).L(l, h+down).L(l+arm, arm_m).Z()

    d.append(p)
    # masc
    p = draw.Path(stroke=primary_colour, stroke_width=sw, fill=primary_colour, stroke_linecap='round')
    p.M(r - arm, arm_m).L(r, h + down).L(r + arm, arm_m).Z()
    d.append(p)

    # start
    d.append(draw.Line(wid / 2, h, wid / 2, h - hangar, stroke=primary_colour, stroke_width=sw, stroke_linecap='round'))


def draw_rhombus(d, primary_colour, secondary_colour='none',
              wid=UNSPECIFIED, hei=UNSPECIFIED, x_start=0, y_start=0,
              size_ratio = 1.0, stretch_ratio=1.0, thick_ratio=1.0, orientation=HORIZONTAL):
    """
    Draw a square on a diagonal
    :param d: Drawing object
    :param primary_colour: the colour to fill the rhombus with
    :param secondary_colour: outline colour of rhombus
    :param wid: width of the area we are working with
    :param hei: height of the area we are working with
    :param size_ratio: size factor (radius)
    :param stretch_ratio: horizontal stretching to make diamonds
    :param thick_ratio: scaling factor for the stroke width of the outline
    :return: none
    >>> d = draw.Drawing(500, 300)
    >>> draw_rhombus(d, RAINBOW[0])
    >>> len(d.elements) == 1 and d.elements[-1].args['stroke'] == RAINBOW[0]
    True
    >>> type(d.elements[0])
    <class 'drawsvg.elements.Path'>
    """
    wid, hei = get_effective_dimensions(d, wid, hei)
    sw = thick_ratio* hei / 10
    p = draw.Path(stroke=secondary_colour, stroke_width=sw, fill=primary_colour)
    radius_perc = 0.25 # by default have it take up 1/4 of the height
    y_radius = hei * radius_perc * size_ratio
    x_radius = y_radius*stretch_ratio
    mx, my = wid/2, hei/2
    p.M(mx, my-y_radius)
    p.L(mx+x_radius, my)
    p.L(mx, my+y_radius)
    p.L(mx-x_radius, my).Z()
    d.append(p)


def draw_square(d, primary_colour, secondary_colour='none',
              wid=UNSPECIFIED, hei=UNSPECIFIED, x_start=0, y_start=0,
              size_ratio = 1.0, stretch_ratio=1.0, thick_ratio=1.0, orientation=HORIZONTAL):
    """Draw a square in the style of the dyadic/endosex flag.
    :param d: Drawing object
    :param primary_colour: outline colour of the square
    :param secondary_colour: fill colour of the square
    :param wid: width of the area we are working with
    :param hei: height of the area we are working with
    :param x_start: the x-coordinate of the upper left corner of the rectangular area that is being drawn into
    :param y_start: the y-coordinate of the upper left corner of the rectangular area that is being drawn into
    :param size_ratio: size factor
    :return: height of the square
    >>> d = draw.Drawing(500, 300)
    >>> draw_square(d, RAINBOW[0])
    >>> len(d.elements) == 1 and d.elements[-1].args['stroke'] == RAINBOW[0]
    True
    >>> type(d.elements[0])
    <class 'drawsvg.elements.Path'>
    """
    wid, hei = get_effective_dimensions(d, wid, hei)
    sw = hei / 10
    p = draw.Path(stroke=primary_colour, stroke_width=sw, fill=secondary_colour)
    radius = hei * 0.5 * size_ratio # half the height by default
    p.M((wid/2)-radius/2, (hei/2)-radius/2)
    p.L((wid/2)+radius/2, (hei/2)-radius/2)
    p.L((wid/2)+radius/2, (hei/2)+radius/2)
    p.L((wid/2)-radius/2, (hei/2)+radius/2).Z()
    d.append(p)
    return radius + sw


def draw_diagonal_cut_square(d, primary_colour, secondary_colour='none',
              wid=UNSPECIFIED, hei=UNSPECIFIED, x_start=0, y_start=0,
              size_ratio = 1.0, stretch_ratio=1.0, thick_ratio=1.0, orientation=HORIZONTAL):
    """Draw half of a square that is cut diagonally, to be superimposed with draw_square
    to produce dyadic/endosex flags.
    :param d: Drawing object
    :param primary_colour: the colour of the half-square
    :param wid: width of the area we are working with
    :param hei: height of the area we are working with
    :param size_ratio: size factor
    :return: none
    >>> d = draw.Drawing(500, 300)
    >>> draw_diagonal_cut_square(d, RAINBOW[0])
    >>> len(d.elements) == 1 and d.elements[-1].args['stroke'] == RAINBOW[0]
    True
    >>> type(d.elements[0])
    <class 'drawsvg.elements.Path'>
    """
    bg_colours = ('none', 'none')
    wid, hei = get_effective_dimensions(d, wid, hei)
    radius = hei * 0.5 * size_ratio # half the height by default

    x_offset, y_offset = 0, 0

    stripe_width = (2 * wid) / (len(bg_colours))
    offset = 0 #offset * len(bg_colours) / 10

    for i, c in enumerate(bg_colours[:1]):
        up_left = 0 + math.floor(i * stripe_width) + x_offset
        up_right = up_left + math.ceil(stripe_width + offset)
        up_y = 0 + y_offset

        down_y = hei + y_offset
        down_left = -wid + math.floor(i * stripe_width) + x_offset
        down_right = down_left + math.ceil(stripe_width + offset)
        # the -1/+1 offset is to stop streaks from appearing when there are many stripes

        p = draw.Path(fill=primary_colour)  # draw the stripe as a Path with four points
        p.M(up_left, up_y)
        p.L(down_left, down_y).L(down_right, down_y)
        p.L(up_right, up_y).L(up_right, up_y)
        p.Z()

        clip = draw.ClipPath()
        clip.append(p)
        pr = draw.Path(stroke=primary_colour, stroke_width=hei / 10, fill='none', clip_path=clip)
        pr.M((wid / 2) - radius / 2, (hei / 2) - radius / 2)
        pr.L((wid / 2) + radius / 2, (hei / 2) - radius / 2)
        pr.L((wid / 2) + radius / 2, (hei / 2) + radius / 2)
        pr.L((wid / 2) - radius / 2, (hei / 2) + radius / 2).Z()
        d.append(pr)


def draw_bissu(d, primary_colour, secondary_colour='none',
              wid=UNSPECIFIED, hei=UNSPECIFIED, x_start=0, y_start=0,
              size_ratio = 1.0, stretch_ratio=1.0, thick_ratio=1.0, orientation=HORIZONTAL):
    """
    Draw triangles in the style of the Bissu flag
    :param d: Drawing ojbect
    :param primary_colour: colour of the left triangle
    :param secondary_colour: colour of the right triangle
    :param wid: width of the area we are working with
    :param hei: height of the area we are working with
    :return: none
    """
    wid, hei = get_effective_dimensions(d, wid, hei)
    p = draw.Path(fill=primary_colour)
    mh = hei/2
    mw = wid/2
    p.M(x_start, mh).L(mw, y_start).L(mw, hei).Z()
    d.append(p)
    p = draw.Path(fill=secondary_colour)
    p.M(wid, mh).L(mw, y_start).L(mw, hei).Z()
    d.append(p)


def draw_altersex_symbol(d, primary_colour, secondary_colour='none',
              wid=UNSPECIFIED, hei=UNSPECIFIED, x_start=0, y_start=0,
              size_ratio = 1.0, stretch_ratio=1.0, thick_ratio=1.0, orientation=HORIZONTAL):
    '''
    Draw a triangle with a ring
    :param d: Drawing object
    :param primary_colour: colour (string) of the outline of the symbol
    :param secondary_colour: fill colour (string) of the symbol
    :param wid: width of the area we are working with
    :param hei: height of the area we are working with
    :param size_ratio: size factor
    :param thick_ratio: scaling factor for the outline's stroke width
    :return: none
    >>> d = draw.Drawing(500, 300)
    >>> draw_altersex_symbol(d, RAINBOW[0], RAINBOW[1])
    >>> len(d.elements) == 4 and d.elements[-1].args['stroke'] == RAINBOW[1]
    True
    >>> type(d.elements[0])
    <class 'drawsvg.elements.Circle'>
    '''
    wid, hei = get_effective_dimensions(d, wid, hei)
    radius = size_ratio * hei / 6.9 # 6.9 for lower align, 6 originally
    sw = thick_ratio*radius/4 # started with /4
    x_mid = wid/2

    # triangle measurements
    triangle_height = 3*radius
    tri_base = (radius*3)/2

    total_height = (radius)*2 - sw/2 # circle
    total_height += triangle_height

    # triangle coordinates
    y_top = (hei/2) - (total_height/2)
    y_base = y_top + triangle_height
    # ring coordinate
    y_coord = y_base+radius-sw  #(hei/2) + 2*radius - 0.5*radius

    # draw outer then inner rings
    d.append(draw.Circle(x_mid, y_coord, radius + sw, fill='none', stroke=primary_colour, stroke_width=sw))
    d.append(draw.Circle(x_mid, y_coord, radius - sw, fill='none', stroke=primary_colour, stroke_width=sw))

    # draw triangle
    p = draw.Path(fill=secondary_colour, stroke=primary_colour, stroke_width=sw)
    p.M(x_mid, y_top)
    p.L(x_mid+tri_base, y_base).L(x_mid-tri_base, y_base).L(x_mid, y_top).Z()
    d.append(p)

    # middle ring
    d.append(draw.Circle(x_mid, y_coord, radius, fill='none', stroke=secondary_colour, stroke_width=sw))


def draw_cross(d, primary_colour, secondary_colour='none',
              wid=UNSPECIFIED, hei=UNSPECIFIED, x_start=0, y_start=0,
              size_ratio = 1.0, stretch_ratio=1.0, thick_ratio=1.0, orientation=HORIZONTAL):
    """
    Draw a cross that is, by default, the right size to produce the ipsogender flag
    when combined with a Carpenter ring.
    :param d: drawing object
    :param primary_colour: fill of the cross
    :param wid: width of area the symbol is being added to
    :param hei: height of the area the symbol is being added to
    :param size_ratio: scaling factor for radius
    :param thick_ratio: scaling factor for line width
    :param stretch_ratio: scaling factor that affects how symmetric the cross is
    :return: none
    """
    wid, hei = get_effective_dimensions(d, wid, hei)
    midx = (wid/2) + x_start
    midy = (hei/2) + y_start

    # vertical bar
    intop = top_of_ring(hei)
    inbot = base_of_ring(hei)
    thickness = ring_thickness(hei)*size_ratio*thick_ratio
    line_height = (inbot - intop)*size_ratio
    d.append(
        draw.Rectangle(midx - (thickness / 2), midy - (line_height*0.5), thickness, line_height, fill=primary_colour))

    # horizontal bar
    line_width = line_height*stretch_ratio
    d.append(
        draw.Rectangle(midx - line_width / 2, midy - (thickness*0.5), line_width, thickness, fill=primary_colour))


def draw_metis_lemniscate(d, primary_colour, secondary_colour='none',
              wid=UNSPECIFIED, hei=UNSPECIFIED, x_start=0, y_start=0,
              size_ratio = 1.0, stretch_ratio=1.0, thick_ratio=1.0, orientation=HORIZONTAL):
    """
    Draw an infinity symbol (lemniscate) in the style of the Métis flag.
    :param d: drawing object
    :param primary_colour: fill of the infinity symbol
    :param wid: width of area the symbol is being added to
    :param hei: height of the area the symbol is being added to
    :param size_ratio: scaling factor (radius-equivalent)
    :param stretch_ratio: how round vs spiky it is. Low value is more like a ⋈ shape
    :param thick_ratio: how thick the infinity is. Default is based on Métis flag.
    :return: none
    """
    wid, hei = get_effective_dimensions(d, wid, hei)
    stroke_wid = (24/300)*hei*thick_ratio
    p = draw.Path(stroke=primary_colour, fill='none', stroke_width=stroke_wid)

    horiz_stretch = 0.15*stretch_ratio

    later_x = (110/400)*wid # 110
    start_x = wid - later_x # 290

    cx_diff = (72/400)*wid # 72
    control_x1 = later_x+cx_diff #182
    control_x2 = start_x-cx_diff #218

    upper_height = (97/300)*hei # 97
    lower_height = hei - upper_height # 203

    arcradius_x =  horiz_stretch*wid # 60 - this is how horiz stretched out the C shape will be
    arcradius_y = (lower_height-upper_height)/2  #(53/300)*hei # 53 - middle between top and bottom of the C shape

    p.M(start_x, lower_height)
    p.A(arcradius_x, arcradius_y, 0, 0, 0, start_x, upper_height) # right )
    p.C(control_x2, upper_height, control_x1, lower_height, later_x, lower_height) # upper right to lower left
    p.A(arcradius_x, arcradius_y, 0, 0, 1, later_x, upper_height) # left (
    p.C(control_x1, upper_height, control_x2, lower_height, start_x, lower_height).Z()
    d.append(p)




def single_nautilus_segment(d, wid, hei, arr, primary_colour, step_size, border_width=0.0, border_colour ='black'):
    """
    Helper function for draw_nautilus. Draws a single segment.
    :param d: Drawing object
    :param wid: width of area the entire nautilus is being drawn into
    :param hei: height of the area the entire nautilus is being drawn into
    :param arr: array of coordinates
    :param primary_colour: colour to fill the nautilus segment with
    :param step_size: the "width" of the segment
    :param border_width: width in pixels of the border
    :param border_colour:
    :return:
    """
    mx = step_size + wid / 2
    my = 2*step_size + hei / 2

    p = draw.Path(stroke=border_colour, fill=primary_colour, stroke_width=border_width)
    d.append(p.M(mx, my))
    d.append(p.L(mx+arr[0], my+arr[1]))
    d.append(p.Q(mx+arr[2], my+arr[3], mx+arr[4], my+arr[5]))
    d.append(p.L(mx, my))
    d.append(p.Z())


def draw_nautilus(d, colours,
              wid=UNSPECIFIED, hei=UNSPECIFIED, x_start=0, y_start=0,
              size_ratio = 1.0, stretch_ratio=1.0, thick_ratio=1.0, orientation=HORIZONTAL,
              border_colour='black', border_size=0):
    """
    Draw an autistic spectrum nautilus symbol
    :param d: Drawing object
    :param colours: the colours of the segments, first one will be the largest
    :param wid: width of area the symbol is being added to
    :param hei: height of the area the symbol is being added to
    :param size_ratio: scaling factor
    :param is_horizontal: vertical or horizontal?
    :return: none
    """
    is_horizontal = orientation == HORIZONTAL
    wid, hei = get_effective_dimensions(d, wid, hei)
    height_perc = (120 / 300)*size_ratio
    border_width = 5*size_ratio*border_size
    ang_each = 360 / len(colours)
    coords = []
    a = 0
    start = height_perc*hei#120*height_scale
    step_size = start/12 * 8/len(colours) #10
    l = start
    for i in range(len(colours) + 1):
        x0 = -l * math.sin(math.radians(a))
        y0 = -l * math.sin(math.radians(90 - a))
        coords.append(tuple([x0, y0, a]))
        a += ang_each
        l -= step_size

    controls = []
    l = start
    a = ang_each / 2
    for i, val in enumerate(coords):
        inc = 10*stretch_ratio*size_ratio
        cp_dist = l + inc
        x0 = -(cp_dist) * math.sin(math.radians(a))
        y0 = -(cp_dist) * math.sin(math.radians(90 - a))
        controls.append(tuple([x0, y0]))
        l -= step_size
        a += ang_each

    # draw out each segment
    for i, l in enumerate(colours):
        fill = colours[i]

        x0 = coords[i][0]
        y0 = coords[i][1]
        x1 = coords[i + 1][0]
        y1 = coords[i + 1][1]
        # by default have it vertical
        if is_horizontal:
            trigged = [ y0, x0,  controls[i][1], controls[i][0],  y1, x1]
        else:
            trigged = [x0, y0, controls[i][0], controls[i][1], x1, y1]
        single_nautilus_segment(d, wid, hei, trigged, fill, step_size, border_width=border_width, border_colour=border_colour)


def draw_closet_symbol(d, primary_colour, secondary_colour='none',
              wid=UNSPECIFIED, hei=UNSPECIFIED, x_start=0, y_start=0,
              size_ratio = 1.0, stretch_ratio=1.0, thick_ratio=1.0, orientation=HORIZONTAL):
    """
    Draw a closet symbol, similar in style to the one in isobug's closeted intersex flag
    :param d: Drawing object
    :param primary_colour: colour (string) of the outline of the symbol
    :param secondary_colour: fill colour (string) of the symbol
    :param wid: width of the area we are working with
    :param hei: height of the area we are working with
    :param x_start: the x-coordinate of the upper left corner of the rectangular area that is being drawn into
    :param y_start: the y-coordinate of the upper left corner of the rectangular area that is being drawn into
    :param size_ratio: size factor
    :param stretch_ratio: scaling factor for the width
    :param thick_ratio: scaling factor for the stroke thickness
    :return: none
    """
    wid, hei = get_effective_dimensions(d, wid, hei)
    stroke_width = (hei / 28)*thick_ratio*size_ratio

    # for the outer rectangle
    closet_hei = (hei * (2/3))*size_ratio
    closet_wid = closet_hei * .8 * stretch_ratio
    upper_left = (wid/2) - closet_wid/2
    upper_top = (hei/2) - (closet_hei/2)
    round_radius = closet_hei / 6

    # outer rectangle
    d.append(draw.Rectangle(upper_left + x_start, upper_top + y_start, closet_wid, closet_hei, ry=round_radius,
                            stroke=primary_colour, fill=secondary_colour, stroke_width=stroke_width))

    # inner rectangle
    diff = closet_hei / 10
    d.append(draw.Rectangle(upper_left + diff + x_start, upper_top + diff + y_start, closet_wid - 2 * diff, closet_hei - 2 * diff,
                            ry=round_radius-diff, stroke=primary_colour, fill=secondary_colour, stroke_width=stroke_width))

    # line down the middle
    midx = (wid/2) + x_start
    midy = (hei/2) + y_start
    d.append(draw.Line(midx, upper_top + diff + y_start, midx, upper_top + closet_hei - diff + y_start, stroke=primary_colour, stroke_width=stroke_width))

    # handles
    d.append(draw.Line(midx - diff, midy - diff, midx - diff, midy + diff, stroke=primary_colour, stroke_width=stroke_width))
    d.append(draw.Line(midx + diff, midy - diff, midx + diff, midy + diff, stroke=primary_colour, stroke_width=stroke_width))


def triangle_side_from_hypot(hypot, sidelen):
    """
    Helper function for trigonometry
    :param hypot: hypotenuse of a triangle
    :param sidelen: one of its side lengths
    :return: the other side length
    """
    return math.sqrt(hypot**2 - sidelen**2)


def rubber_helper(line_hei, sw, topln_start_y, topln_start_x, topln_descend_hypot, angle_descent, angle_ascent):
    """
    Helper function for calculating rubber flag lines
    :param line_hei: distance between lines
    :param sw: stroke width
    :param topln_start_y: the y coordinate that the line starts at (the flat line on the left)
    :param topln_start_x: the x coordinate from which the line starts to go downward
    :param topln_descend_hypot: the hypotenuse of the triangle formed from the line going downward
    :param angle_descent: the angle at which the line goes downward (in radians)
    :param angle_ascent: the angle at which the line comes back up (in radians)
    :return: the coordinates needed for the path and the hypotenuse used (is needed for subsequent line calculations)
    """
    midln_start_y = topln_start_y+line_hei
    midln_start_xoffset = line_hei * math.sin(angle_descent)
    midln_start_x = topln_start_x - midln_start_xoffset #229.43057*h # 1925-229.43-> 1695.56943

    # the descent
    midln_descend_hypot = topln_descend_hypot + line_hei/2 - sw/2 # 871.01243
    midln_descend_wid = midln_descend_hypot*math.sin(angle_descent)
    midln_descend_hei = triangle_side_from_hypot(midln_descend_hypot, midln_descend_wid)
    midln_descend_x = midln_start_x + midln_descend_wid
    midln_descend_y = midln_start_y + midln_descend_hei

    # the re-ascending
    midln_ascend_hypot = midln_descend_hei / math.cos(angle_ascent)
    midln_ascend_wid = triangle_side_from_hypot(midln_ascend_hypot, midln_descend_hei) #(1647.0425*w) # 98.5 - 35 degrees
    midln_ascend_x = midln_descend_x + midln_ascend_wid

    return midln_start_x, midln_start_y, midln_descend_x, midln_descend_y, midln_ascend_x, midln_descend_hypot


def draw_rubber_zigzags(d, primary_colour, secondary_colour='none',
              wid=UNSPECIFIED, hei=UNSPECIFIED, x_start=0, y_start=0,
              size_ratio = 1.0, stretch_ratio=1.0, thick_ratio=1.0, orientation=HORIZONTAL):
    """
    Draw zigzag stripes in the style of the rubber pride flag.
    :param d: Drawing object
    :param primary_colour: colour (string) of the outline of the symbol
    :param secondary_colour: fill colour (string) of the symbol
    :param wid: width of the area we are working with
    :param hei: height of the area we are working with
    :param x_start: the x-coordinate of the upper left corner of the rectangular area that is being drawn into
    :param y_start: the y-coordinate of the upper left corner of the rectangular area that is being drawn into
    :param size_ratio: size factor
    :return: line height
    """
    wid, hei = get_effective_dimensions(d, wid, hei)

    OGH = 2250+250/2 # size of the flag I used as reference to make this
    OGW = 4000
    h = hei/OGH
    w = wid/OGW
    sw = 100*h

    p = draw.Path(stroke=primary_colour, fill=secondary_colour, stroke_width=sw)

    topln_start_y = 500*h # this is the flat line height
    # the descent
    angle_descent = math.radians(35)
    topln_start_x = 1925*w
    topln_descend_wid = (2500-1925)*w # 575
    topln_descend_hypot = topln_descend_wid / math.sin(angle_descent) # 471.01243
    topln_descend_hei = triangle_side_from_hypot(topln_descend_hypot, topln_descend_wid) # (821.1851*h) # 35 degrees
    # the actual coordinates that are descended to then ascended to
    topln_descend_x = topln_start_x+topln_descend_wid #2500*w
    topln_descend_y = topln_start_y + topln_descend_hei

    # the re-ascending
    angle_ascent = math.radians(63.5)
    topln_ascend_hypot = topln_descend_hei / math.cos(angle_ascent)
    topln_ascend_wid = triangle_side_from_hypot(topln_ascend_hypot, topln_descend_hei) #(1647.0425*w) # 98.5 - 35 degrees
    topln_ascend_x = topln_descend_x + topln_ascend_wid

    # now calculate the middle and lowest lines
    line_hei = 1000*h - topln_start_y - (sw/2)
    helps = rubber_helper(line_hei, sw, topln_start_y, topln_start_x, topln_descend_hypot, angle_descent, angle_ascent)
    midln_start_x, midln_start_y, midln_descend_x, midln_descend_y, midln_ascend_x, midln_descend_hypot = helps

    helps = rubber_helper(line_hei, sw, midln_start_y, midln_start_x, midln_descend_hypot, angle_descent, angle_ascent)
    lowln_start_x, lowln_start_y, lowln_descend_x, lowln_descend_y, lowln_ascend_x, lowln_descend_hypot = helps

    # top and middle lines are actually one path
    p.M(-sw, topln_start_y)
    p.L(topln_start_x, topln_start_y).L(topln_descend_x, topln_descend_y).L(topln_ascend_x, topln_start_y)
    p.L(midln_ascend_x, midln_start_y).L(midln_descend_x, midln_descend_y).L(midln_start_x, midln_start_y)
    p.L(-sw, midln_start_y).Z()
    d.append(p)

    # bottom line
    p = draw.Path(stroke=primary_colour, stroke_width=sw, fill='none')
    p.M(-sw, lowln_start_y)
    p.L(lowln_start_x, lowln_start_y).L(lowln_descend_x, lowln_descend_y).L(lowln_ascend_x, lowln_start_y)
    d.append(p)
    return line_hei


def draw_refugeeline(d, primary_colour, secondary_colour='none',
              wid=UNSPECIFIED, hei=UNSPECIFIED, x_start=0, y_start=0,
              size_ratio = 1.0, stretch_ratio=1.0, thick_ratio=1.0, orientation=HORIZONTAL):
    """
    Draw a single horizontal line in the style of the refugee flag
    :param d: Drawing object
    :param primary_colour: fill colour (string) of the line
    :param secondary_colour: colour (string) of the outline of the line
    :param wid: width of the area we are working with
    :param hei: height of the area we are working with
    :param x_start: the x-coordinate of the upper left corner of the rectangular area that is being drawn into
    :param y_start: the y-coordinate of the upper left corner of the rectangular area that is being drawn into
    :param size_ratio: size factor
    :return: the top of the line (y coordinate)
    """
    wid, hei = get_effective_dimensions(d, wid, hei)
    '''
    <rect width="800" height="500" fill="#f06942"/>
    <rect width="800" height="65" y="315"/>'''
    top_of_line = hei * (315/500)
    height_of_line = hei * (65/500) * size_ratio
    d.append(draw.Rectangle(x_start, y_start+top_of_line, wid, height_of_line, fill=primary_colour, stroke=secondary_colour))
    return top_of_line


def draw_intersex_ally(d, primary_colour, secondary_colour='none',
              wid=UNSPECIFIED, hei=UNSPECIFIED, x_start=0, y_start=0,
              size_ratio = 1.0, stretch_ratio=1.0, thick_ratio=1.0, orientation=HORIZONTAL):
    """
    Draw a chevron/vee in the style of the ally flag
    :param d: Drawing object
    :param primary_colour: fill colour (string) of the line
    :param secondary_colour: colour (string) of THE INTERSEX RING INSIDE IT
    :param wid: width of the area we are working with
    :param hei: height of the area we are working with
    :param x_start: the x-coordinate of the upper left corner of the rectangular area that is being drawn into
    :param y_start: the y-coordinate of the upper left corner of the rectangular area that is being drawn into
    :param size_ratio: size factor
    :return: radius for maximum incircle
    """
    wid, hei = get_effective_dimensions(d, wid, hei)
    midx =wid/2

    awidth = wid / 3
    inner_right = x_start + wid - awidth
    inner_left = inner_right - awidth
    lower_height = 2*hei/3

    p = draw.Path(fill=primary_colour) #, stroke=secondary_colour)
    p.M(x_start, hei) # bottom left
    p.L(x_start + midx, y_start) # top of A
    p.L(x_start + wid, hei) # bottom right
    p.L(inner_right, hei) # loop back
    p.L(x_start + midx, lower_height)
    p.L(inner_left, hei)
    d.append(p)

    # for calculating where to put an intersex ring
    # create an upper isosceles triangle from the armpit of the ^ upwards
    asprat = hei/wid
    upper_tri_hei = lower_height
    upper_tri_wid = upper_tri_hei / asprat

    r = (upper_tri_wid*upper_tri_hei) / ((upper_tri_wid+math.sqrt(upper_tri_wid**2 + 4*upper_tri_hei**2)))

    incircle_y = lower_height - r
    d.append(draw.Circle(x_start + midx, incircle_y, r*0.8, fill='none',
                         stroke=secondary_colour, stroke_width=r/7))
    return r


def draw_pocketgender_hourglass(d, colours,
              wid=UNSPECIFIED, hei=UNSPECIFIED, x_start=0, y_start=0,
              size_ratio = 1.0, stretch_ratio=1.0, thick_ratio=1.0, orientation=HORIZONTAL):
    """
    Draw a straight hourglass type shape seen in the pocket gender flag
    :param d: Drawing object
    :param colours: in order: top fill, middle fill, bottom fill, (optional) stroke colour
    :param wid: width of the area we are working with
    :param hei: height of the area we are working with
    :param x_start: the x-coordinate of the upper left corner of the rectangular area that is being drawn into
    :param y_start: the y-coordinate of the upper left corner of the rectangular area that is being drawn into
    :param size_ratio: size factor
    :return: none
    """
    wid, hei = get_effective_dimensions(d, wid, hei)
    strokecolour = 'none'
    if len(colours) > 3:
        strokecolour = colours[3]
    sw = hei/80

    midx = x_start + wid/2
    midy = y_start + hei/2

    bigtri_wid = wid/3
    left = x_start + (wid/2) - (bigtri_wid/2)
    right = x_start + (wid/2) + (bigtri_wid/2)
    top = y_start
    bottom = y_start + hei
    # at first I thought the triangles were equilateral, but they are *not*
    bigtri_hei = (hei/3)+sw #(hei/wid)*(zig_wid/2) # (wid/6)/(bigtri_wid+(wid/6))

    gap = (hei - bigtri_hei*2)/2
    minitri_wid = (gap)*(wid/6)/(hei/3)

    # break it into three paths: top
    p = draw.Path(fill=colours[0], stroke=strokecolour, stroke_width=sw)
    p.M(left, top-sw).L(midx, y_start+bigtri_hei).L(right, top-sw).Z()
    d.append(p)
    # bottom
    p = draw.Path(fill=colours[2], stroke=strokecolour, stroke_width=sw)
    p.M(left, bottom+sw).L(midx, bottom-bigtri_hei).L(right, bottom+sw).Z()
    d.append(p)
    # middle
    p = draw.Path(fill=colours[1], stroke=strokecolour, stroke_width=sw)
    p.M(midx, bottom-bigtri_hei).L(midx+minitri_wid, midy).L(midx, y_start+bigtri_hei).L(midx-minitri_wid, midy).Z()
    d.append(p)


def draw_triskelion(d, colours,
              wid=UNSPECIFIED, hei=UNSPECIFIED, x_start=0, y_start=0,
              size_ratio = 1.0, stretch_ratio=1.0, thick_ratio=1.0, orientation=HORIZONTAL):
    """
    Draw a triskelion symbol used for BDSM fetish flags.
    Based on: https://commons.wikimedia.org/wiki/File:Dotted_triskelion_(fixed_width).svg
    :param d: Drawing object
    :param colours: in order: tracing colour, (optional) fill colour, (optional) dot colour
    :param wid: width of the area we are working with
    :param hei: height of the area we are working with
    :param x_start: the x-coordinate of the upper left corner of the rectangular area that is being drawn into
    :param y_start: the y-coordinate of the upper left corner of the rectangular area that is being drawn into
    :param size_ratio: size factor (radius)
    :param stretch_ratio: scaling factor for the radii of the inner dots
    :param thick_ratio: scaling factor for the stroke width inside the triskelion
    :return: none
    """
    wid, hei = get_effective_dimensions(d, wid, hei)

    #w = wid/3619.2151
    h = size_ratio*hei/3619.2151
    w = h

    x_start += (wid/2) - 1357.0*w
    y_start += (hei/2) - 1366.0*h

    # x coordinates
    x1 = x_start + 1366.0 * w
    x2 = x_start + 507.0 * w
    x3 = x_start + 498.0 * w
    # y coordinates
    y1 = y_start + 71.0 * h # was 77
    y2 = y_start + 71.0 * h # smallest
    y3 = y_start + 1372.0 * h

    # x coordinates
    x6 = x_start + 233.0 * w
    x7 = x_start + 660.0 * w
    x8 = x_start + 1784.0 * w
    x_cent = x_start + 1357.0 * w
    x10 = x_start + 1782.0 * w
    x11 = x_start + 2919.0 * w
    x12 = x_start + 2485.0 * w
    # y coordinates
    y6 = y_start + 2008.0 * h
    y7 = y_start + 2747.0 * h
    y8 = y_start + 2105.0 * h
    y_cent = y_start + 1366.0 * h
    y10 = y_start + 619.0 * h
    y11 = y_start + 1263.0 * h
    y12 = y_start + 2004.0 * h

    sw=thick_ratio*hei/20
    pathcolour = colours[0]
    circlebg = 'none'
    if len(colours) > 1:
        circlebg = colours[1]
    if len(colours) > 2:
        dotcolour = colours[2]
    else:
        dotcolour = pathcolour

    rad = (y_cent - y2) # 1 overshoots and 0.5 undershoots
    d.append(draw.Circle(x_cent, y_cent, rad, stroke_width=sw, fill=circlebg, stroke=pathcolour))

    p = draw.Path(stroke=pathcolour, fill='none', stroke_width=sw)
    p.M(x1, y1) # upper C
    p.C(x2, y2, x3, y3, x_cent, y_cent)
    p.M(x6, y6) # the two lower C shapes
    p.C(x7, y7, x8, y8, x_cent, y_cent)
    p.C(x10, y10, x11, y11, x12, y12)
    d.append(p)

    minirad = stretch_ratio*rad/6
    bottomlevel = y_cent+rad/4 # is this actually correct?
    xoffs = rad/2 # is this actually correct?
    d.append(draw.Circle(x_cent, y_cent-rad/2, minirad,  fill=dotcolour))
    d.append(draw.Circle(x_cent+xoffs, bottomlevel, minirad,  fill=dotcolour))
    d.append(draw.Circle(x_cent-xoffs, bottomlevel, minirad,  fill=dotcolour))


def draw_circle(d, primary_colour, secondary_colour='none',
              wid=UNSPECIFIED, hei=UNSPECIFIED, x_start=0, y_start=0,
              size_ratio = 1.0, stretch_ratio=1.0, thick_ratio=1.0, orientation=HORIZONTAL):
    """
    Draw a solid circle
    :param d: Drawing object
    :param primary_colour: fill colour (string) of the circle
    :param secondary_colour: colour (string) of the outline of the circle
    :param wid: width of the area we are working with
    :param hei: height of the area we are working with
    :param x_start: the x-coordinate of the upper left corner of the rectangular area that is being drawn into
    :param y_start: the y-coordinate of the upper left corner of the rectangular area that is being drawn into
    :param size_ratio: size factor
    :return: none
    """
    wid, hei = get_effective_dimensions(d, wid, hei)
    midx = x_start + wid/2
    midy = y_start + hei/2
    radius = (hei/2)*size_ratio*0.975
    sw = 0
    if secondary_colour != 'none':
        sw = thick_ratio*hei/20
    d.append(draw.Circle(midx, midy, radius, fill=primary_colour, stroke=secondary_colour, stroke_width=sw))
    return radius


def draw_ellipse(d, primary_colour, secondary_colour='none',
              wid=UNSPECIFIED, hei=UNSPECIFIED, x_start=0, y_start=0,
              size_ratio = 1.0, stretch_ratio=1.0, thick_ratio=1.0, orientation=HORIZONTAL):
    """
    Draw a solid ellipse
    :param d: Drawing object
    :param primary_colour: fill colour (string) of the circle
    :param secondary_colour: colour (string) of the outline of the circle
    :param wid: width of the area we are working with
    :param hei: height of the area we are working with
    :param x_start: the x-coordinate of the upper left corner of the rectangular area that is being drawn into
    :param y_start: the y-coordinate of the upper left corner of the rectangular area that is being drawn into
    :param size_ratio: y-axis radius
    :param stretch_ratio: scaling factor of the x-axis radius
    :param thick_ratio: scaling factor for outline of the ellipse (if used)
    :return: none
    """
    wid, hei = get_effective_dimensions(d, wid, hei)
    midx = x_start + wid/2
    midy = y_start + hei/2
    radius = (hei/2)*size_ratio*0.975
    sw = 0
    if secondary_colour != 'none':
        sw = thick_ratio*hei/20
    d.append(draw.Ellipse(midx, midy, radius*stretch_ratio, radius, fill=primary_colour, stroke=secondary_colour, stroke_width=sw))
    return radius



def draw_inverted_triangle(d, primary_colour, secondary_colour='none',
                           wid=UNSPECIFIED, hei=UNSPECIFIED, x_start=0, y_start=0,
                           size_ratio = 1.0, stretch_ratio=1.0, thick_ratio=1.0, orientation=HORIZONTAL):
    """
    Draw an inverted triangle like the pink triangle flag
    :param d: Drawing object
    :param primary_colour: fill colour (string) of the triangle
    :param secondary_colour: colour (string) of the outline of the triangle
    :param wid: width of the area we are working with
    :param hei: height of the area we are working with
    :param x_start: the x-coordinate of the upper left corner of the rectangular area that is being drawn into
    :param y_start: the y-coordinate of the upper left corner of the rectangular area that is being drawn into
    :param size_ratio: size factor
    :return: none
    """
    wid, hei = get_effective_dimensions(d, wid, hei)
    if secondary_colour:
        sw = hei/50
    else:
        sw = 0

    w = wid/132.292
    h = hei/79.375

    triwidtop = (109.178*w -  23.330*w)*size_ratio
    triwidhei = (78.977*h - 0.661*h)*size_ratio*stretch_ratio
    midx = x_start + wid/2
    midy = y_start + hei/2
    left = midx - triwidtop/2
    right= midx + triwidtop/2
    top = midy - triwidhei/2
    bottom = midy + triwidhei/2

    p = draw.Path(fill=primary_colour, stroke=secondary_colour, stroke_width=sw)
    p.M(left,top).L(right, top).L(midx, bottom).L(left,top).Z()
    d.append(p)


def draw_triangle(d, primary_colour, secondary_colour='none',
              wid=UNSPECIFIED, hei=UNSPECIFIED, x_start=0, y_start=0,
              size_ratio = 1.0, stretch_ratio=1.0, thick_ratio=1.0, orientation=HORIZONTAL):
    """
    Draw a triangle
    :param d: Drawing object
    :param primary_colour: the fill of the star
    :param secondary_colour: the outline of the star
    :param wid: width of the area we are working with
    :param hei: height of the area we are working with
    :param x_start: the x-coordinate of the upper left corner of the rectangular area that is being drawn into
    :param y_start: the y-coordinate of the upper left corner of the rectangular area that is being drawn into
    :param size_ratio: size factor
    :param stretch_ratio: affects the length of the base of the triangle relative to the other two vertices. If set to 1, triangle will be equilateral.
    :param thick_ratio: scaling factor for the stroke width.
    :return: the height of the top/bottom lines
    """
    angle_offset = angle_offset_for_orientation(orientation) - 90
    #print('ang offs', angle_offset, orientation)
    wid, hei = get_effective_dimensions(d, wid, hei)

    midx = x_start + wid/2
    midy = y_start + hei/2

    radius = size_ratio*hei/4

    if secondary_colour != 'none':
        sw = thick_ratio*hei/100
    else:
        sw = 0


    y_top = midy - radius
    y_base = midy + radius
    x_top = midx
    x_left = midx - radius*stretch_ratio
    x_right = midx + radius*stretch_ratio

    p = draw.Path(fill=primary_colour, stroke=secondary_colour, stroke_width=sw, transform=f'rotate({angle_offset},{midx},{midy})')
    p.M(x_top, y_top).L(x_left, y_base).L(x_right, y_base).L(x_top, y_top)
    p.Z()
    d.append(p)
    return sw



def draw_asympile(d, primary_colour, secondary_colour='none',
              wid=UNSPECIFIED, hei=UNSPECIFIED, x_start=0, y_start=0,
              size_ratio = 1.0, stretch_ratio=1.0, thick_ratio=1.0, orientation=HORIZONTAL):
    """
    Draw an asymmetric pile in the style of the tricolour polyamory flag
    :param d: Drawing object
    :param primary_colour: fill colour (string) of the triangle
    :param secondary_colour: colour (string) of the outline of the triangle
    :param wid: width of the area we are working with
    :param hei: height of the area we are working with
    :param x_start: the x-coordinate of the upper left corner of the rectangular area that is being drawn into
    :param y_start: the y-coordinate of the upper left corner of the rectangular area that is being drawn into
    :param size_ratio: size factor
    :return: none
    """
    wid, hei = get_effective_dimensions(d, wid, hei)
    if secondary_colour:
        sw = hei/50
    else:
        sw = 0

    horizlinewid = hei/3

    top = y_start
    bottom = y_start + hei
    left = x_start
    x_rightorigin = left + horizlinewid
    x_rightmost = left + 2*horizlinewid
    y_rightmost = top + horizlinewid

    p = draw.Path(fill=primary_colour, stroke=secondary_colour, stroke_width=sw)
    p.M(left, top)
    p.L(left, bottom)
    p.L(x_rightmost, y_rightmost)
    p.L(x_rightorigin, top)
    p.L(left, top).Z()
    d.append(p)


def draw_trichevron(d, colours,
              wid=UNSPECIFIED, hei=UNSPECIFIED, x_start=0, y_start=0,
              size_ratio = 1.0, stretch_ratio=1.0, thick_ratio=1.0, orientation=HORIZONTAL):
    """
    Draw three chevrons in this style from https://queerflag.tumblr.com/post/151443283619/bizexuals-more-queer-pride-flagsvariations
    :param d: Drawing object
    :param colours: in order: top chevron, (optional) middle chevron, (optional) bottom chevron.
                If two colours are provided, they are used for top & bottom and the middle area is transparent.
                If one colour is provided, it is used for top & bottom and the middle area is transparent.
    :param wid: width of the area we are working with
    :param hei: height of the area we are working with
    :param x_start: the x-coordinate of the upper left corner of the rectangular area that is being drawn into
    :param y_start: the y-coordinate of the upper left corner of the rectangular area that is being drawn into
    :param size_ratio: size factor
    :return: the height of the top/bottom chevrons
    """
    base_sw = d.height/6
    # top chevron
    heights = [base_sw, base_sw/2, base_sw]
    start_height = base_sw
    mid_height = base_sw*2.5
    mid_bottom = mid_height

    if len(colours) > 2:
        colours_in_use = colours.copy()
    elif len(colours) == 2:
        colours_in_use = [colours[0], 'none', colours[1]]
    else: #if len(colours) == 1:
        colours_in_use = [colours[0], 'none', colours[0]]

    for i in range(3):
        sw = heights[i]
        mid_bottom += sw
        if type(colours_in_use[i]) == str:
            p = draw.Path(fill=colours_in_use[i])
        else:
            p = draw.Path(fill=colours_in_use[i].hex)
        p.M(0, start_height)
        p.L(d.width/2, mid_height).L(d.width, start_height) # top
        p.L(d.width, start_height+sw) #go down
        p.L(d.width/2, mid_bottom).L(0, start_height+sw).Z()
        d.append(p)
        start_height += sw
        mid_height = mid_bottom
    return base_sw


def draw_crossdresser(d, colours,
              wid=UNSPECIFIED, hei=UNSPECIFIED, x_start=0, y_start=0,
              size_ratio = 1.0, stretch_ratio=1.0, thick_ratio=1.0, orientation=HORIZONTAL):
    """
    Draw an X in the style of this crossdresser flag: https://flag.library.lgbt/flags/crossdresser/
    :param d: Drawing object
    :param colours: in order top background, bottom background
    :param wid: width of the area we are working with
    :param hei: height of the area we are working with
    :param x_start: the x-coordinate of the upper left corner of the rectangular area that is being drawn into
    :param y_start: the y-coordinate of the upper left corner of the rectangular area that is being drawn into
    :param size_ratio: size factor
    :return: the height of the top/bottom chevrons
    """
    if len(colours) == 1:
        colours.append('none')

    wid, hei = get_effective_dimensions(d, wid, hei)
    midx = x_start + wid/2
    midy = y_start + hei/2

    draw_horiz_bars(d, colours, wid=wid, hei=hei, x_start=x_start, y_start=y_start)

    line_wid = wid/8
    line_hei = line_wid*(hei/wid)

    top = y_start
    bottom = y_start+hei
    leftmost = x_start
    rightmost = x_start + wid

    p = draw.Path(fill=colours[0])
    p.M(leftmost, bottom)
    p.L(leftmost, bottom-line_hei)
    p.L(midx-line_wid, midy)
    p.L(midx+line_wid, midy)
    p.L(rightmost, bottom-line_hei)
    p.L(rightmost, bottom) # bottom right corner
    p.L(rightmost-line_wid, bottom) # double back
    p.L(midx, midy+line_hei)
    p.L(x_start+line_wid, bottom)
    p.L(x_start+line_wid, bottom)
    p.Z()
    d.append(p)

    p = draw.Path(fill=colours[1])
    p.M(leftmost, top)
    p.L(leftmost, top+line_hei)
    p.L(midx-line_wid, midy)
    p.L(midx+line_wid, midy)
    p.L(rightmost, top+line_hei)
    p.L(rightmost, top) # bottom right corner
    p.L(rightmost-line_wid, top) # double back
    p.L(midx, midy-line_hei)
    p.L(x_start+line_wid, top)
    p.L(x_start+line_wid, top)
    p.Z()
    d.append(p)


def draw_equals(d, primary_colour, secondary_colour='none',
              wid=UNSPECIFIED, hei=UNSPECIFIED, x_start=0, y_start=0,
              size_ratio = 1.0, stretch_ratio=1.0, thick_ratio=1.0, orientation=HORIZONTAL):
    """
    Draw an equals sign in the style of the horizontal androgyne flag
    :param d: Drawing object
    :param primary_colour: the colour of the top
    :param bottom: the colour of the bottom
    :param wid: width of the area we are working with
    :param hei: height of the area we are working with
    :param x_start: the x-coordinate of the upper left corner of the rectangular area that is being drawn into
    :param y_start: the y-coordinate of the upper left corner of the rectangular area that is being drawn into
    :param size_ratio: size factor
    :return: the height of the top/bottom lines
    """
    wid, hei = get_effective_dimensions(d, wid, hei)
    midx = x_start + wid/2
    midy = y_start + hei/2

    line_hei = hei/5
    line_wid = size_ratio*(wid*0.43)/2

    # top
    p = draw.Path(fill=primary_colour)
    p.M(midx-line_wid, line_hei)
    p.L(midx+line_wid, line_hei)
    p.L(midx+line_wid, 2*line_hei)
    p.L(midx-line_wid, 2*line_hei).Z()
    d.append(p)

    # bottom
    p = draw.Path(fill=secondary_colour)
    p.M(midx-line_wid, 3*line_hei)
    p.L(midx+line_wid, 3*line_hei)
    p.L(midx+line_wid, 4*line_hei)
    p.L(midx-line_wid, 4*line_hei).Z()
    d.append(p)
    return line_hei


def draw_bipolar(d, primary_colour, secondary_colour='none',
              wid=UNSPECIFIED, hei=UNSPECIFIED, x_start=0, y_start=0,
              size_ratio = 1.0, stretch_ratio=1.0, thick_ratio=1.0, orientation=HORIZONTAL):
    """
    Draw the bipolar symbol
    :param d: Drawing object
    :param primary_colour: the fill of the lines
    :param secondary_colour: the background colour
    :param wid: width of the area we are working with
    :param hei: height of the area we are working with
    :param x_start: the x-coordinate of the upper left corner of the rectangular area that is being drawn into
    :param y_start: the y-coordinate of the upper left corner of the rectangular area that is being drawn into
    :param size_ratio: size factor
    :return: the height of the top/bottom lines
    """
    wid, hei = get_effective_dimensions(d, wid, hei)
    midx = x_start + wid/2
    midy = y_start + hei/2

    rad = hei/10
    # filling in a side
    p = draw.Path(fill=secondary_colour)
    p.M(midx-rad, y_start)
    p.L(midx+rad, midy)
    p.L(midx-rad, y_start+hei)
    p.L(x_start+wid, y_start+hei)
    p.L(x_start+wid, y_start)
    p.L(midx, y_start).Z()
    d.append(p)

    # the circles
    dotwidth = wid/4
    dotheight = hei/6
    leftside = midx - dotwidth
    rightside = midx + dotwidth
    top = midy - dotheight
    bottom = midy + dotheight
    d.append(draw.Circle(leftside, top, rad, fill=primary_colour))
    d.append(draw.Circle(leftside, bottom, rad, fill=primary_colour))
    d.append(draw.Circle(rightside, top, rad, fill=primary_colour))
    d.append(draw.Circle(rightside, bottom, rad, fill=primary_colour))

    w = wid/291.20126
    h = hei/291.20126*2

    x_start -= 5*w
    y_start -= 37.162864*h + 4*h
    # x coordinates
    x1 = x_start + 143.0 * w
    x6 = x_start + 136.0 * w
    x7 = x_start + 118.0 * w
    x8 = x_start + 115.0 * w
    x9 = x_start + 113.0 * w
    x12 = x_start + 121.0 * w
    x13 = x_start + 130.0 * w
    x14 = x_start + 148.0 * w
    x15 = x_start + 155.0 * w
    x16 = x_start + 173.0 * w
    x17 = x_start + 178.0 * w
    x20 = x_start + 160.0 * w
    x21 = x_start + 145.0 * w
    # y coordinates
    y1 = y_start + 114.0 * h
    y3 = y_start + 113.0 * h
    y4 = y_start + 112.0 * h
    y5 = y_start + 100.0 * h
    y6 = y_start + 84.0 * h
    y7 = y_start + 47.0 * h
    y8 = y_start + 42.0 * h
    y9 = y_start + 37.0 * h
    y14 = y_start + 52.0 * h
    y15 = y_start + 87.0 * h

    p = draw.Path(fill=primary_colour)
    p.M(x1, y1)
    p.C(x1, y1, x1, y3, x1, y4)
    p.C(x1, y5, x6, y6, x7, y7)
    p.C(x8, y8, x9, y9, x9, y9)
    p.C(x9, y9, x12, y9, x13, y9)
    p.H(x14)
    p.L(x15, y14)
    p.C(x16, y15, x17, y5, x17, y3)
    p.L(x17, y1)
    p.H(x20)
    p.C(x21, y1, x1, y1, x1, y1)
    p.Z()
    d.append(p)

    p = draw.Path(fill=primary_colour, transform=f'translate(0, {2*midy}) scale(1,-1)')
    p.M(x1, y1)
    p.C(x1, y1, x1, y3, x1, y4)
    p.C(x1, y5, x6, y6, x7, y7)
    p.C(x8, y8, x9, y9, x9, y9)
    p.C(x9, y9, x12, y9, x13, y9)
    p.H(x14)
    p.L(x15, y14)
    p.C(x16, y15, x17, y5, x17, y3)
    p.L(x17, y1)
    p.H(x20)
    p.C(x21, y1, x1, y1, x1, y1)
    p.Z()
    d.append(p)


def draw_belt(d, primary_colour, secondary_colour='none',
              wid=UNSPECIFIED, hei=UNSPECIFIED, x_start=0, y_start=0,
              size_ratio = 1.0, stretch_ratio=1.0, thick_ratio=1.0, orientation=HORIZONTAL):
    # default size should be voidpunk
    wid, hei = get_effective_dimensions(d, wid, hei)
    midx = x_start + wid/2
    midy = y_start + hei/2

    radius = size_ratio*(hei*0.185)
    belt_thickness = thick_ratio*(hei/4)*(1/3)

    p = draw.Path(stroke_width=belt_thickness, stroke=primary_colour)
    p.M(x_start, midy).L(midx-radius, midy)
    p.M(x_start+wid, midy).L(midx+radius, midy)
    d.append(p)

    d.append(draw.Circle(midx, midy, radius,
                         stroke=primary_colour, fill=secondary_colour,
                         stroke_width=belt_thickness*0.825))

    return belt_thickness


def draw_diamond(d, primary_colour, secondary_colour='none',
              wid=UNSPECIFIED, hei=UNSPECIFIED, x_start=0, y_start=0,
              size_ratio = 1.0, stretch_ratio=1.0, thick_ratio=1.0, orientation=HORIZONTAL):
    """
    Draw a Diamond, based on the Alderspintellic flag
    from https://www.tumblr.com/revenant-coining/704184782702149633/alderspintellic-an-aldernic-term-for-one-is-or
    :param d: Drawing object
    :param primary_colour: the fill of the diamond
    :param secondary_colour: optional outline of diamond
    :param wid: width of the area we are working with
    :param hei: height of the area we are working with
    :param x_start: the x-coordinate of the upper left corner of the rectangular area that is being drawn into
    :param y_start: the y-coordinate of the upper left corner of the rectangular area that is being drawn into
    :param size_ratio: size factor. The "radius" of the diamond.
    :param stretch_ratio: scaling factor used to stretch the diamond horizontally.
    :param thick_ratio: scaling factor for the line width of the outline (if used)
    :return: stroke width
    """

    wid, hei = get_effective_dimensions(d, wid, hei)
    midx = x_start + wid/2
    midy = y_start + hei/2

    diamond_height = hei*0.3*size_ratio
    diamond_width = diamond_height*0.8*stretch_ratio

    p = draw.Path(fill=primary_colour)
    if secondary_colour != 'none':
        sw = diamond_height*0.035*thick_ratio
        p = draw.Path(fill=primary_colour, stroke=secondary_colour, stroke_width=sw)
    p.M(midx, midy-diamond_height)
    p.L(midx+diamond_width, midy)
    p.L(midx, midy+diamond_height)
    p.L(midx-diamond_width, midy)
    p.L(midx, midy-diamond_height).Z()
    d.append(p)
    return diamond_height



def draw_teardrop(d, primary_colour, secondary_colour='none',
              wid=UNSPECIFIED, hei=UNSPECIFIED, x_start=0, y_start=0,
              size_ratio = 1.0, stretch_ratio=1.0, thick_ratio=1.0, orientation=HORIZONTAL):
    """
    Draw a teardrop in the centre
    :param d: Drawing object
    :param primary_colour: fill colour (string) of the teardrop
    :param secondary_colour: colour (string) of the outline
    :param wid: width of the area we are working with
    :param hei: height of the area we are working with
    :param x_start: the x-coordinate of the upper left corner of the rectangular area that is being drawn into
    :param y_start: the y-coordinate of the upper left corner of the rectangular area that is being drawn into
    :param size_ratio: size factor (radius of teardrop's base circle)
    :param stretch_ratio: how stretched out the teardrop is
    :param thick_ratio: scaling factor for the line width (if outline of heart is used). Default is hei/100 if outlining, 0 if not.
    :return: none
    """
    wid, hei = get_effective_dimensions(d, wid, hei)
    midx = x_start + wid/2
    midy = y_start + hei/2

    radius = size_ratio*(hei/6)
    tear_len = radius*stretch_ratio*2.5
    sw = thick_ratio*(hei/100)

    circ_y = midy+tear_len*0.5
    #d.append(draw.Circle(midx, circ_y, radius, stroke=secondary_colour, stroke_width=sw, fill=primary_colour))

    cy_bottom_roundness = midy+tear_len*1
    cy_top_roundness = midy+tear_len*0.6
    cx_top_roundness = radius
    tear_top = midy - tear_len*0.5
    p = draw.Path(stroke=secondary_colour, stroke_width=sw, fill=primary_colour)
    p.M(midx, tear_top) # start from the top
    p.Q(midx+cx_top_roundness, cy_top_roundness , midx+radius, circ_y)
    p.C(midx+radius, cy_bottom_roundness, midx-radius, cy_bottom_roundness, midx-radius, circ_y) # round part at the bottom
    p.Q(midx-cx_top_roundness, cy_top_roundness, midx, tear_top)
    d.append(p)


def draw_caed(d, primary_colour, secondary_colour='none',
              wid=UNSPECIFIED, hei=UNSPECIFIED, x_start=0, y_start=0,
              size_ratio=1.0, stretch_ratio=1.0, thick_ratio=1.0, orientation=HORIZONTAL):
    """
    Draw the bottom vertical stripes used in the caedsexual, caedromantic, etc flags
    :param d: Drawing object
    :param primary_colour: fill colour of the middle bar
    :param secondary_colour: fill colour of the side bars
    :param wid: width of the area we are working with
    :param hei: height of the area we are working with
    :param x_start: the x-coordinate of the upper left corner of the rectangular area that is being drawn into
    :param y_start: the y-coordinate of the upper left corner of the rectangular area that is being drawn into
    :param size_ratio: size factor - radius of the central diamond
    :param stretch_ratio: how concave to make the middle lines. Set to 0 for a flat line.
    :param thick_ratio: not currently used
    :return: radius
    """
    wid, hei = get_effective_dimensions(d, wid, hei)

    step_height = size_ratio * (hei / 5)
    each_wid = stretch_ratio*(wid / 5)

    bottom_left = x_start
    bottom = y_start + hei
    side_height = step_height*2
    mid_left = bottom_left+each_wid*2
    mid_height = step_height*3

    # side stripes
    d.append(draw.Rectangle(bottom_left+each_wid, bottom-side_height, each_wid*3, side_height, fill=primary_colour))

    # middle stripe
    d.append(draw.Rectangle(mid_left, bottom-mid_height, each_wid, mid_height, fill=secondary_colour))


if __name__ == '__main__':
    doctest.testmod()
    wid = 500
    hei = 300
    d = draw.Drawing(wid, hei)
    draw_horiz_bars(d, ['black'])
    '''
    draw_perisex(d, 'white')
    draw_rhombus(d, 'blue', size_ratio=0.75)
    draw_square(d, 'green', size_ratio=1.8)
    draw_diagonal_cut_square(d, 'green', size_ratio=1.8)
    draw_altersex_symbol(d, 'red', 'pink', size_ratio=0.1)
    '''
    draw_diamond(d, 'white', 'red')
    d.save_png('drawflags/test.png')

    d = draw.Drawing(wid, hei)
    pal = ['purple', 'orange', 'black', 'grey', 'red']
    draw_horiz_bars(d, pal)
    #draw_bipolar(d, 'blue', 'black')
    #draw_fivesided_star(d, 'red', y_start=-100, x_start=100, orientation=DIAGONAL)
    #draw_arbitrary_star(d,'red', 'black', num_points=20, secondary_size=0.75, square=False)
    #draw_bipolar(d, 'black', 'blue')
    #draw_teardrop(d,'white')
    #draw_caed(d, 'green', 'yellow')
    draw_open_lemniscate(d, 'white')
    d.save_svg('drawflags/test2.svg')