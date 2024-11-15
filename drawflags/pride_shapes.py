"""
Draw shapes that are neither lines nor rings.

draw_square is unlike the others in this file

"""
import drawsvg

from pride_rings import *


def draw_text(d, text_to_add, fill_colour, wid=UNSPECIFIED, hei=UNSPECIFIED, size_ratio=1.0, x_start=0, y_start=0, orientation=VERTICAL, name=None):
    """
    Add text to the flag
    :param d: Drawing object
    :param fill_colour: the colour of the text
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
    if type(fill_colour) == list:
        fill_colour = fill_colour[0]
    wid, hei = get_effective_dimensions(d, wid, hei)
    textsize = size_ratio*(hei/3)
    y_coord = (hei/2) + (textsize/5) + y_start
    d.append(draw.Text(text_to_add, textsize, wid / 2, y_coord, fill=fill_colour,
                       text_anchor='middle', dominant_baseline='middle', font_family='Times New Roman'))  # 8pt text at (-10, -35)


def draw_pile(d, fill_colour, wid=UNSPECIFIED, hei=UNSPECIFIED, x_start=0, y_start=0, size_ratio = 1.0, orientation=VERTICAL):
    """
    Add a triangle to the left side like in the demisexual flag
    (it's called a pile: https://en.wikipedia.org/wiki/Glossary_of_vexillology )
    :param d: Drawing object
    :param fill_colour: fill of the pile (str hex code)
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
    p = draw.Path(fill=fill_colour)
    p.M(leftmost, topmost)
    p.L(x_dist, hei / 2)
    p.L(leftmost, hei)
    p.L(leftmost, topmost).Z()
    d.append(p)


def draw_multipile(d, colours, wid=UNSPECIFIED, hei=UNSPECIFIED,  x_start=0, y_start=0,
                   size_ratio = 1.0, line_width=UNSPECIFIED, orientation=VERTICAL):
    """
    Add a triangle to the left side like in the demisexual flag
    (it's called a pile: https://en.wikipedia.org/wiki/Glossary_of_vexillology )
    :param d: Drawing object
    :param fill_colour: fill of the pile (str hex code)
    :param wid: width of the area we are working with
    :param hei: height of the area we are working with
    :param size_ratio: used to scale the size (width) of the pile
    :return: the width of the leftmost pile
    >>> d = draw.Drawing(500, 300)
    >>> draw_pile(d, RAINBOW[0])
    >>> len(d.elements) == 1 and d.elements[-1].args['fill'] == RAINBOW[0]
    True
    >>> type(d.elements[0])
    <class 'drawsvg.elements.Path'>
    """
    wid, hei = get_effective_dimensions(d, wid, hei)

    if type(line_width) not in [int, float] or line_width < 0:
        line_width = wid/10
    piles = []
    first_width = None
    for i, fill_colour in enumerate(colours):
        x_offset = i*line_width + x_start
        x_dist = ((wid/3) * size_ratio)+x_offset # a third of the width by default

        leftmost = x_offset
        topmost = 0
        p = draw.Path(fill=fill_colour)
        p.M(leftmost, topmost)
        p.L(x_dist, hei / 2)
        p.L(leftmost, hei)
        p.L(x_start, hei).L(x_start, topmost)
        p.L(leftmost, topmost).Z()
        piles.append(p)
        if not first_width:
            first_width = x_dist

    # add them in reverse order
    for p in reversed(piles):
        d.append(p)
    return first_width

def draw_corners(d, fill_colour, wid=UNSPECIFIED, hei=UNSPECIFIED, size_ratio=1.0, orientation=VERTICAL):
    """
    Add diagonal corners in the style of the disability pride flag
    :param d: Drawing object
    :param fill_colour: fill of the corners (str hex code)
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
    p = draw.Path(fill=fill_colour, stroke=fill_colour)

    upper_height = (1/3)*hei*size_ratio
    lefter_width = (1/3)*wid*size_ratio
    p.M(0, hei).L(0, upper_height).L(wid-lefter_width, hei).Z()
    d.append(p)

    # upper right
    p = draw.Path(fill=fill_colour)
    p.M(wid, 0).L(wid, hei-upper_height).L(lefter_width, 0).Z()
    d.append(p)



def draw_topbottom(d, fill_colour, wid=UNSPECIFIED, hei=UNSPECIFIED, size_ratio=1.0, orientation=VERTICAL):
    """
    Add stripes to top and bottom. Used for mashup flags.
    :param d: Drawing object
    :param fill_colour: fill colour
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
    p = draw.Path(fill=fill_colour, stroke=fill_colour)
    upper_height = (1/3)*hei*size_ratio

    # top
    p.M(0, 0).L(0, upper_height).L(wid, upper_height).L(wid, 0).L(0,0).Z()
    d.append(p)

    # bottom
    p = draw.Path(fill=fill_colour)
    p.M(0, hei).L(0, hei-upper_height).L(wid, hei-upper_height).L(wid, hei).L(0,hei).Z()
    d.append(p)


def draw_perisex(d, fill_colour, wid=UNSPECIFIED, hei=UNSPECIFIED, size_ratio=1.0, orientation=VERTICAL):
    """
    Draws an abstract scale/balance thing with f and m ends
    :param d: drawing image
    :param fill_colour: colour of the lines
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
    d.append(draw.Line(l, h, r, h, stroke=fill_colour, stroke_width=sw, stroke_linecap='round'))
    d.append(draw.Line(l, h, l, fem_end, stroke=fill_colour, stroke_width=sw, stroke_linecap='round'))
    d.append(draw.Line(r, h, r, h + down, stroke=fill_colour, stroke_width=sw, stroke_linecap='round'))

    # fem
    # d.append(draw.Line(l-arm, arm_x, l+arm, arm_x, stroke=fill, stroke_width=sw, stroke_linecap='round'))
    p = draw.Path(stroke=fill_colour, stroke_width=sw, fill=fill_colour, stroke_linecap='round')
    arm_low = h + down + (fudge / 4)
    f_arm = arm * 1.5
    arm_m = arm_x

    fudge = sw/3
    p.M(l-arm, h+down+fudge).L(l, arm_m).L(l+arm, h+down+fudge).Z()
    #p.M(l-arm, arm_m).L(l, h+down).L(l+arm, arm_m).Z()

    d.append(p)
    # masc
    p = draw.Path(stroke=fill_colour, stroke_width=sw, fill=fill_colour, stroke_linecap='round')
    p.M(r - arm, arm_m).L(r, h + down).L(r + arm, arm_m).Z()
    d.append(p)

    # start
    d.append(draw.Line(wid / 2, h, wid / 2, h - hangar, stroke=fill_colour, stroke_width=sw, stroke_linecap='round'))


def draw_rhombus(d, outer_colour, fill='none', wid=UNSPECIFIED, hei=UNSPECIFIED, size_ratio=1.0, orientation=VERTICAL):
    """
    Draw a square on a diagonal
    :param d: Drawing object
    :param outer_colour: the colour of the rhombus
    :param fill: the colour to fill the rhombus with
    :param wid: width of the area we are working with
    :param hei: height of the area we are working with
    :param size_ratio: size factor
    :return: none
    >>> d = draw.Drawing(500, 300)
    >>> draw_rhombus(d, RAINBOW[0])
    >>> len(d.elements) == 1 and d.elements[-1].args['stroke'] == RAINBOW[0]
    True
    >>> type(d.elements[0])
    <class 'drawsvg.elements.Path'>
    """
    wid, hei = get_effective_dimensions(d, wid, hei)
    p = draw.Path(stroke=outer_colour, stroke_width=hei / 10, fill=fill)
    radius_perc = 0.25 # by default have it take up 1/4 of the height
    radius = hei * radius_perc * size_ratio
    mx, my = wid/2, hei/2
    p.M(mx, my-radius)
    p.L(mx+radius, my)
    p.L(mx, my+radius)
    p.L(mx-radius, my).Z()
    d.append(p)


def draw_square(d, outer_colour, fill_colour='none', wid=UNSPECIFIED, hei=UNSPECIFIED,
                x_start=0, y_start=0, size_ratio = 1.0, orientation=VERTICAL):
    """Draw a square in the style of the dyadic/endosex flag.
    :param d: Drawing object
    :param outer_colour: a colour as a string
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
    p = draw.Path(stroke=outer_colour, stroke_width=sw, fill=fill_colour)
    radius = hei * 0.5 * size_ratio # half the height by default
    p.M((wid/2)-radius/2, (hei/2)-radius/2)
    p.L((wid/2)+radius/2, (hei/2)-radius/2)
    p.L((wid/2)+radius/2, (hei/2)+radius/2)
    p.L((wid/2)-radius/2, (hei/2)+radius/2).Z()
    d.append(p)
    return radius + sw


def draw_diagonal_cut_square(d, fill_colour, wid=UNSPECIFIED, hei=UNSPECIFIED, size_ratio=1.0, orientation=VERTICAL):
    """Draw half of a square that is cut diagonally, to be superimposed with draw_square
    to produce dyadic/endosex flags.
    :param d: Drawing object
    :param fill_colour: the colour of the half-square
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

        p = draw.Path(fill=fill_colour)  # draw the stripe as a Path with four points
        p.M(up_left, up_y)
        p.L(down_left, down_y).L(down_right, down_y)
        p.L(up_right, up_y).L(up_right, up_y)
        p.Z()

        clip = draw.ClipPath()
        clip.append(p)
        pr = draw.Path(stroke=fill_colour, stroke_width=hei / 10, fill='none', clip_path=clip)
        pr.M((wid / 2) - radius / 2, (hei / 2) - radius / 2)
        pr.L((wid / 2) + radius / 2, (hei / 2) - radius / 2)
        pr.L((wid / 2) + radius / 2, (hei / 2) + radius / 2)
        pr.L((wid / 2) - radius / 2, (hei / 2) + radius / 2).Z()
        d.append(pr)


def draw_bissu(d, left_colour, right_colour, wid=UNSPECIFIED, hei=UNSPECIFIED,
               x_start=0, y_start=0, orientation=VERTICAL):
    """
    Draw triangles in the style of the Bissu flag
    :param d: Drawing ojbect
    :param left_colour: colour of the left triangle
    :param right_colour: colour of the right triangle
    :param wid: width of the area we are working with
    :param hei: height of the area we are working with
    :return: none
    """
    wid, hei = get_effective_dimensions(d, wid, hei)
    p = draw.Path(fill=left_colour)
    mh = hei/2
    mw = wid/2
    p.M(x_start, mh).L(mw, y_start).L(mw, hei).Z()
    d.append(p)
    p = draw.Path(fill=right_colour)
    p.M(wid, mh).L(mw, y_start).L(mw, hei).Z()
    d.append(p)


def draw_altersex_symbol(d, outer_colour, fill_colour, wid=UNSPECIFIED, hei=UNSPECIFIED,
                         x_start=0, y_start=0, size_ratio=1.0, orientation=VERTICAL):
    '''
    Draw a triangle with a ring
    :param d: Drawing object
    :param outer_colour: colour (string) of the outline of the symbol
    :param fill_colour: fill colour (string) of the symbol
    :param wid: width of the area we are working with
    :param hei: height of the area we are working with
    :param size_ratio: size factor
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
    sw = radius/4 # started with /4
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
    d.append(draw.Circle(x_mid, y_coord, radius+sw,  fill='none', stroke=outer_colour, stroke_width=sw))
    d.append(draw.Circle(x_mid, y_coord, radius-sw,  fill='none', stroke=outer_colour, stroke_width=sw))

    # draw triangle
    p = draw.Path(fill=fill_colour, stroke=outer_colour, stroke_width=sw)
    p.M(x_mid, y_top)
    p.L(x_mid+tri_base, y_base).L(x_mid-tri_base, y_base).L(x_mid, y_top).Z()
    d.append(p)

    # middle ring
    d.append(draw.Circle(x_mid, y_coord, radius, fill='none', stroke=fill_colour, stroke_width=sw))


def draw_cross(d, fill_colour, wid=UNSPECIFIED, hei=UNSPECIFIED, x_start=0, y_start=0, size_ratio=1.0, orientation=VERTICAL):
    """
    Draw a cross that is, by default, the right size to produce the ipsogender flag
    when combined with a Carpenter ring.
    :param d: drawing object
    :param fill_colour: fill of the cross
    :param wid: width of area the symbol is being added to
    :param hei: height of the area the symbol is being added to
    :param size_ratio: scaling factor
    :return: none
    """
    wid, hei = get_effective_dimensions(d, wid, hei)
    midx = (wid/2) + x_start
    midy = (hei/2) + y_start

    # vertical bar
    intop = top_of_ring(hei)
    inbot = base_of_ring(hei)
    thickness = ring_thickness(hei)*size_ratio
    line_height = (inbot - intop)*size_ratio
    d.append(
        draw.Rectangle(midx - (thickness / 2), intop + (thickness / 2), thickness, line_height, fill=fill_colour))

    # horizontal bar
    line_width = line_height
    d.append(
        draw.Rectangle(midx - line_width / 2, midy - (thickness / 2), line_width, thickness, fill=fill_colour))


def draw_metis_lemniscate(d, fill_colour, wid=UNSPECIFIED, hei=UNSPECIFIED, x_start=0, y_start=0, size_ratio=1.0,
                          horiz_stretch=0.15, orientation=VERTICAL):
    """
    Draw an infinity symbol (lemniscate) in the style of the Metis flag.
    :param d: drawing object
    :param fill_colour: fill of the infinity symbol
    :param wid: width of area the symbol is being added to
    :param hei: height of the area the symbol is being added to
    :param size_ratio: scaling factor
    :return: none
    """
    wid, hei = get_effective_dimensions(d, wid, hei)
    stroke_wid = (24/300)*hei*size_ratio
    p = draw.Path(stroke=fill_colour, fill='none', stroke_width=stroke_wid)

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


def single_nautilus_segment(d, wid, hei, arr, fill_colour, step_size, border_width=0.0, border_colour ='black'):
    """
    Helper function for draw_nautilus. Draws a single segment.
    :param d: Drawing object
    :param wid: width of area the entire nautilus is being drawn into
    :param hei: height of the area the entire nautilus is being drawn into
    :param arr: array of coordinates
    :param fill_colour: colour to fill the nautilus segment with
    :param step_size: the "width" of the segment
    :param border_width: width in pixels of the border
    :param border_colour:
    :return:
    """
    mx = step_size + wid / 2
    my = 2*step_size + hei / 2

    p = draw.Path(stroke=border_colour, fill=fill_colour, stroke_width=border_width)
    d.append(p.M(mx, my))
    d.append(p.L(mx+arr[0], my+arr[1]))
    d.append(p.Q(mx+arr[2], my+arr[3], mx+arr[4], my+arr[5]))
    d.append(p.L(mx, my))
    d.append(p.Z())


def draw_nautilus(d, colours, wid=UNSPECIFIED, hei=UNSPECIFIED, x_start=0, y_start=0, size_ratio=1.0,
                  is_horizontal=True, border_colour='black', border_size=0, orientation=VERTICAL):
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
        inc = 10
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


def draw_closet_symbol(d, outer_colour, fill_colour='none', wid=UNSPECIFIED, hei=UNSPECIFIED,
                       x_start=0, y_start=0, size_ratio=1, orientation=VERTICAL):
    """
    Draw a closet symbol, similar in style to the one in isobug's closeted intersex flag
    :param d: Drawing object
    :param outer_colour: colour (string) of the outline of the symbol
    :param fill_colour: fill colour (string) of the symbol
    :param wid: width of the area we are working with
    :param hei: height of the area we are working with
    :param x_start: the x-coordinate of the upper left corner of the rectangular area that is being drawn into
    :param y_start: the y-coordinate of the upper left corner of the rectangular area that is being drawn into
    :param size_ratio: size factor
    :return: none
    """
    wid, hei = get_effective_dimensions(d, wid, hei)
    stroke_width = (hei / 28)*size_ratio

    # for the outer rectangle
    closet_hei = (hei * (2/3))*size_ratio
    closet_wid = closet_hei * .8
    upper_left = (wid/2) - closet_wid/2
    upper_top = (hei/2) - (closet_hei/2)
    round_radius = closet_hei / 6

    # outer rectangle
    d.append(draw.Rectangle(upper_left+x_start, upper_top+y_start, closet_wid, closet_hei, ry=round_radius,
                          stroke=outer_colour, fill=fill_colour, stroke_width=stroke_width))

    # inner rectangle
    diff = closet_hei / 10
    d.append(draw.Rectangle(upper_left+diff+x_start, upper_top+diff+y_start, closet_wid-2*diff, closet_hei-2*diff,
                            ry=round_radius-diff, stroke=outer_colour, fill=fill_colour, stroke_width=stroke_width))

    # line down the middle
    midx = (wid/2) + x_start
    midy = (hei/2) + y_start
    d.append(draw.Line(midx, upper_top+diff+y_start, midx, upper_top+closet_hei-diff+y_start, stroke=outer_colour, stroke_width=stroke_width))

    # handles
    d.append(draw.Line(midx-diff, midy-diff, midx-diff, midy+diff, stroke=outer_colour, stroke_width=stroke_width))
    d.append(draw.Line(midx+diff, midy-diff, midx+diff, midy+diff, stroke=outer_colour, stroke_width=stroke_width))


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


def draw_rubber_zigzags(d, outer_colour, fill_colour='none', wid=UNSPECIFIED, hei=UNSPECIFIED,
                        x_start=0, y_start=0, size_ratio=1, orientation=VERTICAL):
    """
    Draw zigzag stripes in the style of the rubber pride flag.
    :param d: Drawing object
    :param outer_colour: colour (string) of the outline of the symbol
    :param fill_colour: fill colour (string) of the symbol
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

    p = draw.Path(stroke=outer_colour, fill=fill_colour, stroke_width=sw)

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
    p = draw.Path(stroke=outer_colour, stroke_width=sw, fill='none')
    p.M(-sw, lowln_start_y)
    p.L(lowln_start_x, lowln_start_y).L(lowln_descend_x, lowln_descend_y).L(lowln_ascend_x, lowln_start_y)
    d.append(p)
    return line_hei


def draw_refugeeline(d, fill_colour, outer_colour='none',
                     wid=UNSPECIFIED, hei=UNSPECIFIED, x_start=0, y_start=0, size_ratio=1, orientation=VERTICAL):
    """
    Draw a single horizontal line in the style of the refugee flag
    :param d: Drawing object
    :param fill_colour: fill colour (string) of the line
    :param outer_colour: colour (string) of the outline of the line
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
    d.append(draw.Rectangle(x_start, y_start+top_of_line, wid, height_of_line, fill=fill_colour, stroke=outer_colour))
    return top_of_line

def draw_intersex_ally(d, fill_colour, outer_colour='none', wid=UNSPECIFIED, hei=UNSPECIFIED,
                       x_start=0, y_start=0, size_ratio=1, orientation=VERTICAL):
    """
    Draw a chevron/vee in the style of the ally flag
    :param d: Drawing object
    :param fill_colour: fill colour (string) of the line
    :param outer_colour: colour (string) of THE INTERSEX RING INSIDE IT
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

    p = draw.Path(fill=fill_colour) #, stroke=outer_colour)
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
                         stroke=outer_colour, stroke_width=r/7))
    return r




def draw_heart(d, fill_colour, outer_colour='none', wid=UNSPECIFIED, hei=UNSPECIFIED,
               x_start=0, y_start=0, size_ratio=1, orientation=None):
    """
    Draw a heart in the centre
    :param d: Drawing object
    :param fill_colour: fill colour (string) of the heart
    :param outer_colour: colour (string) of the outline of the heart
    :param wid: width of the area we are working with
    :param hei: height of the area we are working with
    :param x_start: the x-coordinate of the upper left corner of the rectangular area that is being drawn into
    :param y_start: the y-coordinate of the upper left corner of the rectangular area that is being drawn into
    :param size_ratio: size factor
    :return: none
    """
    # path traced from https://commons.wikimedia.org/wiki/File:Icons8_flat_like.svg
    wid, hei = get_effective_dimensions(d, wid, hei)
    h = (hei/48)
    w = h #(wid/48)

    # the way inkscape centred the heart on the y axis looks off
    # this is a kludge to fix it
    y_start += 1*(hei/48)

    midx = x_start+ (wid/2)
    midy = y_start+ (hei/2)

    # heart rotation needed for leather flag
    rotateby = angle_offset_for_orientation(orientation)

    # the sides
    max_wid = (24-2)*w*size_ratio
    rightmost = midx+max_wid #wid-x_margin + x_start
    leftmost = midx-max_wid#x_margin + x_start
    y_side = midy - (24-18)*h*size_ratio # 18*h+ yoffs # 21 before centring
    cy_sidetop = midy - (24-11.4)*h*size_ratio #11.4*h+ yoffs #14.4
    cy_sidelower = midy + (30-24)*h*size_ratio #30*h+ yoffs #33

    # the two bumps
    crest_from_midx = (34-24)*w*size_ratio
    cx_outer_from_midx = (40.6-24)*w*size_ratio
    cx_inner_from_midx = (29.8-24)*w*size_ratio
    top_crests = midy - (24-6)*h*size_ratio #6*h+ yoffs # 9
    x_rightcrest = midx+crest_from_midx#34 * w + xoffs # 34
    x_leftcrest = midx-crest_from_midx#wid - x_rightcrest # 14
    cx_outer_rightcrest = midx+cx_outer_from_midx#40.6*w+ xoffs
    cx_outer_leftcrest = midx-cx_outer_from_midx##wid-cx_outer_rightcrest
    cx_inner_rightcrest = midx+cx_inner_from_midx#29.8*w+ xoffs
    cx_inner_leftcrest = midx-cx_inner_from_midx#wid-cx_inner_rightcrest

    # the trough in the middle
    top_from_midy = (24-8.1)*h*size_ratio
    cx_trough_from_midx = (26.1-24)*w*size_ratio
    cy_trough = midy - top_from_midy  # 8.1*h+ yoffs #11.3
    cx_righttrough = midx+cx_trough_from_midx #26.1*w+ xoffs
    cx_lefttrough = midx-cx_trough_from_midx #wid-cx_righttrough

    # the bottom
    bottom = midy + top_from_midy #hei-top_crests #45*h + yoffs

    if rotateby != 0:
        p = draw.Path(fill=fill_colour, stroke=outer_colour, transform=f'rotate({rotateby},{midx},{midy})')
    else:
        p = draw.Path(fill=fill_colour, stroke=outer_colour)
    p.M(x_rightcrest,top_crests) # start from right crest
    p.C(cx_inner_rightcrest,top_crests,cx_righttrough,cy_trough,midx,cy_sidetop) # go ccw to the trough
    p.C(cx_lefttrough,cy_trough,cx_inner_leftcrest,top_crests,x_leftcrest,top_crests) # ccw to left crest
    p.C(cx_outer_leftcrest,top_crests,leftmost,cy_sidetop,leftmost,y_side) # left side
    # originally this had the first cx be 32.9 instead of 33 but I'm simplifying:
    p.C(leftmost,cy_sidelower,midx,bottom,midx,bottom) # go to the bottom
    p.S(rightmost,cy_sidelower,rightmost,y_side) # symmetric copy of last curve
    p.C(rightmost,cy_sidetop,cx_outer_rightcrest,top_crests,x_rightcrest,top_crests) # return to right crest
    p.Z()
    d.append(p)


def draw_pocketgender_hourglass(d, colours, wid=UNSPECIFIED, hei=UNSPECIFIED,
               x_start=0, y_start=0, size_ratio=1, orientation=None):
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


def draw_triskelion(d, colours, wid=UNSPECIFIED, hei=UNSPECIFIED,
               x_start=0, y_start=0, size_ratio=1.0, orientation=None):
    """
    Draw a triskelion symbol used for BDSM fetish flags.
    Based on: https://commons.wikimedia.org/wiki/File:Dotted_triskelion_(fixed_width).svg
    :param d: Drawing object
    :param colours: in order: tracing colour, (optional) fill colour, (optional) dot colour
    :param wid: width of the area we are working with
    :param hei: height of the area we are working with
    :param x_start: the x-coordinate of the upper left corner of the rectangular area that is being drawn into
    :param y_start: the y-coordinate of the upper left corner of the rectangular area that is being drawn into
    :param size_ratio: size factor
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

    sw=hei/20
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

    minirad = rad/6
    bottomlevel = y_cent+rad/4 # is this actually correct?
    xoffs = rad/2 # is this actually correct?
    d.append(draw.Circle(x_cent, y_cent-rad/2, minirad,  fill=dotcolour))
    d.append(draw.Circle(x_cent+xoffs, bottomlevel, minirad,  fill=dotcolour))
    d.append(draw.Circle(x_cent-xoffs, bottomlevel, minirad,  fill=dotcolour))



def draw_circle(d, fill_colour, outer_colour='none', wid=UNSPECIFIED, hei=UNSPECIFIED,
               x_start=0, y_start=0, size_ratio=1.0, orientation=None):
    """
    Draw a solid circle
    :param d: Drawing object
    :param fill_colour: fill colour (string) of the circle
    :param outer_colour: colour (string) of the outline of the circle
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
    if outer_colour != 'none':
        sw = hei/20
    d.append(draw.Circle(midx, midy, radius, fill=fill_colour, stroke=outer_colour, stroke_width=sw))
    return radius


def draw_triangle(d, fill_colour, outer_colour='none', wid=UNSPECIFIED, hei=UNSPECIFIED,
               x_start=0, y_start=0, size_ratio=1.0, orientation=None):
    """
    Draw an inverted triangle like the pink triangle flag
    :param d: Drawing object
    :param fill_colour: fill colour (string) of the triangle
    :param outer_colour: colour (string) of the outline of the triangle
    :param wid: width of the area we are working with
    :param hei: height of the area we are working with
    :param x_start: the x-coordinate of the upper left corner of the rectangular area that is being drawn into
    :param y_start: the y-coordinate of the upper left corner of the rectangular area that is being drawn into
    :param size_ratio: size factor
    :return: none
    """
    wid, hei = get_effective_dimensions(d, wid, hei)
    if outer_colour:
        sw = hei/50
    else:
        sw = 0

    w = wid/132.292
    h = hei/79.375

    triwidtop = (109.178*w -  23.330*w)*size_ratio
    triwidhei = (78.977*h - 0.661*h)*size_ratio
    midx = x_start + wid/2
    midy = y_start + hei/2
    left = midx - triwidtop/2
    right= midx + triwidtop/2
    top = midy - triwidhei/2
    bottom = midy + triwidhei/2

    p = draw.Path(fill=fill_colour, stroke=outer_colour, stroke_width=sw)
    p.M(left,top).L(right, top).L(midx, bottom).L(left,top).Z()
    d.append(p)


def draw_asympile(d, fill_colour, outer_colour='none', wid=UNSPECIFIED, hei=UNSPECIFIED,
               x_start=0, y_start=0, size_ratio=1.0, orientation=None):
    """
    Draw an asymmetric pile in the style of the tricolour polyamory flag
    :param d: Drawing object
    :param fill_colour: fill colour (string) of the triangle
    :param outer_colour: colour (string) of the outline of the triangle
    :param wid: width of the area we are working with
    :param hei: height of the area we are working with
    :param x_start: the x-coordinate of the upper left corner of the rectangular area that is being drawn into
    :param y_start: the y-coordinate of the upper left corner of the rectangular area that is being drawn into
    :param size_ratio: size factor
    :return: none
    """
    wid, hei = get_effective_dimensions(d, wid, hei)
    if outer_colour:
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

    p = draw.Path(fill=fill_colour, stroke=outer_colour, stroke_width=sw)
    p.M(left, top)
    p.L(left, bottom)
    p.L(x_rightmost, y_rightmost)
    p.L(x_rightorigin, top)
    p.L(left, top).Z()
    d.append(p)


def draw_trichevron(d, colours, wid=UNSPECIFIED, hei=UNSPECIFIED,
               x_start=0, y_start=0, size_ratio=1.0, orientation=None):
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


def draw_crossdresser(d, colours, wid=UNSPECIFIED, hei=UNSPECIFIED,
               x_start=0, y_start=0, size_ratio=1.0, orientation=None):
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


def draw_equals(d, top_colour, bottom_colour, wid=UNSPECIFIED, hei=UNSPECIFIED,
               x_start=0, y_start=0, size_ratio=1.0, orientation=None):
    """
    Draw an equals sign in the style of the horizontal androgyne flag
    :param d: Drawing object
    :param top_colour: the colour of the top
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
    p = draw.Path(fill=top_colour)
    p.M(midx-line_wid, line_hei)
    p.L(midx+line_wid, line_hei)
    p.L(midx+line_wid, 2*line_hei)
    p.L(midx-line_wid, 2*line_hei).Z()
    d.append(p)

    # bottom
    p = draw.Path(fill=bottom_colour)
    p.M(midx-line_wid, 3*line_hei)
    p.L(midx+line_wid, 3*line_hei)
    p.L(midx+line_wid, 4*line_hei)
    p.L(midx-line_wid, 4*line_hei).Z()
    d.append(p)
    return line_hei


if __name__ == '__main__':
    doctest.testmod()
    wid = 500
    hei = 300
    d = draw.Drawing(wid, hei)
    draw_horiz_bars(d, ['black'])
    draw_perisex(d, 'white')
    draw_rhombus(d, 'blue', size_ratio=0.75)
    draw_square(d, 'green', size_ratio=1.8)
    draw_diagonal_cut_square(d, 'green', size_ratio=1.8)
    draw_altersex_symbol(d, 'red', 'pink', size_ratio=0.1)
    d.save_png('drawflags/test.png')

    d = draw.Drawing(wid, hei)
    pal = ['purple', 'orange', 'black', 'black']
    draw_horiz_bars(d, ['yellow'])
    #draw_bipolar(d, 'blue', 'black')
    draw_triskelion(d, ['black', 'red', 'white'], size_ratio=0.9)
    d.save_svg('drawflags/test2.svg')