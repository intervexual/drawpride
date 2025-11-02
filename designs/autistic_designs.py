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

# canvas size - change if you want a different aspect ratio
h, w = 500*2, 300*2

############################### CONCENTRIC INFINITY DESIGNS

# ideas for stripes
roylg_colours = ['#2cad74', '#98d570', '#ffc65b',  '#f68249', '#e43546']
mad_colours = ['#796098', '#bf7998', '#796098', '#bf7998']
chem_pun = ['#edc54b', '#999592', '#f8f49d', '#999592', '#000000']
disabled_colours = [disability_grey] + disability_stripes + [disability_grey]
stripe_options = {'roylg':roylg_colours, 'mad':mad_colours,
                  'disabled':disabled_colours, 'lgbt':rainbow_stripes, 'trans':trans_stripes, 'pun':chem_pun}


# ideas for backgrounds
bg_options = {'white':'white', 'whitish':'#f7f7f7', 'disgrey':disability_grey}

for bg in bg_options:
    for stripe_scheme in stripe_options:
        d = draw.Drawing(h, w)
        draw_horiz_bars(d, [ bg_options[bg] ])
        draw_concentric_infinities(d, stripe_options[stripe_scheme], bg_options[bg], size_ratio=0.7)
        filename = f'autistic_concentric_{stripe_scheme}_on_{bg}'
        filelocations = save_flag(d, filename, outdir, same_folder=True, show_image=to_show)


############################### ICON ON A WHITE(ISH) BACKGROUND DESIGNS

spectrum_rainbow = ['#cf7280', '#dfa87c', '#eede77', '#95c77a', '#3bb07d', '#5bb9af', '#7bc2e0', '#97a7c0', '#b38da0']
#spectrum_rainbow = ['#2cad74', '#98d570', '#eede77',  '#f68249', '#e43546'][::-1] + ['#5bb9af', '#7bc2e0', '#97a7c0', '#b38da0']
                # roylg red, orange, dis yellow, roylg lime, roylg green, then rest as usual

# nautilus ideas
spectrum_rainbow_9 = ['#cf7280', '#dfa87c', '#eede77', '#95c77a', '#3bb07d', '#5bb9af', '#7bc2e0', '#97a7c0', '#b38da0']
spectrum_rainbow_8 = ['#cf7280', '#dfa87c', '#eede77', '#95c77a', '#3bb07d', '#7bc2e0', '#97a7c0', '#a78cbf']
spectrum_rainbow_7 = ['#cf7280', '#dfa87c', '#eede77', '#95c77a', '#3bb07d', '#7bc2e0', '#a78cbf']#, '#b38da0']
spectrum_rainbow_6 = ['#cf7280', '#dfa87c', '#eede77', '#3bb07d', '#7bc2e0', '#a78cbf']#, '#b38da0']

naut_options = {6:spectrum_rainbow_6, 7:spectrum_rainbow_7, 8:spectrum_rainbow_8, 9:spectrum_rainbow_9}
naut_sr = {6:3+1.75, 7:3.5, 8:4, 9:2.5}

icon_options = {'aufinity':'disability/aufinity_rainbow.png',
                'gold_infinity':'disability/infinity_gold_ryanyflags.svg',
                'bordered_infinity':'disability/gold_bordered_infinity.svg',
                'rainbow_infinity':'disability/neurodiversity_rainbow.svg',
                'rainbow_ADHD':'disability/ADHD_butterfly_rainbow.svg',
                'red_infinity':'disability/open_infinity.svg',
                'pointy_infinity':'disability/infinity_pointy.svg',
                'thick_infinity': 'disability/thick_infinity.svg',
                'brick_infinity': 'disability/bright_thick_infinity.svg',
                'gold_auf':'disability/aufinity_gold.svg',
                'yellow_auf': 'disability/aufinity_yellow.svg',
                'white_auf': 'disability/aufinity_white.svg',
                'red_auf':'disability/aufinity.svg',
                'nautilus9':draw_nautilus,
                'nautilus8':draw_nautilus,
                'nautilus7': draw_nautilus,
                'nautilus6': draw_nautilus,
                }
sizes = {'aufinity':0.99,
         'bordered_infinity':1,
         'gold_infinity':1.2,
         'rainbow_infinity':1.2,
         'rainbow_ADHD':1.1,
         'red_infinity':1.2,
         'pointy_infinity':1.2,
         'red_auf':0.8,
         'gold_auf': 0.8,
         'yellow_auf': 0.8,
         'white_auf':0.8,
         'thick_infinity':1.3,
         'brick_infinity':1.3,
         'nautilus9':1.25,
         'nautilus8': 1.15,
         'nautilus7': 1.175,
         'nautilus6': 1.15,
         }

for bg in bg_options:
    for icon_name in icon_options:
        d = draw.Drawing(h, w)
        draw_horiz_bars(d, [ bg_options[bg] ])
        size = sizes[icon_name]
        if type(icon_options[icon_name]) == str:
            embed_icon(d, icon_options[icon_name], {}, size_ratio=size)
        elif 'red_infinity' in icon_name:
            pass # TODO
        else:
            shell_num = int(icon_name[-1])
            shell_colours = naut_options[shell_num]
            sr = naut_sr[shell_num]
            if d.height == d.width:
                sr += (2.3-2.25)
                size *= 0.9
            icon_options[icon_name](d, spectrum_rainbow, stretch_ratio=sr, size_ratio=size)
        filename = f'plain_{icon_name}_on_{bg}'
        filelocations = save_flag(d, filename, outdir, same_folder=True, show_image=to_show)


############################## ICON ON DIS PRIDE BACKGROUND

# bordered_inf0_gold_3.png - 5 and 4 are too rotate-y
nd_gold = '#fac757'
nd_edge = [nd_gold]*2 + ['#ffFFff'] + [nd_gold]*2
side_diags = {'dispride':disability_stripes + [disability_grey]*15 + disability_stripes,
              'ndpride':nd_edge + ['#4d4d4d']*19 + nd_edge}

for side_name in side_diags:
    for icon_name in icon_options:
        if 'ADHD' not in icon_name:
            d = draw.Drawing(h, w)
            draw_diagonal_stripes(d, side_diags[side_name])
            scaling = 0.9
            if 'infinity' in icon_name:
                scaling = 0.8
            if type(icon_options[icon_name]) == str:
                embed_icon(d, icon_options[icon_name], {}, size_ratio=sizes[icon_name]*scaling)
            elif 'red_infinity' in icon_name:
                pass # TODO
            else:
                shell_num = int(icon_name[-1])
                shell_colours = naut_options[shell_num]
                sr = naut_sr[shell_num]
                icon_options[icon_name](d, shell_colours, stretch_ratio=sr, size_ratio=sizes[icon_name]*scaling)
            filename = f'diagonal_{icon_name}_on_{side_name}'
            filelocations = save_flag(d, filename, outdir, same_folder=True, show_image=to_show)




############################### ICON ON A DIAGONAL ROYLG BACKGROUND

for icon_name in icon_options:
    if 'ADHD' not in icon_name:
        d = draw.Drawing(h, w)
        draw_diagonal_stripes(d, ['#2cad74', '#98d570'] + ['#ffc65b']*6 + ['#f68249', '#e43546'])
        scaling = 0.9
        if 'infinity' in icon_name:
            scaling = 0.8
        if type(icon_options[icon_name]) == str:
            embed_icon(d, icon_options[icon_name], {}, size_ratio=sizes[icon_name]*scaling)
        elif 'red_infinity' in icon_name:
            pass # TODO
        else:
            shell_num = int(icon_name[-1])
            shell_colours = naut_options[shell_num]
            sr = naut_sr[shell_num]
            icon_options[icon_name](d, shell_colours, stretch_ratio=sr, size_ratio=sizes[icon_name]*scaling)
        filename = f'diagonal_{icon_name}_on_roylg'
        filelocations = save_flag(d, filename, outdir, same_folder=True, show_image=to_show)


############################## ICON IN A BELT ON HORIZONTAL STRIPES

# riffing on https://www.tumblr.com/themogaidragon/762687565710213120/hi-i-just-wanted-to-ask-if-you-would-accept-an?source=share
# and https://www.tumblr.com/themogaidragon/701717045607317504/pathological-demand-avoidance?source=share

horiz_stripe_options = {'teal':['#243444',  '#3dcec1', '#eae186', 'white',  '#eae186', '#3dcec1', '#243444'],
                        'sprite':['#282f37',  '#3dcec1', '#eae186', 'white',  '#eae186', '#3dcec1', '#282f37'],
                        'roylg':['#2cad74', '#98d570', '#ffc65b', 'white', '#ffc65b', '#f68249', '#e43546']}

for bg in horiz_stripe_options:
    for icon_name in icon_options:
        if 'ADHD' not in icon_name:
            d = draw.Drawing(h, w)
            draw_horiz_bars(d, horiz_stripe_options[bg])
            draw_circle(d, 'white', size_ratio=0.6)
            scaling = 0.4
            if icon_name == 'aufinity':
                scaling = 0.5

            if type(icon_options[icon_name]) == str:
                embed_icon(d, icon_options[icon_name], {}, size_ratio=sizes[icon_name]*scaling)
            #elif 'red_infinity' in icon_name:
            #    icon_options[icon_name](d, '#8f0103', stretch_ratio=1.5, size_ratio=sizes[icon_name] * scaling)
            else:
                icon_options[icon_name](d, spectrum_rainbow, stretch_ratio=2.25,
                                        size_ratio=sizes[icon_name]*scaling, wid=d.width/3, x_start=d.width/3)
            filename = f'horizontal_{icon_name}_on_{bg}'
            filelocations = save_flag(d, filename, outdir, same_folder=True, show_image=to_show)






for spec in naut_options:
    for bg in bg_options:

        d = draw.Drawing(h, w)
        draw_horiz_bars(d, [bg_options[bg]])
        sr = spec * 0.5
        if spec == 6:
            sr += 1.5
        draw_nautilus(d, naut_options[spec], stretch_ratio=sr, size_ratio=sizes[icon_name]*0.9) #, wid=d.width/3, x_start=d.width/3)
        filename = f'exp_nautilus_{spec}_on_{bg}'
        filelocations = save_flag(d, filename, outdir, same_folder=True, show_image=to_show)



for stripe_scheme in stripe_options:
    d = draw.Drawing(h, w)
    pun_colours = ['#4d4d4d'] * 5 + stripe_options[stripe_scheme] + ['#4d4d4d'] * 5
    draw_diagonal_stripes(d, pun_colours)
    filename = f'simple_diagonal_{stripe_scheme}_on_dark'
    filelocations = save_flag(d, filename, outdir, same_folder=True, show_image=to_show)


# Julietanboy
julietan = ['#c94948', '#da7756', '#dab558', '#6ea35d', '#2e7472', '#232728']
dimensions = {'horiz':draw_horiz_bars, 'diag':draw_diagonal_stripes}
wids = {'horiz':0.7, 'diag':0.72}
heis = {'horiz':1, 'diag':1}

schemes = {'julietan':julietan, 'roylg':roylg_colours}
which_inf = ['original', 'simple', '']

for present in which_inf:
    for sch in schemes:
        for dim in dimensions:
            d = draw.Drawing(h, w)
            dimensions[dim](d, schemes[sch])
            if present:
                if present == 'simple':
                    draw_simple_infinity(d, julietan[-1], size_ratio=0.69, stretch_ratio=0.95, thick_ratio=1.13)
                else:
                    xs = (1 - wids[dim]) / 2
                    ys = (1 - heis[dim]) / 2
                    draw_open_linear_infinity(d, julietan[-1], stretch_ratio=1.0, wid=wids[dim]*d.width, x_start=xs*d.width,
                                      hei=heis[dim]*d.height, y_start=ys*d.height)
            else:
                shell_colours = [julietan[-1]]*7
                shell_num = int(icon_name[-1])
                sr = naut_sr[shell_num]
                scaling=1.0
                draw_nautilus(d, shell_colours, stretch_ratio=sr, size_ratio=sizes[icon_name] * scaling)

            filename = f'inf_stripes_{sch}_{dim}_{present}'
            filelocations = save_flag(d, filename, outdir, same_folder=True, show_image=to_show)