import drawsvg

from gender_symbols import *

def draw_pocketgender_hourglass(d, colours,
                                wid=UNSPECIFIED, hei=UNSPECIFIED, x_start=0, y_start=0,
                                size_ratio=1.0, stretch_ratio=1.0, sharp_ratio=1.0, sparse_ratio=1.0, thick_ratio=1.0,
                                orientation=HORIZONTAL):
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
                    size_ratio=1.0, stretch_ratio=1.0, sharp_ratio=1.0, sparse_ratio=1.0, thick_ratio=1.0,
                    orientation=HORIZONTAL):
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


def draw_nautilus(d, colours, border_colour='black',
                  wid=UNSPECIFIED, hei=UNSPECIFIED, x_start=0, y_start=0,
                  size_ratio=1.0, stretch_ratio=1.0, sharp_ratio=1.0, sparse_ratio=1.0, thick_ratio=1.0,
                  orientation=HORIZONTAL):
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
    border_width = 5 * size_ratio * (1-sharp_ratio)
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


def draw_trichevron(d, colours,
                    wid=UNSPECIFIED, hei=UNSPECIFIED, x_start=0, y_start=0,
                    size_ratio=1.0, stretch_ratio=1.0, sharp_ratio=1.0, sparse_ratio=1.0, thick_ratio=1.0,
                    orientation=HORIZONTAL):
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
                      size_ratio=1.0, stretch_ratio=1.0, sharp_ratio=1.0, sparse_ratio=1.0, thick_ratio=1.0,
                      orientation=HORIZONTAL):
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


def draw_longhair(d, colours,
                  wid=UNSPECIFIED, hei=UNSPECIFIED, x_start=0, y_start=0,
                  size_ratio=1.0, stretch_ratio=1.0, sharp_ratio=1.0, sparse_ratio=1.0, thick_ratio=1.0,
                  orientation=HORIZONTAL):
    """
    Draw stripes in the style of the Longhair flag
    :param d: Drawing object
    :param colours: left to right
    :param wid: width of the area we are working with
    :param hei: height of the area we are working with
    :param x_start: the x-coordinate of the upper left corner of the rectangular area that is being drawn into
    :param y_start: the y-coordinate of the upper left corner of the rectangular area that is being drawn into
    :param size_ratio: size factor: how much of the width the lines take up
    :param stretch_ratio: how much more width the lines are at bottom than top
    :param thick_ratio: changes the height of the upper part
    :return: the height of the top part
    """
    wid, hei, x_mid, y_mid, x_end, y_end = get_standard_dimensions(d, wid, hei, x_start, y_start)
    bottom_width = size_ratio*stretch_ratio*(wid/2)
    top_width = size_ratio*(wid/4)

    top_start = x_start + (wid - top_width)/2
    bottom_start = x_start + (wid - bottom_width)/2
    top_each = top_width / len(colours)
    bottom_each = bottom_width / len(colours)

    # d.append(drawsvg.Circle(x_mid, y_start+top_each*5*thick_ratio, 1.4*top_width/2, fill='white'))
    y_head = y_start + top_each * thick_ratio * 2.5 * 1.3
    extra_thick = top_width * 0.1
    cy = y_head - top_width * 0.5
    cyq = y_head - top_width * 0.66
    cp = draw.Path(fill='white')
    cp.M(bottom_start, y_end)
    cp.L(bottom_start + bottom_each*len(colours), y_end)
    cp.L(top_start + top_each*len(colours) + extra_thick, y_head)
    # p.C(curr_top_left+extra_thick, cy, top_start-extra_thick, cy, top_start-extra_thick, y_head)
    cp.Q(x_mid, cyq, top_start - extra_thick, y_head)
    cp.L(bottom_start, y_end).Z()
    clip = draw.ClipPath()
    clip.append(cp)

    curr_top_left = top_start
    curr_bottom_left = bottom_start
    for i, c in enumerate(colours):
        p = draw.Path(fill=c, clip_path=clip)
        p.M(curr_top_left, y_start)
        p.L(curr_bottom_left, y_end)
        curr_top_left += top_each
        curr_bottom_left += bottom_each
        p.L(curr_bottom_left, y_end)
        p.L(curr_top_left, y_start).Z()
        d.append(p)
    return y_head


def draw_x_gender(d, colours,
                  wid=UNSPECIFIED, hei=UNSPECIFIED, x_start=0, y_start=0,
                  size_ratio=1.0, stretch_ratio=1.0, sharp_ratio=1.0, sparse_ratio=1.0, thick_ratio=1.0,
                  orientation=HORIZONTAL):
    """
    Draw an X in the style of the X gender flag
    :param d: Drawing object
    :param colours: left to right top to bottom (there should be four)
    :param wid: width of the area we are working with
    :param hei: height of the area we are working with
    :param x_start: the x-coordinate of the upper left corner of the rectangular area that is being drawn into
    :param y_start: the y-coordinate of the upper left corner of the rectangular area that is being drawn into
    :param size_ratio: size factor: how much of the width the lines take up
    :param stretch_ratio: how much more width the lines are at bottom than top
    :param thick_ratio: changes the height of the upper part
    :return: the height of the top part
    """
    wid, hei, x_mid, y_mid, x_end, y_end = get_standard_dimensions(d, wid, hei, x_start, y_start)
    base_ratio = 10
    line_width = thick_ratio*(wid/base_ratio)
    line_height = thick_ratio*stretch_ratio*(hei/base_ratio)

    assert len(colours) >= 4, 'X-gender needs at least 4 colours'

    # upper left
    p = draw.Path(fill=colours[0])
    p.M(x_start, y_start)
    p.L(x_start+line_width, y_start)
    p.L(x_mid, y_mid-line_height)
    p.L(x_mid, y_mid)
    p.L(x_mid-line_width, y_mid)
    p.L(x_start, y_start+line_height)
    p.Z()
    d.append(p)

    # upper right
    p = draw.Path(fill=colours[1])
    p.M(x_end, y_start)
    p.L(x_end-line_width, y_start)
    p.L(x_mid, y_mid-line_height)
    p.L(x_mid, y_mid)
    p.L(x_mid+line_width, y_mid)
    p.L(x_end, y_start+line_height)
    p.Z()
    d.append(p)

    # lower left
    p = draw.Path(fill=colours[2])
    p.M(x_start, y_end)
    p.L(x_start+line_width, y_end)
    p.L(x_mid, y_mid+line_height)
    p.L(x_mid, y_mid)
    p.L(x_mid-line_width, y_mid)
    p.L(x_start, y_end-line_height)
    p.Z()
    d.append(p)

    # lower right
    p = draw.Path(fill=colours[3])
    p.M(x_end, y_end)
    p.L(x_end-line_width, y_end)
    p.L(x_mid, y_mid+line_height)
    p.L(x_mid, y_mid)
    p.L(x_mid+line_width, y_mid)
    p.L(x_end, y_end-line_height)
    p.Z()
    d.append(p)


def draw_lines(d, colours,
               wid=UNSPECIFIED, hei=UNSPECIFIED, x_start=0, y_start=0,
               size_ratio=1.0, stretch_ratio=1.0, sharp_ratio=1.0, sparse_ratio=1.0, thick_ratio=1.0,
               orientation=HORIZONTAL):
    siding = ['none']*4
    new_colours = siding + colours + siding
    draw_stripes(d, new_colours, orientation=orientation, wid=wid, hei=hei, x_start=x_start, y_start=y_start,
                 size_ratio=size_ratio, stretch_ratio=stretch_ratio, thick_ratio=thick_ratio)



if __name__ == '__main__':
    doctest.testmod()
    wid = 1200
    hei = 720

    orien = HORIZONTAL

    d = draw.Drawing(wid, hei)
    draw_horiz_bars(d, ['#f8d209'])
    draw_longhair(d, RAINBOW, thick_ratio=1, stretch_ratio=1.5, size_ratio=1.5)
    d.save_svg('drawflags/test.svg')

    d = draw.Drawing(wid, hei)
    draw_horiz_bars(d, ['#f8d209'])
    draw_x_gender(d, RAINBOW)
    d.save_svg('drawflags/test2.svg')