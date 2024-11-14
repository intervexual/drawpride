"""
Draw rings for pride flags, mostly intersex-related.
"""

from pride_stripes import *

##########################################################
# helpers for making Carpenter-style rings
# getter methods to avoid magic numbers in my code
##########################################################

def top_of_ring(hei):
    '''Top of the ring on a Carpenter flag.'''
    return 21 * (hei / 100)

def bottom_of_ring(hei):
    '''Bottom of the top of the ring on a Carpenter flag.'''
    return 29 * (hei / 100)

def ring_thickness(hei):
    '''Width of the ring.'''
    return 8 * (hei / 100)

def base_of_ring(hei):
    '''Top of the bottom of the ring.'''
    return 71 * (hei / 100)

def outer_left_of_ring(hei):
    return 35 * (hei / 100)

def inner_left_of_ring(hei):
    return 39 * (hei / 100)

def inner_right_of_ring(hei):
    return 60 * (hei / 100)

##########################################################
# Functions for draw rings in the style of the Carpenter intersex flag
##########################################################

def draw_transparent_ring(d, colour_of_ring, fill_colour='none', wid=UNSPECIFIED, hei=UNSPECIFIED,
                          opac=1, size_ratio=1.0, x_start=0, y_start=0, orientation=VERTICAL):
    '''Draw a ring with a transparent fill, of the size for a Carpenter flag
    Useful for making the intersex flag.

    dimensions: wid x hei (int x int)
    colour_of_ring: the fill of the ring itself (hex code as str)
    opac: opacity of the fill inside the ring (0-1 float)
    fill_colour: colour that goes *inside* the ring (hex code as str)
    '''
    wid, hei = get_effective_dimensions(d, wid, hei)

    width_of_ring = ring_thickness(hei)  # 29-21
    top_o = top_of_ring(hei) + width_of_ring / 2  # for a 100px

    width_of_ring *= size_ratio
    top_o *= size_ratio

    centre_x = (wid/2)+x_start
    centre_y = (hei/2)+y_start
    d.append(draw.Circle(centre_x, centre_y, top_o,
                         fill=fill_colour, stroke_width=width_of_ring, stroke=colour_of_ring, fill_opacity=opac))


def fill_outside_the_ring(d, fill_colour, border_width, wid=UNSPECIFIED, hei=UNSPECIFIED, opac=0):
    '''Fill everything outside a Carpenter ring... with a bigger ring!
    Useful for if you want to shade out everything outside the ring.

    dimensions: wid x hei (int x int)
    border_width: the size of the border around the presumed Carpenter ring in the middle
        this is here to ensure that when you colour outside the ring, you don't colour
        over any border you drew with draw_border_ring.

    fill_colour: hex code as str.
    The fill colour only matters if the opacity isn't 0

    opacity: float 0-1'''
    wid, hei = get_effective_dimensions(d, wid, hei)
    width_of_ring = hei + 2 * top_of_ring(hei) - border_width  # was hei + 41 for bord width
    d.append(draw.Circle(wid / 2, hei / 2, hei,
                         fill=fill_colour, stroke_width=width_of_ring, stroke=fill_colour, opacity=opac,
                         fill_opacity=0))

def draw_border_ring(d, border_colour, border_width, wid=UNSPECIFIED, hei=UNSPECIFIED, opac=0, fill_colour = 'white'):
    '''Draw a ring slightly larger than the Carpenter sized ring.
    Intended for making a border around a Carpenter ring.

    dimensions: wid x hei (int x int)
    border_colour: the fill of the ring itself (hex code as str)
    width: the width in pixels (int) of this ring border ring.
    opac: opacity of the fill inside the ring (0-1 float)
    fill_colour: colour that goes *inside* the ring (hex code as str)
    '''
    wid, hei = get_effective_dimensions(d, wid, hei)
    width_of_ring = ring_thickness(hei) + 2*border_width # 2x so it's on both sides
    top_o = top_of_ring(hei) + ring_thickness(hei)/2 # for a 100px

    d.append(draw.Circle(wid/2, hei/2, top_o,
        fill=fill_colour, stroke_width=width_of_ring, stroke=border_colour, fill_opacity=opac))


def draw_inset_into_intersex(d, stripes, outer_colour, ring_colour, wid=UNSPECIFIED, hei=UNSPECIFIED, orientation=HORIZONTAL):
    '''Given a list of stripes,
    draw the striped flag inside the ring of a Carpenter style intersex flag.

    dimensions: wid x hei (int)
    stripes: list of str hex codes
    outer_colour: str hex code for the background outside the ring
    is_vertical: str ('V' vertical, 'H' horizontal, 'D' diagonal)
    '''
    wid, hei = get_effective_dimensions(d, wid, hei)
    stp_h = 0
    if VERTICAL in orientation:
        constr_left = inner_left_of_ring(wid)
        constr_wid = inner_right_of_ring(wid) - inner_left_of_ring(wid) + 1
        stp_h = constr_wid
        draw_vert_bars(d, stripes, constr_wid, hei,  constr_left)
    elif HORIZONTAL in orientation:
        constr_top = bottom_of_ring(hei)
        constr_hei = base_of_ring(hei) - bottom_of_ring(hei)  # 29 at top, 70 at bottom
        stp_h = constr_hei
        draw_horiz_bars(d,  stripes,  wid, constr_hei, y_start=constr_top)
    else:
        constr_left = inner_left_of_ring(wid)
        constr_hei =base_of_ring(hei) - bottom_of_ring(hei)  # 29 at top, 70 at botto
        constr_wid = constr_hei*(wid/hei) #inner_right_of_ring(wid) - inner_left_of_ring(wid) + 1
        constr_top = bottom_of_ring(hei)
        stp_h = constr_wid
        # x_offset=(d.width/2)-new_wid/2
        xoff = (d.width/2)-constr_wid/2
        yoff = (d.height/2)-constr_hei/2
        draw_diagonal_stripes(d, constr_wid, constr_hei, stripes, x_start=xoff, y_start=yoff)

    draw_transparent_ring(d, ring_colour, fill_colour='none')
    opacity = 1
    bord_wid = 1
    draw_border_ring(d, ring_colour, bord_wid)
    fill_outside_the_ring(d,  outer_colour, bord_wid, opac=opacity)
    return stp_h


def draw_segmented_ring(d, colours, wid=UNSPECIFIED, hei=UNSPECIFIED, fill_colour = 'none',
                        opac = 1, size_ratio=1.0, border_fill='none', border_ratio=2, orientation=VERTICAL,
                        x_start=0, y_start=0):
    '''
    Draw a segmented ring flag.
    dimensions of image: wid x hei
    colours: list of hex code strings for colouring the ring segments
    fill_colour: colour inside the ring
    border_colour: border between segments, str hex code
    border_width: the width in pixels of the border (int)
    ang_offset = from where to start drawing the segments
    '''
    wid, hei = get_effective_dimensions(d, wid, hei)
    arc_width = 360 / len(colours)
    width_of_ring = ring_thickness(hei)*size_ratio  # 29-21
    top_o = top_of_ring(hei) + width_of_ring / 2  # for a 100px

    ang_offset = angle_offset_for_orientation(orientation)
    x_centre = (wid/2)+x_start
    y_centre = (hei/2)+y_start

    if border_fill != 'none':
        border_ring = draw.Circle(x_centre, y_centre, top_o, stroke=border_fill, fill='none', stroke_width=width_of_ring*border_ratio)
        d.append(border_ring)

    rad = top_o*3 # used for the clip
    for i, c in enumerate(colours):
        stop1 = get_triangle_coords(rad, arc_width, i, cent_x=x_centre, cent_y=y_centre, offset=ang_offset)
        stop2 = get_triangle_coords(rad, arc_width, i+1, cent_x=x_centre, cent_y=y_centre, offset=ang_offset)
        stopM = get_triangle_coords(rad, arc_width, i+0.5, cent_x=x_centre, cent_y=y_centre, offset=ang_offset)
        # need a middle stop so it still works when n=2

        p = draw.Path(stroke='black', stroke_width=2, fill=c)
        p.M(x_centre, y_centre).L(*stop1).L(*stopM).L(*stop2).L(x_centre, y_centre).Z()

        clip = draw.ClipPath()
        clip.append(p)
        ring = draw.Circle(x_centre, y_centre, top_o,
                           fill=fill_colour, stroke_width=width_of_ring, stroke=c, fill_opacity=opac,
                           clip_path=clip)
        d.append(ring)


def draw_ring(d, wid, hei, radius, thickness, ring_colour, fill_colour , opacity = 0):
    '''Helper function for intersex flag mashups
    image dimensions: wid x hei (int x int)
    radius: radius of the ring in pixels (int)
    thickness: thickness of the ring in pixels (int)
    colour_of_ring: the fill of the ring itself (hex code as str)
    opac: opacity of the fill inside the ring (0-1 float)
    fill_colour: colour that goes *inside* the ring (hex code as str)
    '''
    width_of_ring = thickness
    top_o = radius #(hei/2) - thickness - radius

    d.append(draw.Circle(wid/2, hei/2, top_o,
        fill=fill_colour, stroke_width=thickness, stroke=ring_colour, fill_opacity=opacity))



def draw_concentric_rings(d, colours, wid=UNSPECIFIED, hei=UNSPECIFIED,
                          border_colour='none', border_thickness=0, inner_colour='none', size_ratio=1.0):
    """
    Draw concentric rings approximately the size of a Carpenter ring. Intended for intersex flag mashups.
    :param d: Drawing object
    :param colours: colours of the concentric rings
    :param wid: width of the area that the rings are being added to
    :param hei: height of the area that the rings are being added to
    :param border_colour: possible colour for outlining the concentric rings
    :param border_thickness: thickness in pixels if adding a border
    :param inner_colour: colour used to fill inside the innermost ring
    :param size_ratio: scaling factor
    :return: none
    """
    wid, hei = get_effective_dimensions(d, wid, hei)

    # the basic circle
    thickness = (2 * ring_thickness(hei)) / (len(colours))
    # radius = thickness*4
    # top_of_ring(hei) -  ring_thickness(hei) / (2*len(colours)-2)

    radius = top_of_ring(hei)*size_ratio

    fudge = max(d.height/800,1)
    draw_ring(d, wid, hei, radius, thickness + fudge, colours[0], fill_colour=inner_colour, opacity=1)
    # draw rings around it
    i = 0
    while i < len(colours) - 1:
        # print(i)
        draw_ring(d, wid, hei, math.ceil(radius + (i + 1) * thickness), thickness + fudge, colours[i + 1], 'none')
        i += 1

    # border inside
    draw_ring(d, wid, hei, radius - (thickness / 2), border_thickness, border_colour, 'none')
    # border outside
    draw_ring(d, wid, hei, radius + (i + 1) * thickness - (thickness / 2), border_thickness, border_colour, 'none')




def draw_bullseye(d, colours, wid=UNSPECIFIED, hei=UNSPECIFIED, size_ratio=1.0):
    """
    Draw concentric rings inside the intersex ring. All ring widths will be the same.
    :param d: Drawing object
    :param colours: list of str (colours)
    :param size_ratio: scaling factor
    :return: none
    """
    wid, hei = get_effective_dimensions(d, wid, hei)
    radius = top_of_ring(hei)*size_ratio

    width_of_ring = ring_thickness(hei)  # 29-21
    top_o = top_of_ring(hei) + width_of_ring / 2  # the external radius of the whole thing

    width_of_ring *= size_ratio

    thickness = top_o / len(colours)
    fudge = 0

    # do the inner one first
    d.append(draw.Circle(wid/2, hei/2, thickness, fill=colours[-1]))

    i = 0
    while i < len(colours) - 1:
        # print(i)
        draw_ring(d, wid, hei, math.ceil(radius - (i + 1) * thickness), thickness + fudge, colours[i + 1], 'none')
        i += 1
    # do the outer one last
    draw_ring(d, wid, hei, math.ceil(radius), thickness + fudge, colours[0], 'none')


def draw_inner_bullseye(d, colours, wid=UNSPECIFIED, hei=UNSPECIFIED, size_ratio=1.0):
    """
    Draw concentric rings inside the intersex ring (outer ring will always have the standard thickness)
    :param d: Drawing object
    :param colours: list of str (colours)
    :param size_ratio: scaling factor
    :return: none
    """
    wid, hei = get_effective_dimensions(d, wid, hei)
    width_of_ring = ring_thickness(hei)  # 29-21

    width_of_ring *= size_ratio
    radius = (top_of_ring(hei)+(width_of_ring/3))*size_ratio # the radius INSIDE the outer ring

    thickness  = radius/(len(colours)-1)
    fudge = max(hei/100, 1)

    # do the inner one first
    d.append(draw.Circle(wid/2, hei/2, thickness, fill=colours[-1]))

    # outer ring
    draw_transparent_ring(d, d.width, d.height, colours[0], 'none', size_ratio=size_ratio)

    i = 0
    while i < len(colours) - 1:
        draw_ring(d, wid, hei, math.ceil(radius - (i + 1) * thickness), thickness + fudge, colours[i + 1], 'none')
        i += 1



if __name__ == '__main__':
    wid = 500
    hei = 300
    d = draw.Drawing(wid, hei)
    draw_horiz_bars(d, ['yellow'])
    draw_transparent_ring(d, wid, hei, 'purple', 'none')
    draw_inset_into_intersex(d, wid, hei, ['pink', 'blue', 'white', 'blue', 'pink'], 'yellow', 'purple', HORIZONTAL)
    draw_segmented_ring(d, wid, hei, ['purple', 'magenta'], ang_offset=VERTICAL)
    d.save_png('drawflags/test.png')