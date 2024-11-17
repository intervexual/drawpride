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

    # https://commons.wikimedia.org/wiki/File:Flag_of_Morocco_LGBT.svg
    rainbow_stripes = ['#fe0a00', '#ff9800', '#ffFF00', '#307500', '#0b3cff', '#7d02b1']
    d = draw.Drawing(800*4, 533*4) #500*4, 300*4)
    draw_horiz_bars(d, rainbow_stripes)
    draw_morocco_star(d, '#026233')
    filelocations = save_flag(d, 'morocco_rainbow',  commonsflags)

    # https://commons.wikimedia.org/wiki/File:Wiradjuri_Aboriginal_Flag.svg
    d = draw.Drawing(800*4, 400*4)
    draw_horiz_bars(d, ['black', '#db0701'])
    draw_southern_cross(d, '#fdc82e', x_start=d.width*0.01)
    filelocations = save_flag(d, 'wiradjuri_aboriginal', commonsflags)

    # https://commons.wikimedia.org/wiki/File:LGBT_Flag_of_Czechoslovakia_(Unofficial_civil).svg
    rainbow_stripes = ['#d81525', '#ff6300', '#ffFF00', '#329c00', '#0600ce', '#ce32ff']
    d = draw.Drawing(800*4, 533*4)
    draw_horiz_bars(d, rainbow_stripes)
    draw_pile(d, '#11457e', size_ratio=1.5)
    draw_fivesided_star(d, '#de0700', secondary_size=0.38, wid=d.width/2, size_ratio=1.15, y_start=-d.height*0.205)
    filelocations = save_flag(d, 'czechoslovakia_civil_rainbow', commonsflags)

    # https://commons.wikimedia.org/wiki/File:Gay_Pride_Flag_of_the_Czechoslovakia_(Unofficial_civil).svg
    d = draw.Drawing(800*4, 533*4)
    draw_horiz_bars(d, ['white', '#fe0a00'])
    draw_pile(d, '#f493f4', size_ratio=1.5)
    draw_fivesided_star(d, '#de0700', secondary_size=0.38, wid=d.width*0.535, size_ratio=1.11, y_start=-d.height*0.19)
    filelocations = save_flag(d, 'czechoslovakia_civil_gay', commonsflags)

    # https://commons.wikimedia.org/wiki/File:Flag_of_Czechoslovakia_Bisexual_Vaporwave_(Unofficial_civil).svg
    d = draw.Drawing(800 * 4, 533 * 4)
    draw_horiz_bars(d, ['white', '#ff0a77'])
    draw_pile(d, '#39d0e0', size_ratio=1.5)
    draw_fivesided_star(d, '#de0700', secondary_size=0.38, wid=d.width * 0.535, size_ratio=1.11,
                        y_start=-d.height * 0.19)
    filelocations = save_flag(d, 'czechoslovakia_civil_bi_vaporwave', commonsflags)

    # https://commons.wikimedia.org/wiki/File:Flag_of_the_Czechoslovakia_Bisexual_(Unofficial_civil).svg
    d = draw.Drawing(800 * 4, 533 * 4)
    draw_horiz_bars(d, ['white', '#ff0a77'])
    draw_pile(d, '#0500be', size_ratio=1.5)
    draw_fivesided_star(d, '#de0700', secondary_size=0.38, wid=d.width * 0.535, size_ratio=1.11,
                        y_start=-d.height * 0.19)
    filelocations = save_flag(d, 'czechoslovakia_civil_bi', commonsflags)

    # https://commons.wikimedia.org/wiki/File:LGBT_Flag_of_Czechoslovakia_Vaporwave_(Unofficial_civil).svg
    rainbow_stripes = ['#d81525', '#ff6300', '#ffFF00', '#329c00', '#0600ce', '#ce32ff']
    d = draw.Drawing(800 * 4, 533 * 4)
    draw_horiz_bars(d, rainbow_stripes)
    draw_pile(d, '#39d0e0', size_ratio=1.5)
    draw_fivesided_star(d, '#de0700', secondary_size=0.38, wid=d.width * 0.535, size_ratio=1.11,
                        y_start=-d.height * 0.19)
    filelocations = save_flag(d, 'czechoslovakia_civil_vaporwave', commonsflags)
