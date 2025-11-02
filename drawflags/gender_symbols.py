from stars_and_hearts import *

def astro_symbol_defaults(d, primary_colour, secondary_colour,
                          wid, hei, x_start, y_start,
                          size_ratio, stretch_ratio, sharp_ratio, sparse_ratio, thick_ratio, orientation):
    # helper function for the gender symbols
    wid, hei, x_mid, y_mid, x_end, y_end = get_standard_dimensions(d, wid, hei, x_start, y_start)
    sw = thick_ratio*size_ratio*hei/18
    radius = size_ratio*hei/5.75 # radius of the central circle
    arm_length = radius*1.25*stretch_ratio # how long the arm is
    cross_length = radius*.5*sharp_ratio # how long the crossbar is
    joint_length = arm_length*.5*sparse_ratio # where the arm meets the cross

    rotateby = angle_offset_for_orientation(orientation) + 90

    # central circle
    d.append(draw.Circle( x_mid, y_mid, radius, stroke=primary_colour, stroke_width=sw, fill=secondary_colour ))

    return wid, hei, x_mid, y_mid, x_end, y_end, sw, radius, arm_length, cross_length, joint_length, rotateby


###### helpers for paths

def path_arm(p, x_mid, y_mid, radius, arm_length):
    # a simple line downwards
    p.M(x_mid, y_mid+radius)
    p.L(x_mid, y_mid+radius+arm_length)

def path_venus(p, x_mid, y_mid, radius, arm_length, cross_length, joint_length):
    # makes a cross on the arm path
    y_intersect = y_mid+radius+joint_length
    p.M(x_mid - cross_length, y_intersect)
    p.L(x_mid + cross_length, y_intersect)

def path_mars(p, x_mid, y_mid, radius, arm_length, cross_length, sparse_ratio):
    x_len = cross_length #joint_length
    y_len = cross_length/sparse_ratio
    p.M(x_mid - x_len, y_mid+radius+arm_length-y_len)
    p.L(x_mid, y_mid + radius + arm_length)
    p.L(x_mid + x_len, y_mid+radius+arm_length-y_len)

def path_mercury(p, x_mid, y_mid, radius, arm_length, sharp_ratio):
    top = y_mid - radius
    upper = y_mid - radius - arm_length
    left = x_mid - radius
    right = x_mid + radius

    p.M(left, upper)
    cx_len = radius*.3*sharp_ratio
    cy_len = radius*0.05
    outer_cx = radius*.05
    outer_cy = radius*.1
    p.C(left+outer_cx, top-outer_cy, x_mid-cx_len, top-cy_len, x_mid, top)
    p.C(x_mid+cx_len, top-cy_len, right-outer_cx, top-outer_cy, right, upper)


############# drawing functions

def draw_venus_symbol(d, primary_colour, secondary_colour='none',
                      wid=UNSPECIFIED, hei=UNSPECIFIED, x_start=0, y_start=0,
                      size_ratio=1.0, stretch_ratio=1.0, sharp_ratio=1.0, sparse_ratio=1.0, thick_ratio=1.0,
                      orientation=HORIZONTAL):
    """
    Draw a Venus symbol. Centring is done based on the centre circle, not the whole symbol.
    This centring is done to make it easier to layer symbols atop each other.
    :param d: Drawing object
    :param primary_colour: stroke colour
    :param secondary_colour: fill colour of the centre ring
    :param wid: width of the area we are working with
    :param hei: height of the area we are working with
    :param x_start: the x-coordinate of the upper left corner of the rectangular area that is being drawn into
    :param y_start: the y-coordinate of the upper left corner of the rectangular area that is being drawn into
    :param size_ratio: radius of the central circle
    :param stretch_ratio: how long the arm is relative to the radius of the central circle
    :param sharp_ratio: how long the cross or arrow is relative to the radius of the central circle
    :param sparse_ratio: adjusts how far the cross is from the central circle
    :param thick_ratio: adjusts line thickness
    :param orientation: positioning of the arm, default is HORIZONTAL
    :return:
    """
    vars = astro_symbol_defaults(d, primary_colour, secondary_colour, wid, hei, x_start, y_start,
                                 size_ratio, stretch_ratio, sharp_ratio, sparse_ratio, thick_ratio, orientation)
    wid, hei, x_mid, y_mid, x_end, y_end, sw, radius, arm_length, cross_length, joint_length, rotateby = vars

    # the arm
    if rotateby != 0:
        p = draw.Path(stroke=primary_colour, stroke_width=sw, transform=f'rotate({rotateby},{x_mid},{y_mid})', fill='none')
    else:
        p = draw.Path(stroke=primary_colour, stroke_width=sw, fill='none')
    path_arm(p, x_mid, y_mid, radius, arm_length)
    # use sparse_ratio to adjust where the cross is on the arm
    path_venus(p, x_mid, y_mid, radius, arm_length, cross_length, joint_length)
    d.append(p)

def draw_mars_symbol(d, primary_colour, secondary_colour='none',
                     wid=UNSPECIFIED, hei=UNSPECIFIED, x_start=0, y_start=0,
                     size_ratio=1.0, stretch_ratio=1.0, sharp_ratio=1.0, sparse_ratio=1.0, thick_ratio=1.0,
                     orientation=HORIZONTAL):
    """
    Draw a Mars symbol. Centring is done based on the centre circle, not the whole symbol.
    This centring is done to make it easier to layer symbols atop each other.
    :param d: Drawing object
    :param primary_colour: stroke colour
    :param secondary_colour: fill colour of the centre ring
    :param wid: width of the area we are working with
    :param hei: height of the area we are working with
    :param x_start: the x-coordinate of the upper left corner of the rectangular area that is being drawn into
    :param y_start: the y-coordinate of the upper left corner of the rectangular area that is being drawn into
    :param size_ratio: radius of the central circle
    :param stretch_ratio: how long the arm is relative to the radius of the central circle
    :param sharp_ratio: how long the cross or arrow is relative to the radius of the central circle
    :param sparse_ratio: adjusts how far the cross is from the central circle
    :param thick_ratio: adjusts line thickness
    :param orientation: positioning of the arm, default is HORIZONTAL
    :return:
    """
    vars = astro_symbol_defaults(d, primary_colour, secondary_colour, wid, hei, x_start, y_start,
                                 size_ratio, stretch_ratio, sharp_ratio, sparse_ratio, thick_ratio, orientation)
    wid, hei, x_mid, y_mid, x_end, y_end, sw, radius, arm_length, cross_length, joint_length, rotateby = vars

    # rotation is by default BEND
    rotateby += 45 + 180

    # the arm
    if rotateby != 0:
        p = draw.Path(stroke=primary_colour, stroke_width=sw, transform=f'rotate({rotateby},{x_mid},{y_mid})', fill='none')
    else:
        p = draw.Path(stroke=primary_colour, stroke_width=sw, fill='none')
    path_arm(p, x_mid, y_mid, radius, arm_length) # draws the arm
    # the arrow
    path_mars(p, x_mid, y_mid, radius, arm_length, cross_length, sparse_ratio)
    d.append(p)


def draw_androgyne_symbol(d, primary_colour, secondary_colour='none',
                          wid=UNSPECIFIED, hei=UNSPECIFIED, x_start=0, y_start=0,
                          size_ratio=1.0, stretch_ratio=1.0, sharp_ratio=1.0, sparse_ratio=1.0, thick_ratio=1.0,
                          orientation=HORIZONTAL):
    """
    Draw the Mars+Venus symbol used in the trans symbol. Centring is done based on the centre circle, not the whole symbol.
    :param d: Drawing object
    :param primary_colour: stroke colour
    :param secondary_colour: fill colour of the centre ring
    :param wid: width of the area we are working with
    :param hei: height of the area we are working with
    :param x_start: the x-coordinate of the upper left corner of the rectangular area that is being drawn into
    :param y_start: the y-coordinate of the upper left corner of the rectangular area that is being drawn into
    :param size_ratio: radius of the central circle
    :param stretch_ratio: how long the arm is relative to the radius of the central circle
    :param sharp_ratio: how long the cross or arrow is relative to the radius of the central circle
    :param sparse_ratio: adjusts how far the cross is from the central circle
    :param thick_ratio: adjusts line thickness
    :param orientation: positioning of the arm, default is HORIZONTAL
    :return:
    """
    vars = astro_symbol_defaults(d, primary_colour, secondary_colour, wid, hei, x_start, y_start,
                                 size_ratio, stretch_ratio, sharp_ratio, sparse_ratio, thick_ratio, orientation)
    wid, hei, x_mid, y_mid, x_end, y_end, sw, radius, arm_length, cross_length, joint_length, rotateby = vars

    rotateby += 45+90 # default is actually DIAGONAL

    # the arm
    if rotateby != 0:
        p = draw.Path(stroke=primary_colour, stroke_width=sw, transform=f'rotate({rotateby},{x_mid},{y_mid})', fill='none')
    else:
        p = draw.Path(stroke=primary_colour, stroke_width=sw, fill='none')
    path_arm(p, x_mid, y_mid, radius, arm_length) # draws the arm
    # the Mars portion
    path_mars(p, x_mid, y_mid, radius, arm_length, cross_length, sparse_ratio)
    # the Venus portion is further towards the centre
    path_venus(p, x_mid, y_mid, radius, arm_length, cross_length, joint_length*0.675)
    d.append(p)


def draw_trans_symbol(d, primary_colour, secondary_colour='none',
                      wid=UNSPECIFIED, hei=UNSPECIFIED, x_start=0, y_start=0,
                      size_ratio=1.0, stretch_ratio=1.0, sharp_ratio=1.0, sparse_ratio=1.0, thick_ratio=1.0,
                      orientation=HORIZONTAL):
    """
    Draw the Mars+Venus symbol used in the trans symbol. Centring is done based on the centre circle, not the whole symbol.
    :param d: Drawing object
    :param primary_colour: stroke colour
    :param secondary_colour: fill colour
    :param wid: width of the area we are working with
    :param hei: height of the area we are working with
    :param x_start: the x-coordinate of the upper left corner of the rectangular area that is being drawn into
    :param y_start: the y-coordinate of the upper left corner of the rectangular area that is being drawn into
    :param size_ratio: radius of the central circle
    :param stretch_ratio: how long the arm is relative to the radius of the central circle
    :param sharp_ratio: how long the cross or arrow is relative to the radius of the central circle
    :param sparse_ratio: adjusts how far the cross is from the central circle
    :param thick_ratio: adjusts line thickness
    :param orientation: positioning of the arm, default is HORIZONTAL
    :return:
    """
    draw_mars_symbol(d, primary_colour, secondary_colour, wid, hei, x_start, y_start,
          size_ratio, stretch_ratio, sharp_ratio*1.2, sparse_ratio, thick_ratio, orientation)
    draw_venus_symbol(d, primary_colour, secondary_colour, wid, hei, x_start, y_start,
          size_ratio, stretch_ratio, sharp_ratio*1.2, sparse_ratio*1.1, thick_ratio, orientation)
    draw_androgyne_symbol(d, primary_colour, secondary_colour, wid, hei, x_start, y_start,
                          size_ratio, stretch_ratio, sharp_ratio, sparse_ratio, thick_ratio, orientation)

def draw_mercury_symbol(d, primary_colour, secondary_colour='none',
                      wid=UNSPECIFIED, hei=UNSPECIFIED, x_start=0, y_start=0,
                      size_ratio=1.0, stretch_ratio=1.0, sharp_ratio=1.0, sparse_ratio=1.0, thick_ratio=1.0,
                      orientation=HORIZONTAL):
    """
    Draw a Mercury symbol. Centring is done based on the centre circle, not the whole symbol.
    This centring is done to make it easier to layer symbols atop each other.
    :param d: Drawing object
    :param primary_colour: stroke colour
    :param secondary_colour: fill colour of the centre ring
    :param wid: width of the area we are working with
    :param hei: height of the area we are working with
    :param x_start: the x-coordinate of the upper left corner of the rectangular area that is being drawn into
    :param y_start: the y-coordinate of the upper left corner of the rectangular area that is being drawn into
    :param size_ratio: radius of the central circle
    :param stretch_ratio: how long the arm is relative to the radius of the central circle
    :param sharp_ratio: how long the cross or arrow is relative to the radius of the central circle
    :param sparse_ratio: adjusts how far the cross is from the central circle
    :param thick_ratio: adjusts line thickness
    :param orientation: positioning of the arm, default is HORIZONTAL
    :return:
    """
    vars = astro_symbol_defaults(d, primary_colour, secondary_colour, wid, hei, x_start, y_start,
                                 size_ratio, stretch_ratio, sharp_ratio, sparse_ratio, thick_ratio, orientation)
    wid, hei, x_mid, y_mid, x_end, y_end, sw, radius, arm_length, cross_length, joint_length, rotateby = vars

    # the arm
    if rotateby != 0:
        p = draw.Path(stroke=primary_colour, stroke_width=sw, transform=f'rotate({rotateby},{x_mid},{y_mid})', fill='none')
    else:
        p = draw.Path(stroke=primary_colour, stroke_width=sw, fill='none')
    path_arm(p, x_mid, y_mid, radius, arm_length)
    # use sparse_ratio to adjust where the cross is on the arm
    path_venus(p, x_mid, y_mid, radius, arm_length, cross_length*1.3, joint_length)
    path_mercury(p, x_mid, y_mid, radius, arm_length*.8, sharp_ratio)
    d.append(p)


def draw_neutral_symbol(d, primary_colour, secondary_colour='none',
                      wid=UNSPECIFIED, hei=UNSPECIFIED, x_start=0, y_start=0,
                      size_ratio=1.0, stretch_ratio=1.0, sharp_ratio=1.0, sparse_ratio=1.0, thick_ratio=1.0,
                      orientation=HORIZONTAL):
    """
    Draw a gender neutral symbol. Centring is done based on the centre circle, not the whole symbol.
    This centring is done to make it easier to layer symbols atop each other.
    :param d: Drawing object
    :param primary_colour: stroke colour
    :param secondary_colour: fill colour of the centre ring
    :param wid: width of the area we are working with
    :param hei: height of the area we are working with
    :param x_start: the x-coordinate of the upper left corner of the rectangular area that is being drawn into
    :param y_start: the y-coordinate of the upper left corner of the rectangular area that is being drawn into
    :param size_ratio: radius of the central circle
    :param stretch_ratio: how long the arm is relative to the radius of the central circle
    :param sharp_ratio: how long the cross or arrow is relative to the radius of the central circle
    :param sparse_ratio: adjusts how far the cross is from the central circle
    :param thick_ratio: adjusts line thickness
    :param orientation: positioning of the arm, default is HORIZONTAL
    :return:
    """
    vars = astro_symbol_defaults(d, primary_colour, secondary_colour, wid, hei, x_start, y_start,
                                 size_ratio, stretch_ratio, sharp_ratio, sparse_ratio, thick_ratio, orientation)
    wid, hei, x_mid, y_mid, x_end, y_end, sw, radius, arm_length, cross_length, joint_length, rotateby = vars
    # the arm
    if rotateby != 0:
        p = draw.Path(stroke=primary_colour, stroke_width=sw, transform=f'rotate({rotateby},{x_mid},{y_mid})', fill='none')
    else:
        p = draw.Path(stroke=primary_colour, stroke_width=sw, fill='none')
    path_arm(p, x_mid, y_mid, radius, arm_length)
    d.append(p)


def draw_nonbinary_symbol(d, primary_colour, secondary_colour='none',
                      wid=UNSPECIFIED, hei=UNSPECIFIED, x_start=0, y_start=0,
                      size_ratio=1.0, stretch_ratio=1.0, sharp_ratio=1.0, sparse_ratio=1.0, thick_ratio=1.0,
                      orientation=HORIZONTAL):
    """
    Draw a Nonbinary * symbol. Centring is done based on the centre circle, not the whole symbol.
    This centring is done to make it easier to layer symbols atop each other.
    :param d: Drawing object
    :param primary_colour: stroke colour
    :param secondary_colour: fill colour of the centre ring
    :param wid: width of the area we are working with
    :param hei: height of the area we are working with
    :param x_start: the x-coordinate of the upper left corner of the rectangular area that is being drawn into
    :param y_start: the y-coordinate of the upper left corner of the rectangular area that is being drawn into
    :param size_ratio: radius of the central circle
    :param stretch_ratio: how long the arm is relative to the radius of the central circle
    :param sharp_ratio: how long the cross or arrow is relative to the radius of the central circle
    :param sparse_ratio: adjusts how far the cross is from the central circle
    :param thick_ratio: adjusts line thickness
    :param orientation: positioning of the arm, default is HORIZONTAL
    :return:
    """
    vars = astro_symbol_defaults(d, primary_colour, secondary_colour, wid, hei, x_start, y_start,
                                 size_ratio, stretch_ratio, sharp_ratio, sparse_ratio, thick_ratio, orientation)
    wid, hei, x_mid, y_mid, x_end, y_end, sw, radius, arm_length, cross_length, joint_length, rotateby = vars
    rotateby += 180 # default is actually UPSIDE
    # the arm
    if rotateby != 0:
        p = draw.Path(stroke=primary_colour, stroke_width=sw, transform=f'rotate({rotateby},{x_mid},{y_mid})', fill='none')
    else:
        p = draw.Path(stroke=primary_colour, stroke_width=sw, fill='none')
    path_arm(p, x_mid, y_mid, radius, arm_length)
    # use sparse_ratio to adjust where the cross is on the arm
    y_intersect = y_mid+radius+joint_length
    for i in range(6):
        ang_inc = 360/6
        coord = get_triangle_coords(cross_length, ang_inc, i, cent_x=x_mid, cent_y=y_intersect, offset=90)
        p.M(*coord)
        p.L(x_mid, y_intersect)
    d.append(p)



def draw_xenous_symbol(d, primary_colour, secondary_colour='none',
                      wid=UNSPECIFIED, hei=UNSPECIFIED, x_start=0, y_start=0,
                      size_ratio=1.0, stretch_ratio=1.0, sharp_ratio=1.0, sparse_ratio=1.0, thick_ratio=1.0,
                      orientation=HORIZONTAL):
    """
    Draw a Xenous symbol. Centring is done based on the centre circle, not the whole symbol.
    This centring is done to make it easier to layer symbols atop each other.
    :param d: Drawing object
    :param primary_colour: stroke colour
    :param secondary_colour: fill colour of the centre ring
    :param wid: width of the area we are working with
    :param hei: height of the area we are working with
    :param x_start: the x-coordinate of the upper left corner of the rectangular area that is being drawn into
    :param y_start: the y-coordinate of the upper left corner of the rectangular area that is being drawn into
    :param size_ratio: radius of the central circle
    :param stretch_ratio: how long the arm is relative to the radius of the central circle
    :param sharp_ratio: how long the cross or arrow is relative to the radius of the central circle
    :param sparse_ratio: adjusts how far the cross is from the central circle
    :param thick_ratio: adjusts line thickness
    :param orientation: positioning of the arm, default is HORIZONTAL
    :return:
    """
    vars = astro_symbol_defaults(d, primary_colour, secondary_colour, wid, hei, x_start, y_start,
                                 size_ratio, stretch_ratio, sharp_ratio, sparse_ratio, thick_ratio, orientation)
    wid, hei, x_mid, y_mid, x_end, y_end, sw, radius, arm_length, cross_length, joint_length, rotateby = vars
    # the arm
    if rotateby != 0:
        p = draw.Path(stroke=primary_colour, stroke_width=sw, transform=f'rotate({rotateby},{x_mid},{y_mid})', fill='none')
    else:
        p = draw.Path(stroke=primary_colour, stroke_width=sw, fill='none')
    path_arm(p, x_mid, y_mid, radius, arm_length)

    bump_height = sw*1.5
    bump_top =  y_mid+radius+joint_length
    bump_bottom = bump_top + bump_height
    bump_width = cross_length*1.25
    left = x_mid - bump_width
    cx_len = sw*0.4*sparse_ratio
    right = x_mid + bump_width
    p.M(left, bump_bottom)
    p.C(left+cx_len, bump_top, x_mid-cx_len, bump_top, x_mid, bump_bottom)
    p.C(x_mid+cx_len, bump_top, right-cx_len, bump_top, right, bump_bottom)
    d.append(p)


if __name__ == '__main__':
    doctest.testmod()
    wid = 500
    hei = 300
    d = draw.Drawing(wid, hei)
    draw_horiz_bars(d, ['#69F369'])
    '''
    draw_venus(d, 'white', orientation=HORIZONTAL)
    draw_venus(d, 'white', orientation=UPSIDE)
    draw_mars(d, 'yellow')
    draw_transmarsvenus(d, 'orange')
    '''
    sparse = 1.0
    sharp = 1.0
    thick = 1.0
    #draw_venus_symbol(d, 'black', stretch_ratio=1.0, sharp_ratio=sharp, size_ratio=1.1, y_start=-.03*d.height, sparse_ratio=sparse, thick_ratio=thick)
    #draw_transmarsvenus(d, 'black', stretch_ratio=1.0, sharp_ratio=sharp, size_ratio=1.1, y_start=-.03*d.height, sparse_ratio=sparse, thick_ratio=thick)
    #draw_mars_symbol(d, 'black', stretch_ratio=1.0, sharp_ratio=sharp, size_ratio=1.1, y_start=-.03*d.height, sparse_ratio=sparse, thick_ratio=thick)
    draw_mercury_symbol(d, 'black', stretch_ratio=1.0, sharp_ratio=sharp, size_ratio=1.1, y_start=-.03*d.height, sparse_ratio=sparse, thick_ratio=thick)
    d.save_svg('drawflags/test.svg')

    d = draw.Drawing(wid, hei)
    draw_horiz_bars(d, ['#ED058D', '#0091D4'])
    draw_xenous_symbol(d, 'white', y_start=-.03*d.height, thick_ratio=.6)
    d.save_svg('drawflags/test2.svg')