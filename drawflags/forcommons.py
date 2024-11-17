import sys
sys.path.insert(0, 'processflags/')
from utils import *

# some useful colours
intersex_yellow = '#FDD70A'
intersex_purple = '#7A01AA'
trans_pink = '#F5A9B8'
trans_blue = '#5BCEFA'
trans_stripes = [trans_pink, trans_blue, 'white', trans_blue, trans_pink]
disability_stripes = ['#CF7280', '#EEDE77', '#E8E8E8', '#7BC2E0', '#3CB07D']
disability_grey = '#595959'

if __name__ == '__main__':
    commonsflags = 'output/commons/'

    # making SVG version for https://commons.wikimedia.org/wiki/File:Australian_Gay_Pride_Flag_with_Aboriginal_Flag.svg
    indig_red = '#fd0a00'
    d = draw.Drawing(800*2, 400*2)
    draw_horiz_bars(d, ['#f49ac0']) # background
    # coordinate/size calculations
    leftwid = d.width/2
    circle_size = 0.55
    upper_height = d.height/2
    lower_height = d.height-upper_height
    lower_start = lower_height
    left_size = 1.25
    rightwid = d.width-leftwid
    right_start = d.width*0.99
    # flag elements
    bh = draw_horiz_bars(d, ['black', indig_red], wid=leftwid, hei=upper_height)
    draw_circle(d, '#ffd700', size_ratio=circle_size, wid=leftwid, hei=upper_height)
    draw_australian_star(d, 'white',  wid=leftwid, hei=lower_height, y_start=lower_start, size_ratio=left_size)
    draw_southern_cross(d, 'white', wid=d.width/2, x_start=right_start)
    filelocations = save_flag(d, 'aus_indigenous_gay_1:2',  commonsflags)

    # https://commons.wikimedia.org/wiki/File:Australian_Gay_Pride_Flag_with_Aboriginal_Flag_(2-3).svg
    d = draw.Drawing(800*2, 533*2)
    draw_horiz_bars(d, ['#f49ac0'])
    # coordinate/size calculations
    leftwid = d.width*0.435
    upper_height = leftwid*(3/5)*1.05
    lower_height = d.height-upper_height
    lower_start = upper_height*1.15
    left_size = 1
    rightwid = d.width-leftwid
    right_start = d.width*0.95
    # flag elements
    bh = draw_horiz_bars(d, ['black', indig_red], wid=leftwid, hei=upper_height)
    draw_circle(d, '#ffff01', size_ratio=circle_size, wid=leftwid, hei=upper_height)
    draw_australian_star(d, 'white',  wid=leftwid, hei=lower_height, y_start=lower_start, size_ratio=left_size)
    draw_southern_cross(d, 'white', wid=d.width/2, x_start=right_start)
    filelocations = save_flag(d,  'aus_indigenous_gay_2:3', commonsflags)

    # https://commons.wikimedia.org/wiki/File:Australian_LGBT_Flag_with_Aboriginal_Flag.svg
    rainbow_stripes = ['#e50800', '#ff8d00', '#ffee00', '#038121', '#0c4cff', '#770288']
    indig_red = '#fd0a00'
    d = draw.Drawing(800*2, 400*2) #500*4, 300*4)
    draw_horiz_bars(d, rainbow_stripes)
    # coordinate/size calculations
    leftwid = d.width/2
    circle_size = 0.6 # why didn't the flag designer keep this consistent???
    upper_height = d.height/2
    lower_height = d.height-upper_height
    lower_start = lower_height
    left_size = 1.25
    rightwid = d.width-leftwid
    right_start = d.width*0.99
    # flag elements
    bh = draw_horiz_bars(d, ['black', '#cc0600'], wid=leftwid, hei=upper_height)
    draw_circle(d, '#ffff00', size_ratio=circle_size, wid=leftwid, hei=upper_height)
    draw_australian_star(d, 'white',  wid=leftwid, hei=lower_height, y_start=lower_start, size_ratio=left_size)
    draw_southern_cross(d, 'white', wid=d.width/2, x_start=right_start)
    filelocations = save_flag(d,  'aus_indigenous_rainbow_1:2', commonsflags)

    # https://commons.wikimedia.org/wiki/File:Australian_Gay_Pride_with_Aboriginal_Flag_(Rainbow_Crux_2-3).svg
    d = draw.Drawing(800*2, 533*2)
    draw_horiz_bars(d, ['#f49ac0'])
    # coordinate/size calculations
    leftwid = d.width*0.435
    upper_height = leftwid*(3/5)*1.05
    lower_height = d.height-upper_height
    lower_start = upper_height*1.15
    left_size = 1
    rightwid = d.width-leftwid
    right_start = d.width*0.95
    # flag elements
    bh = draw_horiz_bars(d, ['black', indig_red], wid=leftwid, hei=upper_height)
    draw_circle(d, '#ffff01', size_ratio=circle_size, wid=leftwid, hei=upper_height)
    sw = draw_australian_star(d, '#0b3cff', 'white',  wid=leftwid, hei=lower_height, y_start=lower_start, size_ratio=left_size)
    draw_southern_cross(d, ['#fd0a00', '#ff8500', '#fffc00', '#307500', '#7d02b1'], 'white', wid=d.width/2, x_start=right_start, sw=sw)
    filelocations = save_flag(d, 'aus_indigenous_gay_rainbowstars_2:3', commonsflags)

    # https://commons.wikimedia.org/wiki/File:Australian_Gay_Pride_with_Aboriginal_Flag_(Rainbow_Crux).svg
    indig_red = '#fd0a00'
    d = draw.Drawing(800*2, 400*2)
    draw_horiz_bars(d, ['#f49ac0']) # background
    # coordinate/size calculations
    leftwid = d.width/2
    circle_size = 0.55
    upper_height = d.height/2
    lower_height = d.height-upper_height
    lower_start = lower_height
    left_size = 1.25
    rightwid = d.width-leftwid
    right_start = d.width*0.99
    # flag elements
    bh = draw_horiz_bars(d, ['black', indig_red], wid=leftwid, hei=upper_height)
    draw_circle(d, '#ffd700', size_ratio=circle_size, wid=leftwid, hei=upper_height)
    sw = draw_australian_star(d, '#0b3cff', 'white',  wid=leftwid, hei=lower_height, y_start=lower_start, size_ratio=left_size)
    draw_southern_cross(d, ['#fd0a00', '#ff8500', '#fffc00', '#307500', '#7d02b1'], 'white', wid=d.width/2, x_start=right_start, sw=sw)
    filelocations = save_flag(d, 'aus_indigenous_gay_rainbowstars_1:2',  commonsflags)