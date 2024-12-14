"""
Draw stripes for pride flags

All drawing functions will draw in a rectangular area with width "wid" and height "hei",
with the upper left of the area specified by x_start and y_start.

Most of the time, this effective drawing area will be the same as the canvas dimensions.
It matters when drawing one flag inside another flag.

Standardized parameter order:
1. Drawing object
2. List of stripes
3. Effective width and height
4. x and y offsets
5. anything else

And return the bar height (or equivalent).

TO IMPLEMENT
- Tees
- arrowheads
- sideways vees for use with piles
"""

import drawsvg as draw
import math
import doctest
import numpy as np

HORIZONTAL = 'H'
VERTICAL = 'V'
DIAGONAL = 'D'
BEND = 'R' # reverse diagonal
CENTRAL = 'C'
NEUTRAL = 'N'
EMPTY = 'none'

UNSPECIFIED = -1.0

# for convenience in testing
RAINBOW = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']


def get_effective_dimensions(d, wid, hei):
    """
    Helper function. Most of the time we want the height and width of the area we're adding stripes to be the
    same as the canvas. But if we're putting a flag in the middle of an intersex ring, we'll want to change
    the effective dimensions.
    :param d: Drawing object
    :param wid: width parameter - if nonnumeric or negative, use canvas' width
    :param hei: height parameter - if nonnumeric or negative, use canvas' height
    :return: width and height
    """
    if type(wid) not in [int, float] or wid < 0:
        wid = d.width
    if type(hei) not in [int, float] or hei < 0:
        hei = d.height
    return wid, hei


def draw_stripes(d, colours, orientation, wid=UNSPECIFIED, hei=UNSPECIFIED, x_start=0, y_start=0, n_bars = EMPTY,
                 size_ratio=1.0, stretch_ratio=1.0, thick_ratio=1.0):
    """
    Wrapper function to draw any given stripes
    :param d: Drawing object
    :param colours: a list of strings of hex codes for the different bars
    :param wid: width of the area that the bars are being added to
    :param hei: height of the area that the bars are being added to
    :param x_start: the x-coordinate to start drawing bars from. Default is zero.
    :param y_start: the height to start drawing bars from. Default is zero, but if drawing a flag inside another
    you will want to use this parameter
    :param size_ratio: not used, just here to make parameterized function calling standardized
    :return: the width of a stripe
    """
    STRIPES = {HORIZONTAL:draw_horiz_bars,
               VERTICAL:draw_vert_bars,
               DIAGONAL:draw_diagonal_stripes,
               BEND:draw_reverse_diagonal_stripes
               }
    return STRIPES[orientation](d, colours, wid=wid, hei=hei, x_start=x_start, y_start=y_start)


def get_relative_sizes(lst):
    """
    Turn a list of colours into two lists: unique colours and sizes
    :param lst:
    :return:
    >>> get_relative_sizes(['a', 'a'])
    (['a'], [1.0])
    >>> get_relative_sizes(['a','b','a','a'])
    (['a', 'b', 'a'], [0.25, 0.25, 0.5])
    >>> get_relative_sizes(['a', 'a', 'b','a','a'])
    (['a', 'b', 'a'], [0.4, 0.2, 0.4])
    """
    new_colours = []
    last_colour = ''
    how_many_last_colour = 1
    quantities = []
    for i, c in enumerate(lst):
        if c != last_colour:
            new_colours.append(c)
            if i != 0:
                quantities.append(how_many_last_colour)
            last_colour = c
            how_many_last_colour = 1
        else:
            how_many_last_colour += 1
    quantities.append(how_many_last_colour)

    q = np.array(quantities)
    relquants = q / np.sum(q)

    return new_colours, list(relquants)

def draw_horiz_bars(d, colours, wid=UNSPECIFIED, hei=UNSPECIFIED, x_start=0, y_start=0):
    """
    Add horizontal bars to the flag
    :param d: Drawing object
    :param colours: a list of strings of hex codes for the different bars
    :param wid: width of the area that the bars are being added to
    :param hei: height of the area that the bars are being added to
    :param x_start: the x-coordinate to start drawing bars from. Default is zero.
    :param y_start: the height to start drawing bars from. Default is zero, but if drawing a flag inside another
    you will want to use this parameter
    :param fudge: to ensure there's no gaps between flags
    :return: the height of the bars drawn
    >>> d = draw.Drawing(500, 300)
    >>> draw_horiz_bars(d, RAINBOW)
    50.0
    >>> len(d.elements) == len(RAINBOW) and d.elements[-1].args['fill'] == RAINBOW[-1]
    True
    >>> type(d.elements[0])
    <class 'drawsvg.elements.Rectangle'>
    """
    wid, hei = get_effective_dimensions(d, wid, hei)
    new_colours, rel_sizes = get_relative_sizes(colours)

    fudge =  min(1, hei / 1000) # here to make sure no gaps between stripes on hi res flags
    current_height = y_start
    stp_hei = hei
    for i, c in enumerate(new_colours):
        this_height = rel_sizes[i]*hei
        stp_hei = min(this_height, stp_hei)
        rect = draw.Rectangle(x_start, current_height, wid, math.ceil(this_height + fudge), fill=c)
        current_height += this_height
        d.append(rect)
    return stp_hei


def draw_vert_bars(d, colours, wid=UNSPECIFIED, hei=UNSPECIFIED, x_start=0, y_start=0):
    """
    Add vertical bars to the flag
    :param d: Drawing object
    :param colours: a list of strings of hex codes for the different bars
    :param x_start: the x coordinate to start drawing bars from. Default is zero, but if drawing a flag inside another
    you will want to use this parameter
    :param y_start: the y coordinate to start drawing bars from. Default is zero, but if drawing a flag inside another
    you will want to use this parameter
    :param wid: width of the area that the bars are being added to
    :param hei: height of the area that the bars are being added to
    :return: the height of the bars drawn
    >>> d = draw.Drawing(500, 300)
    >>> draw_vert_bars(d, RAINBOW)
    83.33333333333333
    >>> len(d.elements) == len(RAINBOW) and d.elements[-1].args['fill'] == RAINBOW[-1]
    True
    >>> type(d.elements[0])
    <class 'drawsvg.elements.Rectangle'>
    """
    wid, hei = get_effective_dimensions(d, wid, hei)
    new_colours, rel_sizes = get_relative_sizes(colours)

    fudge =  min(1, wid / 1000) # here to make sure no gaps between stripes on hi res flags
    current_width = x_start
    stp_wid = wid
    for i, c in enumerate(new_colours):
        this_width = rel_sizes[i]*wid
        stp_wid = min(this_width, stp_wid)
        rect = draw.Rectangle(current_width, y_start, math.ceil(this_width + fudge), hei, fill=c)
        current_width += this_width
        d.append(rect)
    return stp_wid


def draw_diagonal_stripes(d, colours, wid=UNSPECIFIED, hei=UNSPECIFIED, x_start=0.0, y_start=0.0, fudge=2):
    """
    Draw diagonal stripes in the style of the Magill Disability Pride Flag
    :param d: Drawing object
    :param wid: width of the area you are adding diagonal stripes to
    :param hei: height of the area you are adding diagonal stripes to
    :param colours: list of colours (str, hex codes) for the stripes
    :return: stripe width
    >>> d = draw.Drawing(500, 300)
    >>> draw_diagonal_stripes(d, RAINBOW)
    166.66666666666666
    >>> len(d.elements) == len(RAINBOW) and d.elements[-1].args['fill'] == RAINBOW[-1]
    True
    >>> type(d.elements[0])
    <class 'drawsvg.elements.Path'>
    """
    wid, hei = get_effective_dimensions(d, wid, hei)

    stripe_width = (2 * wid) / (len(colours))
    fudge = fudge * len(colours) / 10
    for i, c in enumerate(colours):
        up_left = -wid + math.floor(i * stripe_width) + x_start
        up_right = up_left + math.ceil(stripe_width + fudge)
        up_y = 0 + y_start

        down_y = hei + y_start
        down_left = 0 + math.floor(i * stripe_width) + x_start
        down_right = down_left + math.ceil(stripe_width + fudge)
        # the -1/+1 offset is to stop streaks from appearing when there are many stripes

        p = draw.Path(fill=c)  # draw the stripe as a Path with four points
        p.M(up_left, up_y)
        p.L(down_left, down_y).L(down_right, down_y)
        p.L(up_right, up_y).L(up_right, up_y)
        p.Z()
        d.append(p)
    return stripe_width


def draw_reverse_diagonal_stripes(d, colours, wid=UNSPECIFIED, hei=UNSPECIFIED, offset=2, x_start=0.0, y_start=0.0):
    """
    Draw diagonal stripes, in the mirror image orientation of the Magill Disability Pride Flag
    :param d: Drawing object
    :param wid: width of the area you are adding diagonal stripes to
    :param hei: height of the area you are adding diagonal stripes to
    :param colours: list of colours (str, hex codes) for the stripes
    :return: stripe width
    >>> d = draw.Drawing(500, 300)
    >>> draw_reverse_diagonal_stripes(d, RAINBOW)
    166.66666666666666
    >>> len(d.elements) == len(RAINBOW) and d.elements[-1].args['fill'] == RAINBOW[-1]
    True
    >>> type(d.elements[0])
    <class 'drawsvg.elements.Path'>
    """
    wid, hei = get_effective_dimensions(d, wid, hei)

    stripe_width = (2 * wid) / (len(colours))
    offset = offset * len(colours) / 10
    for i, c in enumerate(colours):
        up_left = 0 + math.floor(i * stripe_width) + x_start
        up_right = up_left + math.ceil(stripe_width + offset)
        up_y = 0 + y_start

        down_y = hei + y_start
        down_left = -wid + math.floor(i * stripe_width) + x_start
        down_right = down_left + math.ceil(stripe_width + offset)
        # the -1/+1 offset is to stop streaks from appearing when there are many stripes

        p = draw.Path(fill=c)  # draw the stripe as a Path with four points
        p.M(up_left, up_y)
        p.L(down_left, down_y).L(down_right, down_y)
        p.L(up_right, up_y).L(up_right, up_y)
        p.Z()
        d.append(p)
    return stripe_width


def draw_vees(d, colours,
              wid=UNSPECIFIED, hei=UNSPECIFIED, x_start=0, y_start=0,
              size_ratio = 1.0, stretch_ratio=1.0, thick_ratio=1.0, orientation=VERTICAL):
    """
    Draw concentric Vs in the style of the varsex flag
    :param d: Drawing object
    :param colours: list of colours as strings
    :return: the line width
    >>> d = draw.Drawing(500, 300)
    >>> draw_vees(d, RAINBOW)
    45.45454545454545
    >>> len(d.elements) == len(RAINBOW) and d.elements[-1].args['fill'] == RAINBOW[-1]
    True
    >>> type(d.elements[0])
    <class 'drawsvg.elements.Path'>
    """
    wid, hei = get_effective_dimensions(d, wid, hei)

    sw = (wid/2)/(len(colours)-0.5) # will need trig
    mid_x = wid/2

    aspect_ratio = (wid/2)/hei

    line_width = sw
    line_height = sw/aspect_ratio

    fudge = min(2, hei/1000)
    for i, c in enumerate(colours):
        p = draw.Path(stroke_width=0, fill=c, stroke_linecap='square')
        p.M(line_width * i, y_start)
        p.L(mid_x, hei - line_height*i + fudge)  # go to middle
        p.L(wid - line_width * i, y_start)
        p.L(wid - line_width * (i+1), y_start)  # turn back
        p.L(mid_x, hei - line_height*(i+1))  # back to middle
        p.L(line_width * (i+1), y_start)
        p.L(line_width * i, y_start).Z()
        d.append(p)
    return line_width


def draw_chevrons(d, colours,
                  wid=UNSPECIFIED, hei=UNSPECIFIED, x_start=0, y_start=0,
                  size_ratio=1.0, stretch_ratio=1.0, thick_ratio=1.0, orientation=VERTICAL):
    """
    Draw a series of chevrons with the colours provided by colours
    :param d: Drawing object
    :param colours: list of strings for the stripe colours
    :param wid: width that makes up the area the chevrons are being drawn into
    :param hei: height that makes up the area the chevrons are being drawn into
    :param x_start: the x-coordinate of the upper left corner of the rectangular area the chevrons are being drawn into
    :param y_start: the y-coordinate of the upper left corner of the rectangular area the chevrons are being drawn into
    :return: chevron height
    >>> d = draw.Drawing(500, 300)
    >>> draw_chevrons(d, RAINBOW)
    22.5
    >>> len(d.elements) == len(RAINBOW) and d.elements[-1].args['fill'] == RAINBOW[-1]
    True
    >>> type(d.elements[0])
    <class 'drawsvg.elements.Path'>
    """
    wid, hei = get_effective_dimensions(d, wid, hei)
    mid_x = wid/2

    downward_factor = 2 # how much lower the middle of the V is from the top (in units of line_height)

    first_height = (1/5)*hei + y_start
    bottom_height = hei - first_height
    chevron_height = bottom_height - first_height

    leftmost = x_start
    rightmost = leftmost + wid
    line_height = chevron_height / (len(colours) +  downward_factor)

    fudge = min(1, hei/1000) # just so there's no gap between lines
    for i, colour in enumerate(colours):
        p = draw.Path(fill=colour)
        lines_top = first_height + i*line_height
        lines_midtop = lines_top + downward_factor*line_height
        lines_bottom = lines_top + line_height + fudge
        lines_midbottom = lines_midtop + line_height + fudge
        p.M(leftmost, lines_top) # start at upper left
        p.L(mid_x, lines_midtop).L(rightmost, lines_top) # the top of the V
        p.L(rightmost, lines_bottom) # go down
        p.L(mid_x, lines_midbottom).L(leftmost, lines_bottom) # bottom of the V
        p.L(leftmost, lines_top).Z() #return to origin
        d.append(p)
    return line_height


def draw_concentric_rectangles(d, colours,
              wid=UNSPECIFIED, hei=UNSPECIFIED, x_start=0, y_start=0,
              size_ratio = 1.0, stretch_ratio=1.0, thick_ratio=1.0, orientation=VERTICAL):
    """
    Draw concentric rectangles from the outside to the inside
    :param d: Drawing object
    :param colours: list of colours as strings
    :param wid: width that makes up the area that is being drawn into (in pixels)
    :param hei: height that makes up the area that is being drawn into (in pixels)
    :param x_start: the x-coordinate of the upper left corner of the rectangular area that is being drawn into
    :param y_start: the y-coordinate of the upper left corner of the rectangular area that is being drawn into
    :return: stripe height
    >>> d = draw.Drawing(500, 300)
    >>> draw_concentric_rectangles(d, RAINBOW)
    25.0
    >>> len(d.elements) == len(RAINBOW) and d.elements[-1].args['fill'] == RAINBOW[-1]
    True
    >>> type(d.elements[0])
    <class 'drawsvg.elements.Path'>
    """
    wid, hei = get_effective_dimensions(d, wid, hei)

    line_height = (hei/2)/len(colours)
    line_width = (wid/2)/len(colours)
    leftmost = x_start
    topmost = y_start

    for i, colour in enumerate(colours):
        p = draw.Path(fill=colour)
        # y coordinates
        outer_top = topmost + i*line_height
        inner_top = outer_top + line_height
        outer_bottom = hei - i*line_height
        inner_bottom = outer_bottom - line_height
        # x coordinates
        outer_left = leftmost + i*line_width
        inner_left = outer_left + line_width
        outer_right = wid - i*line_width
        inner_right = outer_right - line_width
        # the path
        p.M(outer_left, outer_top) # start in upper left corner
        p.L(outer_right, outer_top).L(outer_right, outer_bottom).L(outer_left, outer_bottom) # go around
        p.L(outer_left, inner_top).L(inner_left, inner_top) # start on the inner
        p.L(inner_left, inner_bottom).L(inner_right, inner_bottom).L(inner_right, inner_top) # circle back
        p.L(outer_left, inner_top).L(outer_left, outer_top).Z() # return to origin
        d.append(p)
    return line_height


def get_triangle_coords(rad, arc_width, i, cent_x, cent_y, offset=-90):
    """
    Helper function for drawing segmented rings, Seychelles flags, and other polar math
    :param rad: radius
    :param arc_width: the arc width of a segment
    :param i: which segment we're on
    :param cent_x: the coordinate of the centre (x)
    :param cent_y: the coordinate of the centre (y)
    :param offset: angle in degrees of offset from where we start the segmentation
    :return: coordinates
    >>> get_triangle_coords(10, 45, 1, 0, -45)
    (7.0710678118654755, -52.071067811865476)
    """
    x = rad * math.cos(math.radians(offset + arc_width * i)) + cent_x
    y = rad * math.sin(math.radians(offset + arc_width * i)) + cent_y
    return x, y


def draw_seychelles(d, colours,
              wid=UNSPECIFIED, hei=UNSPECIFIED, x_start=0, y_start=0,
              size_ratio = 1.0, stretch_ratio=1.0, thick_ratio=1.0, orientation=VERTICAL):
    """
    Draw stripes like the flag of Seychelles
    :param d: Drawing object
    :param colours: list of colours as strings
    :param wid: width that makes up the area that is being drawn into (in pixels)
    :param hei: height that makes up the area that is being drawn into (in pixels)
    :param x_start: the x-coordinate of the upper left corner of the rectangular area that is being drawn into
    :param y_start: the y-coordinate of the upper left corner of the rectangular area that is being drawn into
    :return: stripe height
    >>> d = draw.Drawing(500, 300)
    >>> draw_seychelles(d, RAINBOW)
    129.40952255126038
    >>> len(d.elements) == len(RAINBOW) and d.elements[-1].args['fill'] == RAINBOW[-1]
    True
    >>> type(d.elements[0])
    <class 'drawsvg.elements.Path'>
    """
    wid, hei = get_effective_dimensions(d, wid, hei)
    leftmost = x_start
    bottommost = hei + y_start

    ang_offset = -90
    arc_width = 90/len(colours)
    radius = 1.5*max(wid, hei)

    for i, colour in enumerate(colours):
        p = draw.Path(fill=colour)
        stop1 = get_triangle_coords(radius, arc_width, i, cent_x=leftmost, cent_y=bottommost, offset=ang_offset)
        stop2 = get_triangle_coords(radius, arc_width, i + 1, cent_x=leftmost, cent_y=bottommost, offset=ang_offset)
        p.M(leftmost, bottommost) # start from bottom left
        p.L(*stop1).L(*stop2) # draw a triangle that will go over the edges of the canvas
        p.L(leftmost, bottommost).Z() # return to origin
        d.append(p)
    last_height = wid * math.sin(math.radians(arc_width))
    return last_height


def angle_offset_for_orientation(orientation_flag):
    """
    Turn orientation string into an angle (in degrees) to offset a starburst/segmented ring/etc
    :param orientation_flag: one of CENTRAL, HORIZONTAL, DIAGONAL, VERTICAL
    :return: the angle in degrees to offset with
    >>> angle_offset_for_orientation(HORIZONTAL)
    180
    """
    if type(orientation_flag) in [int, float]:
        return orientation_flag
    if orientation_flag == CENTRAL:
        orientation_flag = 90 # for five segments, will give a Y shape
    elif HORIZONTAL in str(orientation_flag):
        orientation_flag = 180 # for five segments -< style shape
    elif VERTICAL in str(orientation_flag): # for five segments, will give an upside Y style
        orientation_flag = -90
    elif orientation_flag == DIAGONAL:
        orientation_flag = -45
    elif orientation_flag == BEND:
        orientation_flag = 45
    else:
        orientation_flag = 0
    return orientation_flag


def draw_starburst(d, colours, wid=UNSPECIFIED, hei=UNSPECIFIED, x_start=0, y_start=0, orientation=VERTICAL):
    """
    Draw stripes as a starburst from the centre
    :param d: Drawing object
    :param colours: list of colours as strings
    :param wid: width that makes up the area that is being drawn into (in pixels)
    :param hei: height that makes up the area that is being drawn into (in pixels)
    :param x_start: the x-coordinate of the upper left corner of the rectangular area that is being drawn into
    :param y_start: the y-coordinate of the upper left corner of the rectangular area that is being drawn into
    :return: perimiter length of a segment
    >>> d = draw.Drawing(500, 300)
    >>> draw_starburst(d, RAINBOW)
    266.6666666666667
    >>> len(d.elements) == len(RAINBOW) and d.elements[-1].args['fill'] == RAINBOW[-1]
    True
    >>> type(d.elements[0])
    <class 'drawsvg.elements.Path'>
    """
    wid, hei = get_effective_dimensions(d, wid, hei)
    centre_x = wid/2
    centre_y = hei/2

    ang_offset = angle_offset_for_orientation(orientation)
    arc_width = 360/len(colours)
    radius = 1.5*max(wid, hei)
    for i, colour in enumerate(colours):
        p = draw.Path(fill=colour)
        stop1 = get_triangle_coords(radius, arc_width, i, cent_x=centre_x, cent_y=centre_y, offset=ang_offset)
        stop2 = get_triangle_coords(radius, arc_width, i + 1, cent_x=centre_x, cent_y=centre_y, offset=ang_offset)
        p.M(centre_x, centre_y) # start from bottom left
        p.L(*stop1).L(*stop2) # draw a triangle that will go over the edges of the canvas
        p.L(centre_x, centre_y).Z() # return to origin
        d.append(p)
    return (2*wid + 2*hei)/len(colours)


def draw_concentric_circles(d, colours,
                            wid=UNSPECIFIED, hei=UNSPECIFIED, x_start=0, y_start=0,
                            size_ratio=1.0, stretch_ratio=1.0, thick_ratio=1.0, orientation=VERTICAL):
    """
    Draw concentric circles from the outside inward
    :param d: Drawing object
    :param colours: list of colours as strings
    :param wid: width that makes up the area that is being drawn into (in pixels)
    :param hei: height that makes up the area that is being drawn into (in pixels)
    :param x_start: the x-coordinate of the upper left corner of the rectangular area that is being drawn into
    :param y_start: the y-coordinate of the upper left corner of the rectangular area that is being drawn into
    :return: perimiter length of a segment
    >>> d = draw.Drawing(500, 300)
    >>> draw_concentric_circles(d, RAINBOW)
    41.666666666666664
    >>> len(d.elements) == len(RAINBOW) and d.elements[-1].args['stroke'] == RAINBOW[-1]
    True
    >>> type(d.elements[0])
    <class 'drawsvg.elements.Circle'>
    """
    wid, hei = get_effective_dimensions(d, wid, hei)
    centre_x = wid/2
    centre_y = hei/2

    radius = (max(wid, hei) /2 )/ len(colours)
    stroke_wid = radius
    for i, colour in enumerate(colours):
        this_radius = radius*(len(colours)-i) - stroke_wid/2
        d.append(draw.Circle(centre_x, centre_y, this_radius, stroke=colours[i], stroke_width=stroke_wid))
    return stroke_wid


def draw_concentric_ellipses(d, colours,
                             wid=UNSPECIFIED, hei=UNSPECIFIED, x_start=0, y_start=0,
                             size_ratio=1.0, stretch_ratio=1.0, thick_ratio=1.0, orientation=VERTICAL):
    """
    Draw concentric circles from the outside inward
    :param d: Drawing object
    :param colours: list of colours as strings
    :param wid: width that makes up the area that is being drawn into (in pixels)
    :param hei: height that makes up the area that is being drawn into (in pixels)
    :param x_start: the x-coordinate of the upper left corner of the rectangular area that is being drawn into
    :param y_start: the y-coordinate of the upper left corner of the rectangular area that is being drawn into
    :return: perimiter length of a segment
    >>> d = draw.Drawing(500, 300)
    >>> draw_concentric_ellipses(d, RAINBOW)
    41.666666666666664
    >>> len(d.elements) == len(RAINBOW) and d.elements[-1].args['stroke'] == RAINBOW[-1]
    True
    >>> type(d.elements[0])
    <class 'drawsvg.elements.Ellipse'>
    """
    wid, hei = get_effective_dimensions(d, wid, hei)
    centre_x = wid/2
    centre_y = hei/2

    x_radius = (wid/2)/len(colours)
    y_radius = (hei/2)/len(colours)

    stroke_wid = max(x_radius, y_radius)
    for i, colour in enumerate(colours):
        this_x_radius = x_radius*(len(colours)-i) - stroke_wid/2
        this_y_radius = y_radius*(len(colours)-i) - stroke_wid/2
        d.append(draw.Ellipse(centre_x, centre_y, this_x_radius, this_y_radius, stroke=colours[i], stroke_width=stroke_wid))
    return stroke_wid


def draw_concentric_beziers(d, colours,
                            wid=UNSPECIFIED, hei=UNSPECIFIED, x_start=0, y_start=0,
                            size_ratio=1.0, stretch_ratio=1.0, thick_ratio=1.0, orientation=VERTICAL):
    """
    Draw concentric bezier curves in the style of the Mental Health flag
    :param d: Drawing object
    :param colours: list of colours as strings
    :param wid: width that makes up the area that is being drawn into (in pixels)
    :param hei: height that makes up the area that is being drawn into (in pixels)
    :param x_start: the x-coordinate of the upper left corner of the rectangular area that is being drawn into
    :param y_start: the y-coordinate of the upper left corner of the rectangular area that is being drawn into
    :return: perimiter length of a segment
    >>> d = draw.Drawing(500, 300)
    >>> draw_concentric_circles(d, RAINBOW)
    41.666666666666664
    >>> len(d.elements) == len(RAINBOW) and d.elements[-1].args['stroke'] == RAINBOW[-1]
    True
    >>> type(d.elements[0])
    <class 'drawsvg.elements.Circle'>
    """
    wid, hei = get_effective_dimensions(d, wid, hei)
    right = x_start
    bottom = y_start+hei

    hypotenuse = math.sqrt( wid**2 + hei**2)
    stroke_wid = hypotenuse / len(colours)

    paths = []
    for i, colour in enumerate(colours):
        x = right+(stroke_wid/2) + i*stroke_wid
        y = bottom-(stroke_wid/2) - i*stroke_wid

        p = draw.Path(stroke_width=stroke_wid, stroke=colour, fill=colour)
        p.M(x, bottom)
        p.Q(x, y, right, y) # draw the curve
        p.L(right, bottom).L(x, bottom).Z() # close the curve so there's no gaps in colour between stripes
        paths.append(p)

    # add the stripes in reversed order to the drawing object so the outer stripes are the bottom layers
    for p in reversed(paths):
        d.append(p)

    '''
    y_radius = ( hei )/ len(colours)
    x_radius = wid/len(colours)
    for i, colour in enumerate(colours):
        this_x_radius = x_radius*(len(colours)-i) - stroke_wid/2
        this_y_radius = y_radius*(len(colours)-i) - stroke_wid/2
        d.append(draw.Ellipse(right, bottom, this_x_radius, this_y_radius, stroke=colours[i], stroke_width=stroke_wid))
    '''
    return stroke_wid


def draw_concentric_infinities(d, colours, bg_colour,
                             wid=UNSPECIFIED, hei=UNSPECIFIED, x_start=0, y_start=0,
                             size_ratio=1.0, stretch_ratio=1.0, thick_ratio=1.0, orientation=VERTICAL):
    """
    Draw concentric infinity loops in the style of the Autistic Pride Day logo.
    :param d: drawing object
    :param fill_colour: the stripes of the infinity
    :param bg_colour: the background colour
    :param wid: width of area the symbol is being added to
    :param hei: height of the area the symbol is being added to
    :param size_ratio: scaling factor (radius)
    :param stretch_ratio: how far apart the two midpoints are
    :return: none
    """
    wid, hei = get_effective_dimensions(d, wid, hei)
    total_thickness = stretch_ratio*size_ratio*(hei / 3)

    midy = hei/2
    midx = wid/2
    left_centre = midx - total_thickness
    right_centre = midx + total_thickness

    each_thickness = total_thickness /(len(colours) + 1)
    greatest_radius = size_ratio*(hei/2) - each_thickness

    # left concentric circles
    for i, colour in enumerate(colours):
        this_radius = greatest_radius - i*each_thickness
        d.append(draw.Circle( left_centre, midy, this_radius, stroke=colour, stroke_width=each_thickness, fill='none' ))

    # right concentric circles
    for i, colour in enumerate(reversed(colours)):
        this_radius = greatest_radius - i*each_thickness
        d.append(draw.Circle( right_centre, midy, this_radius, stroke=colour, stroke_width=each_thickness, fill='none' ))

    # add background-coloured lines to give the cut-off effect
    linedraws = [bg_colour] + colours + [bg_colour]
    for i, colour in enumerate(linedraws):
        this_outer_radius = greatest_radius - (i-1)*each_thickness
        this_inner_radius = greatest_radius - (len(colours)-i)*each_thickness

        lower_angle = math.degrees(math.asin(1.5/2)) + 90
        upper_angle = lower_angle + 180-10
        lower_angle -= 15

        arcshare = 120 # doesn't actually matter
        upper_left = get_triangle_coords(this_outer_radius, arcshare, 0, left_centre, midy, upper_angle)
        lower_right = get_triangle_coords(this_inner_radius, arcshare, 0, right_centre, midy, lower_angle)

        angle_dist_for_control_pts = -17
        other_side_radius = greatest_radius - (i-2)*each_thickness
        cx1 = get_triangle_coords(other_side_radius, arcshare, 0, left_centre, midy, 0+angle_dist_for_control_pts) #upper_angle) #-90+45+15+15)
        next_outer_radius = this_inner_radius + each_thickness
        cx2 = get_triangle_coords(next_outer_radius, arcshare, 0, right_centre, midy, 180+angle_dist_for_control_pts) #lower_angle)#-60+90-15)

        # wavy lines between them
        p = draw.Path(stroke=colour, stroke_width=each_thickness, fill=colour, stroke_linecap='round')
        p.M(*upper_left)
        p.C(*cx1, *cx2, *lower_right)
        d.append(p)


def draw_concentric_tees(d, colours,
                             wid=UNSPECIFIED, hei=UNSPECIFIED, x_start=0, y_start=0,
                             size_ratio=1.0, stretch_ratio=1.0, thick_ratio=1.0, orientation=VERTICAL):
    """
    Draw concentric circles from the outside inward
    :param d: Drawing object
    :param colours: list of colours as strings
    :param wid: width that makes up the area that is being drawn into (in pixels)
    :param hei: height that makes up the area that is being drawn into (in pixels)
    :param x_start: the x-coordinate of the upper left corner of the rectangular area that is being drawn into
    :param y_start: the y-coordinate of the upper left corner of the rectangular area that is being drawn into
    :return: perimiter length of a segment
    """
    wid, hei = get_effective_dimensions(d, wid, hei)
    centre_x = wid/2

    tee_wid = hei / (len(colours)+1)
    start_x, start_y = 0, 0

    # don't do the last one in the loop because it's an irregular size
    for i, colour in enumerate(colours[:-1]):
        p = draw.Path(fill=colour)
        top = start_y + i*tee_wid
        bottom = top + tee_wid
        outer_left = centre_x - (i-0.5)*tee_wid
        inner_left = outer_left - tee_wid
        # left side
        p.M(start_x, top).L(outer_left, top).L(outer_left, hei).L(inner_left, hei).L(inner_left, bottom)
        p.L(start_x, bottom).L(start_x, top).Z()
        d.append(p)

        # right side
        p = draw.Path(fill=colour)
        inner_right = centre_x + (i-0.5)*tee_wid
        outer_right = inner_right + tee_wid
        p.M(wid, top).L(inner_right, top).L(inner_right, hei).L(outer_right, hei).L(outer_right, bottom)
        p.L(wid, bottom).L(wid, top).Z()
        d.append(p)

    # left
    p = draw.Path(fill=colours[-1])
    p.M(start_x, bottom)
    p.L(inner_left, bottom).L(inner_left, hei).L(start_x, hei).L(start_x, bottom).Z()
    d.append(p)

    # right
    p = draw.Path(fill=colours[-1])
    p.M(wid, bottom)
    p.L(outer_right, bottom).L(outer_right, hei).L(wid, hei).L(wid, bottom).Z()
    d.append(p)
    return tee_wid


def draw_ally_stripes(d, colours,
                             wid=UNSPECIFIED, hei=UNSPECIFIED, x_start=0, y_start=0,
                             size_ratio=1.0, stretch_ratio=1.0, thick_ratio=1.0, orientation=VERTICAL):
    """
    Draw a chevron/vee in the style of the ally flag, but with stripes!
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

    clip = draw.ClipPath()
    p = draw.Path()
    p.M(x_start, hei) # bottom left
    p.L(x_start + midx, y_start) # top of A
    p.L(x_start + wid, hei) # bottom right
    p.L(inner_right, hei) # loop back
    p.L(x_start + midx, lower_height)
    p.L(inner_left, hei)
    clip.append(p)

    fudge =  min(1, hei / 1000) # here to make sure no gaps between stripes on hi res flags
    stp_hei = hei / len(colours)
    for i in range(len(colours)):
        d.append \
            (draw.Rectangle(x_start, round(y_start + i * stp_hei), wid, math.ceil(stp_hei + fudge),
                            fill=colours[i % len(colours)], clip_path=clip))
    return stp_hei



def draw_armpit_stripes(d, colours,
                             wid=UNSPECIFIED, hei=UNSPECIFIED, x_start=0, y_start=0,
                             size_ratio=1.0, stretch_ratio=1.0, thick_ratio=1.0, orientation=VERTICAL):
    """
    Draw stripes in the style of the armpit flag
    :param d: Drawing object
    :param colours: the colours used
    :param wid: width of the area we are working with
    :param hei: height of the area we are working with
    :param x_start: the x-coordinate of the upper left corner of the rectangular area that is being drawn into
    :param y_start: the y-coordinate of the upper left corner of the rectangular area that is being drawn into
    :param size_ratio: size factor
    :return:
    """
    wid, hei = get_effective_dimensions(d, wid, hei)
    ew = draw_vert_bars(d, colours, wid=wid/3, x_start=wid*(2/3))

    leftmost = x_start
    rightmost = wid - ew*len(colours)

    line_hei = ew*((2*wid/3)/hei)*0.5
    line_wid = ew

    bottommost = hei + x_start - line_hei
    top = y_start
    fudge = line_hei/10
    for i, c in enumerate(colours):
        p = draw.Path(fill=c)
        p.M(leftmost, bottommost - i*line_hei) # lower left
        p.L(rightmost, top - (i-1) * line_hei+fudge) # lower right
        p.L(rightmost, top - i*line_hei) # upper right
        p.L(leftmost, bottommost - (i+1)*line_hei - fudge)
        d.append(p)

    '''
    p = draw.Path(fill=colours[0])
    p.M(leftmost, bottommost)
    p.L(rightmost, top+line_hei)
    p.L(rightmost, top)
    p.L(leftmost, bottommost-line_hei)
    d.append(p)
    '''




if __name__ == '__main__':
    wid = 500
    hei = 300
    d = draw.Drawing(wid, hei)
    draw_horiz_bars(d, RAINBOW)
    draw_diagonal_stripes(d, ['none', 'grey', 'red', 'yellow', 'white', 'blue', 'green', 'grey', 'none'], wid=wid/2, hei=hei/2, x_start=wid / 2)
    draw_vees(d, RAINBOW)
    d.save_png('drawflags/test.png')

    d = draw.Drawing(wid, hei)
    draw_vert_bars(d,['black'])
    #draw_chevrons(d, stripes)
    #draw_concentric_rectangles(d, stripes, y_start=50)
    draw_concentric_tees(d, RAINBOW[:3])
    d.save_png('drawflags/test2.png')
    d.save_svg('drawflags/test.svg')

    doctest.testmod()