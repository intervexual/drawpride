from pride_rings import *


def draw_arbitrary_star(d, primary_colour, secondary_colour='none', num_points=5, square=True,
              wid=UNSPECIFIED, hei=UNSPECIFIED, x_start=0, y_start=0,
              size_ratio = 1.0, stretch_ratio=0.58, thick_ratio=1.0, orientation=VERTICAL):
    """
    Draw a star of arbitrary points
    :param d: Drawing object
    :param primary_colour: the fill of the star
    :param secondary_colour: the outline of the star
    :param wid: width of the area we are working with
    :param hei: height of the area we are working with
    :param x_start: the x-coordinate of the upper left corner of the rectangular area that is being drawn into
    :param y_start: the y-coordinate of the upper left corner of the rectangular area that is being drawn into
    :param size_ratio: size factor
    :param stretch_ratio: how spiky the star is. 0.58 for Jewish star of david. 0.5 for regular 5-point star.
    :param thick_ratio: scaling factor for stroke thickness. Defaults to hei/100.
    :return: the height of the top/bottom lines
    """
    #secondary_size = 0.58*stretch_ratio
    rotateby = angle_offset_for_orientation(orientation)
    wid, hei = get_effective_dimensions(d, wid, hei)

    midx = x_start + wid/2
    midy = y_start + hei/2

    arc_width = 360 / num_points
    outer_radius = size_ratio*hei/4
    inner_radius = outer_radius*stretch_ratio

    if secondary_colour != 'none':
        sw = thick_ratio*hei/100
    else:
        sw = 0

    ang_offset = rotateby
    if square:
        p = draw.Path(fill=primary_colour, stroke=secondary_colour, stroke_width=sw)
    else:
        p = draw.Path(fill=primary_colour, stroke=secondary_colour, stroke_width=sw, transform=f'scale({wid/hei}, 1')
        midx -= midx*(wid/hei)/4
    for i in range(num_points):
        stop1 = get_triangle_coords(outer_radius, arc_width, i, cent_x=midx, cent_y=midy, offset=ang_offset)
        stop2 = get_triangle_coords(inner_radius, arc_width, i, cent_x=midx, cent_y=midy, offset=ang_offset+arc_width/2)
        if i == 0:
            p.M(*stop1)
        else:
            p.L(*stop1)
        p.L(*stop2)
    p.Z()
    d.append(p)
    return sw


def draw_fivesided_star(d, primary_colour, secondary_colour='none',
              wid=UNSPECIFIED, hei=UNSPECIFIED, x_start=0, y_start=0,
              size_ratio = 1.0, stretch_ratio=1.0, thick_ratio=1.0, orientation=VERTICAL):
    """
    Draw a five-pointed star
    :param d: Drawing object
    :param primary_colour: the fill of the star
    :param secondary_colour: the outline of the star
    :param wid: width of the area we are working with
    :param hei: height of the area we are working with
    :param x_start: the x-coordinate of the upper left corner of the rectangular area that is being drawn into
    :param y_start: the y-coordinate of the upper left corner of the rectangular area that is being drawn into
    :param size_ratio: size factor
    :param stretch_size: how spiky the star is. 0.385 if you want a horizontal line at mid-top
    :param thick_ratio: scaling factor for the stroke width.
    :return: the height of the top/bottom lines
    """
    return draw_arbitrary_star(d, primary_colour, secondary_colour=secondary_colour, num_points=5,
                               wid=wid, hei=hei, x_start=x_start, y_start=y_start, size_ratio=size_ratio,
                               orientation=orientation, stretch_ratio=stretch_ratio*0.5, thick_ratio=thick_ratio)


def draw_sevensided_star(d, primary_colour, secondary_colour='none',
              wid=UNSPECIFIED, hei=UNSPECIFIED, x_start=0, y_start=0,
              size_ratio = 1.0, stretch_ratio=1.0, thick_ratio=1.0, orientation=VERTICAL):
    """
    Draw a seven pointed star polygon in the style of the morvigender flag
    https://genderqueer-dream.tumblr.com/post/638442638940504064/beyond-mogai-pride-flags-morvivgender-a
    :param d: Drawing object
    :param primary_colour: the fill of the star
    :param secondary_colour: the outline of the star
    :param wid: width of the area we are working with
    :param hei: height of the area we are working with
    :param x_start: the x-coordinate of the upper left corner of the rectangular area that is being drawn into
    :param y_start: the y-coordinate of the upper left corner of the rectangular area that is being drawn into
    :param size_ratio: size factor (radius)
    :param stretch_size: how spiky the star is
    :param thick_ratio: scaling factor for the stroke width.
    :return: the height of the top/bottom lines
    """
    return draw_arbitrary_star_trace(d,   primary_colour, secondary_colour=secondary_colour, num_points=7, offset=3,
                                     wid=wid, hei=hei, x_start=x_start, y_start=y_start, size_ratio=size_ratio,
                                     orientation=orientation,
                                     thick_ratio=thick_ratio)


def draw_australian_star(d, primary_colour, secondary_colour='none',
                         wid=UNSPECIFIED, hei=UNSPECIFIED, x_start=0, y_start=0,
                         size_ratio=1.0, stretch_ratio=1.0, thick_ratio=1.0, orientation=VERTICAL):
    """
    Draw a seven-pointed star in the style of the Australian flag
    :param d: Drawing object
    :param primary_colour: the fill of the star
    :param secondary_colour: the outline of the star
    :param wid: width of the area we are working with
    :param hei: height of the area we are working with
    :param x_start: the x-coordinate of the upper left corner of the rectangular area that is being drawn into
    :param y_start: the y-coordinate of the upper left corner of the rectangular area that is being drawn into
    :param size_ratio: size factor used for the radii of the stars
    :param stretch_size: how spiky the stars are. Set to the default Aussie star (0.45).
    :param thick_ratio: scaling factor for stroke width. Set to default Aussie star.
    :return: the height of the top/bottom lines
    """
    secondary_size = 0.45
    return draw_arbitrary_star(d, primary_colour, secondary_colour=secondary_colour, num_points=7,
                               wid=wid, hei=hei, x_start=x_start, y_start=y_start, size_ratio=size_ratio,
                               orientation=orientation, stretch_ratio=secondary_size, thick_ratio=thick_ratio)


def draw_southern_cross(d, primary_colour, secondary_colour='none',
                         wid=UNSPECIFIED, hei=UNSPECIFIED, x_start=0, y_start=0,
                         size_ratio=1.0, stretch_ratio=1.0, thick_ratio=1.0, orientation=VERTICAL):
    """
    Draw the Southern Cross like on the Australian flag
    :param d: Drawing object
    :param primary_colour: the fill of the star
    :param secondary_colour: the outline of the star
    :param wid: width of the area we are working with
    :param hei: height of the area we are working with
    :param x_start: the x-coordinate of the upper left corner of the rectangular area that is being drawn into
    :param y_start: the y-coordinate of the upper left corner of the rectangular area that is being drawn into
    :param size_ratio: size factor used for the radii of the stars
    :param stretch_size: how spiky the stars are. Set to the default Aussie star (0.45).
    :param thick_ratio: scaling factor for stroke width. Set to default Aussie star.
    :return: the height of the top/bottom lines
    """
    wid, hei = get_effective_dimensions(d, wid, hei)
    midx = x_start + wid/2
    midy = y_start + hei/2

    if type(primary_colour) != list:
        primary_colour = [primary_colour]*5

    sw = thick_ratio*hei/100

    # top star is midx and about hei/6?
    top_offs = 2*hei/6
    starsize = 0.3
    draw_australian_star(d, primary_colour[0], secondary_colour,
                         wid=wid/2, hei=hei, x_start=midx/2, y_start=-top_offs,
                         size_ratio=starsize, thick_ratio=thick_ratio, stretch_ratio=stretch_ratio)

    # lower star is also midx
    draw_australian_star(d, primary_colour[4], secondary_colour,
                         wid=wid/2, hei=hei, x_start=midx/2, y_start=top_offs,
                         size_ratio=starsize, thick_ratio=thick_ratio, stretch_ratio=stretch_ratio)

    # left star is at wid/4 and about 2/3 hei?
    leftward = hei*0.25
    left_y = hei*0.065
    draw_australian_star(d, primary_colour[2], secondary_colour,
                         wid=wid/2, hei=hei, x_start=(midx/2)-leftward, y_start=-left_y,
                         size_ratio=starsize, thick_ratio=thick_ratio, stretch_ratio=stretch_ratio)

    # right star is at .75wid and higher than left
    right_y = hei*0.125
    rightward = hei*0.215
    draw_australian_star(d, primary_colour[1], secondary_colour,
                         wid=wid/2, hei=hei, x_start=(midx/2)+rightward, y_start=-right_y,
                         size_ratio=starsize, thick_ratio=thick_ratio, stretch_ratio=stretch_ratio)

    # and then the little star
    small_y = hei*0.05
    small_x = hei*0.09
    draw_fivesided_star(d, primary_colour[3], secondary_colour,
                        wid=wid/2, hei=hei, x_start=(midx/2)+small_x, y_start=small_y,
                        size_ratio=starsize/2, stretch_ratio=0.475, thick_ratio=thick_ratio)



def draw_arbitrary_star_trace(d, primary_colour, secondary_colour='none',  num_points=5, offset=2,
                        wid=UNSPECIFIED, hei=UNSPECIFIED, x_start=0, y_start=0,
                        size_ratio=1.0, secondary_size=0.58, thick_ratio=1.0, orientation=VERTICAL, square=True, sw=0):
    """
    Draw a star of arbitrary points that is the traced out kinda star like a Star of David, with rounded edges
    :param d: Drawing object
    :param primary_colour: the fill of the star
    :param secondary_colour: the outline of the star
    :param wid: width of the area we are working with
    :param hei: height of the area we are working with
    :param x_start: the x-coordinate of the upper left corner of the rectangular area that is being drawn into
    :param y_start: the y-coordinate of the upper left corner of the rectangular area that is being drawn into
    :param size_ratio: size factor. The radius of the star.
    :param stretch_ratio: How spiky the star is. 0.58 for Jewish star of david. 0.5 for regular 5-point star.
    :param thick_ratio: scaling factor for the line width. Default is hei/100.
    :return: the height of the top/bottom lines
    """
    rotateby = angle_offset_for_orientation(orientation)
    wid, hei = get_effective_dimensions(d, wid, hei)

    midx = x_start + wid/2
    midy = y_start + hei/2

    arc_width = 360 / num_points
    outer_radius = size_ratio*hei/4

    if sw == 0:
        sw = thick_ratio*hei/100#outer_radius*secondary_size *0.23

    ang_offset = rotateby

    linecap = 'round'
    for i in range(num_points):
        if square:
            p = draw.Path(stroke=primary_colour, fill=secondary_colour, stroke_width=sw, stroke_linecap=linecap)
        else:
            p = draw.Path(stroke=primary_colour, fill=secondary_colour, stroke_width=sw,
                          transform=f'scale({wid / hei}, 1', stroke_linecap=linecap)
            midx -= midx * (wid / hei) / 4

        stop1 = get_triangle_coords(outer_radius, arc_width, i, cent_x=midx, cent_y=midy, offset=ang_offset)
        stop2 = get_triangle_coords(outer_radius, arc_width, i+offset, cent_x=midx, cent_y=midy, offset=ang_offset)
        p.M(*stop1)
        p.L(*stop2)
        d.append(p)
    return sw


def draw_pointed_arbitrary_star_trace(d, primary_colour, secondary_colour='none',  num_points=5,
                        wid=UNSPECIFIED, hei=UNSPECIFIED, x_start=0, y_start=0,
                        size_ratio=1.0, secondary_size=0.58, orientation=VERTICAL, square=True, sw=0):
    """
    Draw a traced out kind of star, like the Star of David, with pointy points
    :param d: Drawing object
    :param primary_colour: the fill of the star
    :param secondary_colour: the outline of the star
    :param wid: width of the area we are working with
    :param hei: height of the area we are working with
    :param x_start: the x-coordinate of the upper left corner of the rectangular area that is being drawn into
    :param y_start: the y-coordinate of the upper left corner of the rectangular area that is being drawn into
    :param size_ratio: size factor. The radius of the star.
    :param stretch_ratio: How spiky the star is. 0.58 for Jewish star of david. 0.5 for regular 5-point star.
    :param thick_ratio: scaling factor for the line width. Default is hei/100.
    :return: the height of the top/bottom lines
    """
    rotateby = angle_offset_for_orientation(orientation)
    wid, hei = get_effective_dimensions(d, wid, hei)

    midx = x_start + wid/2
    midy = y_start + hei/2

    arc_width = 360 / num_points
    outer_radius = size_ratio*hei/4
    inner_radius = outer_radius*0.63

    if sw == 0 and secondary_colour != 'none':
        sw = thick_ratio*(hei/100)#outer_radius*secondary_size *0.23

    ang_offset = rotateby

    linecap = 'butt' #'round'
    for i in range(num_points):
        if square:
            p = draw.Path(stroke=primary_colour, fill=secondary_colour, stroke_width=sw, stroke_linecap=linecap)
        else:
            p = draw.Path(stroke=primary_colour, fill=secondary_colour, stroke_width=sw,
                          transform=f'scale({wid / hei}, 1', stroke_linecap=linecap)
            midx -= midx * (wid / hei) / 4

        stop1 = get_triangle_coords(outer_radius, arc_width, i, cent_x=midx, cent_y=midy, offset=ang_offset)
        stop2 = get_triangle_coords(outer_radius, arc_width, i+2, cent_x=midx, cent_y=midy, offset=ang_offset)
        stop4 = get_triangle_coords(inner_radius, arc_width, i, cent_x=midx, cent_y=midy, offset=ang_offset)
        stop3 = get_triangle_coords(inner_radius, arc_width, i+2, cent_x=midx, cent_y=midy, offset=ang_offset)
        p.M(*stop1)
        p.L(*stop2)
        if secondary_colour != 'none':
            p.L(*stop3)
        else:
            p.M(*stop3)
        p.L(*stop4)
        if secondary_colour != 'none':
            p.L(*stop1)
        else:
            p.M(*stop1)
        p.Z()
        d.append(p)
    return sw


def draw_morocco_star(d, primary_colour, secondary_colour='none',
              wid=UNSPECIFIED, hei=UNSPECIFIED, x_start=0, y_start=0,
              size_ratio = 1.0, stretch_ratio=1.0, thick_ratio=1.0, orientation=VERTICAL):
    """
    Draw a five-pointed star that is traced out like the Morocco star
    :param d: Drawing object
    :param primary_colour: the fill of the star
    :param secondary_colour: the outline of the star
    :param wid: width of the area we are working with
    :param hei: height of the area we are working with
    :param x_start: the x-coordinate of the upper left corner of the rectangular area that is being drawn into
    :param y_start: the y-coordinate of the upper left corner of the rectangular area that is being drawn into
    :param size_ratio: size factor. The radius of the star.
    :param stretch_ratio: How spiky the star is. Use 0.385 if you want a horizontal line at mid-top
    :param thick_ratio: scaling factor for the line width. Default is based on the Moroccan LGBT flag.
    :return: the height of the top/bottom lines
    """
    wid, hei = get_effective_dimensions(d, wid, hei)

    outer_radius = size_ratio*hei/4
    inner_radius = outer_radius*0.63
    y_start += (outer_radius-inner_radius)*0.25
    sw = thick_ratio*(hei*0.001)
    return draw_pointed_arbitrary_star_trace(d, primary_colour, secondary_colour=primary_colour, num_points=5,
                               wid=wid, hei=hei, x_start=x_start, y_start=y_start, size_ratio=size_ratio*1,
                               orientation=orientation, secondary_size=stretch_ratio*0.5, sw=sw)



def draw_star_of_david(d, primary_colour, secondary_colour='none',
              wid=UNSPECIFIED, hei=UNSPECIFIED, x_start=0, y_start=0,
              size_ratio = 1.0, stretch_ratio=1.0, thick_ratio=1.0, orientation=VERTICAL):
    """
    Draw a Star of David. If secondary colour is 'none', do a hollow Star of David
    like in this Androgynous flag: https://lgbtqia.wiki/wiki/Androgynos#/media/File:Androgynos_(2).png
    :param d: Drawing object
    :param primary_colour: the outline of the star
    :param secondary_colour: the colour used for the inside lines (if any)
    :param wid: width of the area we are working with
    :param hei: height of the area we are working with
    :param x_start: the x-coordinate of the upper left corner of the rectangular area that is being drawn into
    :param y_start: the y-coordinate of the upper left corner of the rectangular area that is being drawn into
    :param size_ratio: size factor. The radius of the star.
    :param stretch_ratio: How spiky the star is. Default is to be a Star of David.
    :param thick_ratio: scaling factor for the line width. Default is based on the Androgynos flag.
    :return: stroke width
    """
    rotateby = angle_offset_for_orientation(orientation)
    wid, hei = get_effective_dimensions(d, wid, hei)

    midx = x_start + wid/2
    midy = y_start + hei/2

    arc_width = 360 / 6
    outer_radius = 1.29*size_ratio*hei/4
    inner_radius = outer_radius*0.578*stretch_ratio

    sw = 1.29*thick_ratio*(hei/4)*0.5 *0.175

    ang_offset = rotateby

    linecap = 'round'
    for i in range(6):
        stopM = get_triangle_coords(inner_radius, arc_width, i+0.5, cent_x=midx, cent_y=midy, offset=ang_offset)
        r = draw.Path(stroke=secondary_colour, fill='none', stroke_width=sw, stroke_linecap=linecap)
        stopQ = get_triangle_coords(inner_radius, arc_width, i+1.5, cent_x=midx, cent_y=midy, offset=ang_offset)
        r.M(*stopM)
        r.L(*stopQ)
        d.append(r)
    for i in range(6):
        stop1 = get_triangle_coords(outer_radius, arc_width, i, cent_x=midx, cent_y=midy, offset=ang_offset)
        stopM = get_triangle_coords(inner_radius, arc_width, i+0.5, cent_x=midx, cent_y=midy, offset=ang_offset)
        stopP = get_triangle_coords(inner_radius, arc_width, i-0.5, cent_x=midx, cent_y=midy, offset=ang_offset)
        p = draw.Path(stroke=primary_colour, fill='none', stroke_width=sw, stroke_linecap=linecap)
        p.M(*stopP)
        p.L(*stop1)
        p.L(*stopM)
        d.append(p)
    return sw



def draw_nautstar(d, primary_colour, secondary_colour='none',
              wid=UNSPECIFIED, hei=UNSPECIFIED, x_start=0, y_start=0,
              size_ratio = 1.0, stretch_ratio=1.0, thick_ratio=1.0, orientation=VERTICAL):
    """
    Draw a star on a path in the style of the outernaut flag
    see https://pluralpedia.org/w/File:Outernaut_Flag.png
    :param d: Drawing object
    :param primary_colour: the colour used for the lines (it goes first because layer-wise it is underneath the star)
    :param secondary_colour: the fill of the star
    :param wid: width of the area we are working with
    :param hei: height of the area we are working with
    :param x_start: the x-coordinate of the upper left corner of the rectangular area that is being drawn into
    :param y_start: the y-coordinate of the upper left corner of the rectangular area that is being drawn into
    :param size_ratio: size factor. The radius of the star.
    :param stretch_ratio: How spiky the star is.
    :param thick_ratio: scaling factor for the line width.
    :return: stroke width
    """
    this_wid, this_hei = get_effective_dimensions(d, wid, hei)
    sw = (this_hei/3)/5
    midy = y_start + this_hei/2
    top_height = midy-sw
    top_bottom = midy+sw
    x_end = x_start + this_wid*0.8
    d.append(draw.Line(x_start, top_height, x_end, top_height, stroke_width=sw, stroke=primary_colour))
    d.append(draw.Line(x_start, top_bottom, x_end, top_bottom, stroke_width=sw, stroke=primary_colour))
    #draw_fivesided_star(d, secondary_colour, size_ratio=0.74, orientation=CENTRAL, y_start=hei*5, x_start=-150*wid)
    draw_fivesided_star(d, secondary_colour, size_ratio=0.74, orientation=CENTRAL, y_start=-this_hei*0.015, x_start=.3*this_wid)


def draw_therian(d, primary_colour, secondary_colour='none',
              wid=UNSPECIFIED, hei=UNSPECIFIED, x_start=0, y_start=0,
              size_ratio = 1.0, stretch_ratio=1.0, thick_ratio=1.0, orientation=VERTICAL):
    """
    Draw the therian symbol, optionally in a circle
    :param d: Drawing object
    :param primary_colour: the colour used for the lines
    :param secondary_colour: fill of background circle (if present)
    :param wid: width of the area we are working with
    :param hei: height of the area we are working with
    :param x_start: the x-coordinate of the upper left corner of the rectangular area that is being drawn into
    :param y_start: the y-coordinate of the upper left corner of the rectangular area that is being drawn into
    :param size_ratio: size factor. The radius of the star.
    :param stretch_ratio: How spiky the star is.
    :param thick_ratio: scaling factor for the line width.
    :return: stroke width
    """
    wid, hei = get_effective_dimensions(d, wid, hei)
    midx = x_start + wid/2
    midy = y_start + hei/2

    radius = 1.2*size_ratio*hei/6
    sw = thick_ratio*2.5*hei/100
    y_offset = 0.02*hei

    if secondary_colour != 'none':
        outer_radius = radius*1.75
        d.append(draw.Circle(midx, midy+y_offset/2, outer_radius, fill=secondary_colour))

    d.append(draw.Circle(midx, midy+y_offset, radius, stroke_width=sw, stroke=primary_colour, fill='none'))
    # the triangle
    draw_arbitrary_star_trace(d, primary_colour, num_points=3, thick_ratio=2.5*thick_ratio, size_ratio=1.2*size_ratio, y_start=y_offset)

def draw_otherkin(d, primary_colour, secondary_colour='none',
              wid=UNSPECIFIED, hei=UNSPECIFIED, x_start=0, y_start=0,
              size_ratio = 1.0, stretch_ratio=1.0, thick_ratio=1.0, orientation=VERTICAL):
    """
    Draw the otherkin symbol, optionally in a circle
    :param d: Drawing object
    :param primary_colour: the colour used for the lines
    :param secondary_colour: fill of background circle (if present)
    :param wid: width of the area we are working with
    :param hei: height of the area we are working with
    :param x_start: the x-coordinate of the upper left corner of the rectangular area that is being drawn into
    :param y_start: the y-coordinate of the upper left corner of the rectangular area that is being drawn into
    :param size_ratio: size factor. The radius of the star.
    :param stretch_ratio: How spiky the star is.
    :param thick_ratio: scaling factor for the line width.
    :return: stroke width
    """
    wid, hei = get_effective_dimensions(d, wid, hei)
    midx = x_start + wid/2
    midy = y_start + hei/2

    radius = 1.2*size_ratio*hei/6
    sw = thick_ratio*2.5*hei/100
    y_offset = 0.02*hei

    if secondary_colour != 'none':
        outer_radius = radius*1.75
        d.append(draw.Circle(midx, midy+y_offset/2, outer_radius, fill=secondary_colour))

    # the star
    draw_arbitrary_star_trace(d, primary_colour, num_points=7, offset=3, thick_ratio=2.2*thick_ratio, size_ratio=1.13*size_ratio, y_start=y_offset)


def draw_nonhuman(d, primary_colour, secondary_colour='none',
              wid=UNSPECIFIED, hei=UNSPECIFIED, x_start=0, y_start=0,
              size_ratio = 1.0, stretch_ratio=1.0, thick_ratio=1.0, orientation=VERTICAL):
    """
    Draw the nonhuman symbol, optionally in a circle
    :param d: Drawing object
    :param primary_colour: the colour used for the lines
    :param secondary_colour: fill of background circle (if present)
    :param wid: width of the area we are working with
    :param hei: height of the area we are working with
    :param x_start: the x-coordinate of the upper left corner of the rectangular area that is being drawn into
    :param y_start: the y-coordinate of the upper left corner of the rectangular area that is being drawn into
    :param size_ratio: size factor. The radius of the star.
    :param stretch_ratio: How spiky the star is.
    :param thick_ratio: scaling factor for the line width.
    :return: stroke width
    """
    wid, hei = get_effective_dimensions(d, wid, hei)
    midx = x_start + wid/2
    midy = y_start + hei/2

    radius = 1.2*size_ratio*hei/6
    sw = thick_ratio*3.5*hei/100
    y_offset = 0.02*hei

    if secondary_colour != 'none':
        outer_radius = radius*1.8
        d.append(draw.Circle(midx, midy+y_offset, outer_radius, fill=secondary_colour))

    # triangle in nonhuman flag has a bottom width that is 1/3 canvas width
    # and its base horizontal line is just under the middle stripe so the top of the path aligns with the stripe
    draw_arbitrary_star_trace(d, primary_colour, num_points=3, thick_ratio=3.5*thick_ratio, size_ratio=1.25*size_ratio, y_start=1.35*y_offset)

    # the ring
    d.append(draw.Circle(midx, midy+y_offset, 1.15*radius, stroke_width=sw, stroke=primary_colour, fill='none'))

    # the star is centred in the ring
    # the star is such that its horizontal line meets the triangle
    # the two little triangles from the star going past the main triangle should be full
    draw_arbitrary_star_trace(d, primary_colour, num_points=7, offset=3, thick_ratio=3.5*thick_ratio, size_ratio=.9*size_ratio, y_start=y_offset)





def draw_heart(d, primary_colour, secondary_colour='none',
              wid=UNSPECIFIED, hei=UNSPECIFIED, x_start=0, y_start=0,
              size_ratio = 1.0, stretch_ratio=1.0, thick_ratio=1.0, orientation=VERTICAL):
    """
    Draw a heart in the centre
    :param d: Drawing object
    :param primary_colour: fill colour (string) of the heart
    :param secondary_colour: colour (string) of the outline of the heart
    :param wid: width of the area we are working with
    :param hei: height of the area we are working with
    :param x_start: the x-coordinate of the upper left corner of the rectangular area that is being drawn into
    :param y_start: the y-coordinate of the upper left corner of the rectangular area that is being drawn into
    :param size_ratio: size factor (radius of heart)
    :param thick_ratio: scaling factor for the line width (if outline of heart is used). Default is hei/100 if outlining, 0 if not.
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
    if orientation in [VERTICAL, HORIZONTAL]:
        rotateby += 90

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
        p = draw.Path(fill=primary_colour, stroke=secondary_colour, transform=f'rotate({rotateby},{midx},{midy})')
    else:
        sw = thick_ratio*(hei/100)
        p = draw.Path(fill=primary_colour, stroke=secondary_colour, stroke_width=sw)
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






if __name__ == '__main__':
    doctest.testmod()
    wid = 1200
    hei = 720
    d = draw.Drawing(wid, hei)
    draw_horiz_bars(d, ['black'])
    draw_southern_cross(d, 'white')
    d.save_png('drawflags/test.png')

    d = draw.Drawing(wid, hei)
    pal = ['purple', 'orange', 'black', 'black']
    #draw_horiz_bars(d, ['yellow'])
    #androg = ["#0552a8", '#0d7dfe'.upper(), '#fffFFF', '#fffFFF', '#ffff61' , '#FED45b']
    #draw_horiz_bars(d, androg)
    draw_horiz_bars(d, ['brown', 'yellow', 'brown'])
    #draw_fivesided_star(d, 'red', y_start=-100, x_start=100, orientation=DIAGONAL)
    #draw_arbitrary_star(d,'red', 'black', num_points=20, secondary_size=0.75, square=False)
    #draw_arbitrary_star_trace(d, 'red', num_points=6)
    #draw_pointed_arbitrary_star_trace(d, 'black', num_points=5)
    #draw_star_of_david(d, 'black', )
    #draw_nautstar(d, 'black', 'blue')
    draw_nonhuman(d, 'black', 'orange')
    d.save_svg('drawflags/test2.svg')

    '''
    # https://commons.wikimedia.org/wiki/File:Flag_of_Czechoslovakia_-_Vaporwave_pink_edition_(Unofficial_civil).svg
    d = draw.Drawing(500*4, 300*4)
    draw_horiz_bars(d, ['white', '#ff78c8'])
    pw = draw_pile(d, '#9f2dad', size_ratio=1.5)
    draw_fivesided_star(d, '#de0700', secondary_size=0.385, wid=0.53*d.width, size_ratio=1.25, y_start=-0.18*d.height) # .37 and .38 too inward
    filelocations = save_flag(d, 'czechvapor')

    d = draw.Drawing(500*4, 300*4)
    draw_horiz_bars(d, ['black', '#cc0000'])
    draw_circle(d, '#ffff01', size_ratio=0.5)
    filelocations = save_flag(d, 'aus_indigenous')
    '''