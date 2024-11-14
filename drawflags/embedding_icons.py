"""
Adding SVG icons to flags rather than creating them in drawsvg
"""
import os
from pride_shapes import *


def embed_icon(d, path_to_icon, colours, icondir='icons/', orientation=None,
               wid=UNSPECIFIED, hei=UNSPECIFIED, x_start=0, y_start=0, size_ratio=1.0,
               name='ch'):
    """
    Wrapper for various ways of adding/embedding icons.
    :param d: Drawing object
    :param path_to_icon: filename of SVG to be embedded, as string
    :param colours: dictionary with colours to remap
    :return:
    """
    wid, hei = get_effective_dimensions(d, wid, hei)
    path_to_icon = icondir + path_to_icon
    if colours:
        changes = {}
        if type(colours) == dict:
            changes = colours
        elif type(colours) == str:
            changes = {'#000000': colours}
        elif type(colours) == list:
            changes = {'#000000': colours[0]}
        assert type(changes) == dict
        for to_replace in changes:
            if changes[to_replace].lower() != to_replace.lower():
                path_to_icon = change_svg_colour(path_to_icon, changes[to_replace], to_replace, name=name)
    if orientation == CENTRAL:
        add_icon_by_embedding(d, path_to_icon, size_ratio * hei)
    elif orientation == CENTRAL+VERTICAL:
        add_icon_by_embedding(d, path_to_icon, size_ratio * wid)
    else:
        add_icon_by_embedding(d, path_to_icon, size_ratio*hei, wid=wid, hei=hei)


def add_icon_by_embedding(d, path_to_icon, icon_hei, wid=UNSPECIFIED, hei=UNSPECIFIED):
    """
    Embed an icon into the flag. Note that svgs produced this way will not be accepted on Wikimedia Commons.
    :param d: Drawing object
    :param path_to_icon: filename of SVG to be embedded, as string
    :param icon_hei: height in pixels that the icon should be when added
    :param wid: width that makes up the area that is being drawn into (in pixels)
    :param hei: height that makes up the area that is being drawn into (in pixels)
    :return: none
    """
    wid, hei = get_effective_dimensions(d, wid, hei)

    icon_wid = icon_hei  # assumes a square input svg!!!
    d.append(draw.Image((wid / 2) - icon_wid / 2, (hei / 2) - icon_hei / 2,
                        icon_wid, icon_hei, path_to_icon, embed=True, dominant_baseline='middle'))


def change_svg_colour(filepath, new_colour, old_colour, save_to_dir = 'output/icons/', name=''):
    """
    Open an SVG file, change its colours, save it for later use
    :param filepath: string filename of input SVG file
    :param new_colour: the colour to be added
    :param old_colour: the colour to be replaced in favour of new_colour
    :return: none
    """
    with open(filepath, 'r') as f:
        s = f.read()

    found = False
    if type(old_colour) == str:
        old_options = [old_colour, old_colour.lower(), old_colour.upper()]
        for old in old_options:
            found = (old in s) or found
            s = s.replace(old, new_colour)
        if not found:
            print('Warning: no colour change to', filepath, old_colour)
    else:
        print('Warning: old colour was not string and hence not changed', filepath, old_colour)

    endpath = filepath.split('/')[-1]

    if not name.endswith(':'):
        name += ':'
    if not os.path.exists(save_to_dir):
        os.makedirs(save_to_dir)
    newpath =  save_to_dir + name + endpath
    with open(newpath, 'w') as g:
        print(s, file=g)
    return newpath


if __name__ == '__main__':
    wid = 500
    hei = 300
    d = draw.Drawing(wid, hei)
    draw_horiz_bars(d, ['yellow'])
    fp = 'icons/gendersex/yinyangren.svg'
    new_fp = change_svg_colour(fp, 'purple', '#fdfdfd')
    add_icon_by_embedding(d, new_fp, hei/2)
    d.save_png('drawflags/test.png')
    d.save_svg('drawflags/test.svg')