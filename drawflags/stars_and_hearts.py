from pride_rings import *

def draw_arbitrary_star(d, primary_colour, secondary_colour='none',  num_points=5,
                        wid=UNSPECIFIED, hei=UNSPECIFIED, x_start=0, y_start=0,
                        size_ratio=1.0, secondary_size=0.58, orientation=VERTICAL, square=True, sw=0):
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
    :param secondary_size: how spiky the star is. 0.58 for Jewish star of david. 0.5 for regular 5-point star.
    :return: the height of the top/bottom lines
    """
    rotateby = angle_offset_for_orientation(orientation)
    wid, hei = get_effective_dimensions(d, wid, hei)

    midx = x_start + wid/2
    midy = y_start + hei/2

    arc_width = 360 / num_points
    outer_radius = size_ratio*hei/4
    inner_radius = outer_radius*secondary_size

    if secondary_colour != 'none' and sw == 0:
        sw = inner_radius *0.13

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


def draw_fivesided_star(d, primary_colour, secondary_colour='none', wid=UNSPECIFIED, hei=UNSPECIFIED,
                x_start=0, y_start=0, size_ratio=1.0, secondary_size=0.5, orientation=VERTICAL, sw=0):
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
    :param secondary_size: how spiky the star is. 0.385 if you want a horizontal line at mid-top
    :return: the height of the top/bottom lines
    """
    return draw_arbitrary_star(d, primary_colour, secondary_colour=secondary_colour, num_points=5,
                               wid=wid, hei=hei, x_start=x_start, y_start=y_start, size_ratio=size_ratio,
                               orientation=orientation, secondary_size=secondary_size, sw=sw)


def draw_australian_star(d, primary_colour, secondary_colour='none', wid=UNSPECIFIED, hei=UNSPECIFIED,
                x_start=0, y_start=0, size_ratio=1.0, secondary_size=0.45, orientation=VERTICAL, sw=0):
    """
    Draw a seven-pointed star in the style of the Australian flag
    :param d: Drawing object
    :param primary_colour: the fill of the star
    :param secondary_colour: the outline of the star
    :param wid: width of the area we are working with
    :param hei: height of the area we are working with
    :param x_start: the x-coordinate of the upper left corner of the rectangular area that is being drawn into
    :param y_start: the y-coordinate of the upper left corner of the rectangular area that is being drawn into
    :param size_ratio: size factor
    :param secondary_size: how spiky the star is. 0.45 by default for Aussie star.
    :param sw: stroke width
    :return: the height of the top/bottom lines
    """
    return draw_arbitrary_star(d, primary_colour, secondary_colour=secondary_colour, num_points=7,
                               wid=wid, hei=hei, x_start=x_start, y_start=y_start, size_ratio=size_ratio,
                               orientation=orientation, secondary_size=secondary_size, sw=sw)


def draw_southern_cross(d, primary_colour, secondary_colour='none', wid=UNSPECIFIED, hei=UNSPECIFIED,
                x_start=0, y_start=0, size_ratio=1.0, orientation=VERTICAL, sw=None):
    """
    Draw the Southern Cross like on the Australian flag
    :param d: Drawing object
    :param primary_colour: the fill of the star
    :param secondary_colour: the outline of the star
    :param wid: width of the area we are working with
    :param hei: height of the area we are working with
    :param x_start: the x-coordinate of the upper left corner of the rectangular area that is being drawn into
    :param y_start: the y-coordinate of the upper left corner of the rectangular area that is being drawn into
    :param size_ratio: size factor
    :param secondary_size: how spiky the star is. 0.45 by default for Aussie star.
    :return: the height of the top/bottom lines
    """
    wid, hei = get_effective_dimensions(d, wid, hei)
    midx = x_start + wid/2
    midy = y_start + hei/2

    if type(primary_colour) != list:
        primary_colour = [primary_colour]*5

    if sw == None:
        sw = hei/100

    # top star is midx and about hei/6?
    top_offs = 2*hei/6
    starsize = 0.3
    draw_australian_star(d, primary_colour[0], secondary_colour, wid=wid/2, hei=hei, x_start=midx/2, y_start=-top_offs, size_ratio=starsize, sw=sw)
    # lower star is also midx
    draw_australian_star(d, primary_colour[4], secondary_colour, wid=wid/2, hei=hei, x_start=midx/2, y_start=top_offs, size_ratio=starsize, sw=sw)

    # left star is at wid/4 and about 2/3 hei?
    leftward = hei*0.25
    left_y = hei*0.065
    draw_australian_star(d, primary_colour[2], secondary_colour, wid=wid/2, hei=hei, x_start=(midx/2)-leftward, y_start=-left_y, size_ratio=starsize, sw=sw)

    # right star is at .75wid and higher than left
    right_y = hei*0.125
    rightward = hei*0.215
    draw_australian_star(d, primary_colour[1], secondary_colour, wid=wid/2, hei=hei, x_start=(midx/2)+rightward, y_start=-right_y, size_ratio=starsize, sw=sw)

    # and then the little star
    small_y = hei*0.04
    small_x = hei*0.09
    draw_fivesided_star(d, primary_colour[3], secondary_colour,  wid=wid/2, hei=hei, x_start=(midx/2)+small_x, y_start=small_y,
                        size_ratio=starsize/2, secondary_size=0.475, sw=sw)


def draw_heart(d, primary_colour, secondary_colour='none', wid=UNSPECIFIED, hei=UNSPECIFIED,
               x_start=0, y_start=0, size_ratio=1, orientation=VERTICAL):
    """
    Draw a heart in the centre
    :param d: Drawing object
    :param primary_colour: fill colour (string) of the heart
    :param secondary_colour: colour (string) of the outline of the heart
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
        p = draw.Path(fill=primary_colour, stroke=secondary_colour)
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
    wid = 500
    hei = 300
    d = draw.Drawing(wid, hei)
    draw_horiz_bars(d, ['black'])
    draw_southern_cross(d, 'white')
    d.save_png('drawflags/test.png')

    d = draw.Drawing(wid, hei)
    pal = ['purple', 'orange', 'black', 'black']
    draw_horiz_bars(d, ['yellow'])
    draw_fivesided_star(d, 'red', y_start=-100, x_start=100, orientation=DIAGONAL)
    draw_arbitrary_star(d,'red', 'black', num_points=20, secondary_size=0.75, square=False)
    d.save_svg('drawflags/test2.svg')

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