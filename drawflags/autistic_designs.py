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
rainbow_stripes = ['#E40303', '#FF8C00', '#FFED00', '#008026', '#24408E', '#732982']

to_show = False
outdir = 'output/intervex/'


############################### CONCENTRIC INFINITY DESIGNS

# ideas for stripes
#apd_colours = ['#2cad74', 'white', '#ffc65b', 'white', '#e43546']
roylg_colours = ['#2cad74', '#98d570', '#ffc65b',  '#f68249', '#e43546']
mad_colours = ['#796098', '#bf7998', '#796098', '#bf7998']
disabled_colours = [disability_grey] + disability_stripes + [disability_grey]
stripe_options = {'roylg':roylg_colours, 'mad':mad_colours,
                  'disabled':disabled_colours, 'lgbt':rainbow_stripes, 'trans':trans_stripes} # 'apd':apd_colours,


# ideas for backgrounds
bg_options = {'white':'white', 'whitish':'#f7f7f7', 'disgrey':disability_grey}

for bg in bg_options:
    for stripe_scheme in stripe_options:
        d = draw.Drawing(500 * 2, 300 * 2)
        draw_horiz_bars(d, [ bg_options[bg] ])
        draw_concentric_infinities(d, stripe_options[stripe_scheme], bg_options[bg], size_ratio=0.7)
        filename = f'autistic_concentric_{stripe_scheme}_on_{bg}'
        filelocations = save_flag(d, filename, outdir, same_folder=True, show_image=to_show)



############################### ICON ON A WHITE(ISH) BACKGROUND DESIGNS

spectrum_rainbow = ['#cf7280', '#dfa87c', '#eede77', '#95c77a', '#3bb07d', '#5bb9af', '#7bc2e0', '#97a7c0', '#b38da0']

icon_options = {'aufinity':'disability/aufinity_rainbow.png',
                'gold_infinity':'disability/infinity_gold_ryanyflags.svg',
                'rainbow_infinity':'disability/neurodiversity_rainbow.svg',
                'rainbow_ADHD':'disability/ADHD_butterfly_rainbow.svg',
                'nautilus':draw_nautilus
                }
sizes = {'aufinity':0.99,
         'gold_infinity':1.2,
         'rainbow_infinity':1.2,
         'rainbow_ADHD':1.1,
         'nautilus':1.25}

for bg in bg_options:
    for icon_name in icon_options:
        d = draw.Drawing(500 * 2, 300 * 2)
        draw_horiz_bars(d, [ bg_options[bg] ])
        if type(icon_options[icon_name]) == str:
            embed_icon(d, icon_options[icon_name], {}, size_ratio=sizes[icon_name])
        else:
            icon_options[icon_name](d, spectrum_rainbow, stretch_ratio=2.25, size_ratio=sizes[icon_name])
        filename = f'plain_{icon_name}_on_{bg}'
        filelocations = save_flag(d, filename, outdir, same_folder=True, show_image=to_show)


############################### ICON ON A DIAGONAL ROYLG BACKGROUND

for icon_name in icon_options:
    if 'ADHD' not in icon_name:
        d = draw.Drawing(500 * 2, 300 * 2)
        draw_diagonal_stripes(d, ['#2cad74', '#98d570'] + ['#ffc65b']*6 + ['#f68249', '#e43546'])
        scaling = 0.9
        if 'infinity' in icon_name:
            scaling = 0.8
        if type(icon_options[icon_name]) == str:
            embed_icon(d, icon_options[icon_name], {}, size_ratio=sizes[icon_name]*scaling)
        else:
            icon_options[icon_name](d, spectrum_rainbow, stretch_ratio=2.25, size_ratio=sizes[icon_name]*scaling)
        filename = f'diagonal_{icon_name}_on_roylg'
        filelocations = save_flag(d, filename, outdir, same_folder=True, show_image=to_show)


############################## ICON IN A BELT ON HORIZONTAL STRIPES

# riffing on https://www.tumblr.com/themogaidragon/762687565710213120/hi-i-just-wanted-to-ask-if-you-would-accept-an?source=share
# and https://www.tumblr.com/themogaidragon/701717045607317504/pathological-demand-avoidance?source=share

horiz_stripe_options = {'teal':['#243444',  '#3dcec1', '#eae186', 'white',  '#eae186', '#3dcec1', '#243444'],
                        'roylg':['#2cad74', '#98d570', '#ffc65b', 'white', '#ffc65b', '#f68249', '#e43546']}

for bg in horiz_stripe_options:
    for icon_name in icon_options:
        if 'ADHD' not in icon_name:
            d = draw.Drawing(500 * 2, 300 * 2)
            draw_horiz_bars(d, horiz_stripe_options[bg])
            draw_circle(d, 'white', size_ratio=0.6)
            scaling = 0.4
            if icon_name == 'aufinity':
                scaling = 0.5

            if type(icon_options[icon_name]) == str:
                embed_icon(d, icon_options[icon_name], {}, size_ratio=sizes[icon_name]*scaling)
            else:
                icon_options[icon_name](d, spectrum_rainbow, stretch_ratio=2.25, size_ratio=sizes[icon_name]*scaling)
            filename = f'horizontal_{icon_name}_on_{bg}'
            filelocations = save_flag(d, filename, outdir, same_folder=True, show_image=to_show)


