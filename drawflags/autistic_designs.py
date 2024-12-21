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

##
# Making a flag inspired by the Autistic Pride Day (Australia) logo
d = draw.Drawing(500*2, 300*2)
draw_horiz_bars(d, ['white'])
draw_concentric_infinities(d, ['#2cad74', 'white', '#ffc65b', 'white', '#e43546'], 'white', size_ratio=0.7)
filelocations = save_flag(d, 'autistic_concentric', outdir, same_folder=True, show_image=to_show)

d = draw.Drawing(500*2, 300*2)
draw_horiz_bars(d, [disability_grey])
draw_concentric_infinities(d, disability_stripes, disability_grey, size_ratio=0.7)
filelocations = save_flag(d, 'autistic_codisabled', outdir, same_folder=True, show_image=to_show)

# codisabled but specifically mad
d = draw.Drawing(500*2, 300*2)
draw_horiz_bars(d, [disability_grey])
draw_concentric_infinities(d, ['#796098', '#bf7998', '#796098', '#bf7998'], disability_grey, size_ratio=0.7)
filelocations = save_flag(d, 'mad_autistic', outdir,  same_folder=True, show_image=to_show)

# rainbow on white
d = draw.Drawing(500*2, 300*2)
draw_horiz_bars(d, ['#f7f7f7'])
draw_concentric_infinities(d, rainbow_stripes, '#f7f7f7', size_ratio=0.7)
filelocations = save_flag(d, 'autistic_queer', outdir, same_folder=True, show_image=to_show)

# trans on white
d = draw.Drawing(500*2, 300*2)
draw_horiz_bars(d, ['#f7f7f7'])
draw_concentric_infinities(d, trans_stripes, '#f7f7f7', size_ratio=0.7)
filelocations = save_flag(d, 'autistic_queer', outdir, same_folder=True, show_image=to_show)

# autism as disability
d = draw.Drawing(500*2, 300*2)
draw_horiz_bars(d, ['#f7f7f7'])
draw_concentric_infinities(d, [disability_grey] + disability_stripes + [disability_grey], '#f7f7f7', size_ratio=0.7)
filelocations = save_flag(d, 'autistic_as_disability', outdir, same_folder=True, show_image=to_show)

# ROYLG on grey
d = draw.Drawing(500*2, 300*2)
draw_horiz_bars(d, [disability_grey])
draw_concentric_infinities(d, ['#2cad74', '#98d570', '#ffc65b',  '#f68249', '#e43546'], disability_grey, size_ratio=0.7)
filelocations = save_flag(d, 'autistic_hybrid', outdir, same_folder=True, show_image=to_show)

#draw_concentric_infinities(d, [disability_grey, '#243444',  '#3dcec1', '#eae186', 'white',  '#eae186', '#3dcec1', '#243444'], size_ratio=0.7)
#filelocations = save_flag(d, 'autistic_teal', outdir, same_folder=True, show_image=to_show)

# ND on ROYLG diagonal
d = draw.Drawing(500*2, 300*2)
draw_horiz_bars(d, ['#f7f7f7'])
draw_diagonal_stripes(d, ['#2cad74', '#98d570'] + ['#ffc65b']*6 + ['#f68249', '#e43546'])
embed_icon(d, 'disability/neurodiversity.svg', {})
filelocations = save_flag(d, 'autistic_ryg_rainb_diag', outdir, same_folder=True, show_image=to_show)

# riffing on https://www.tumblr.com/themogaidragon/762687565710213120/hi-i-just-wanted-to-ask-if-you-would-accept-an?source=share
# and https://www.tumblr.com/themogaidragon/701717045607317504/pathological-demand-avoidance?source=share
d = draw.Drawing(500*2, 300*2)
draw_horiz_bars(d, ['#2cad74', '#98d570', '#ffc65b', 'white', '#ffc65b', '#f68249', '#e43546'])
draw_circle(d, 'white', size_ratio=0.6)
embed_icon(d, 'disability/aufinity2.png', {}, size_ratio=0.5)
filelocations = save_flag(d, 'autistic_ryg_belt_aufinity', outdir, same_folder=True, show_image=to_show)


# riffing on https://www.tumblr.com/themogaidragon/762687565710213120/hi-i-just-wanted-to-ask-if-you-would-accept-an?source=share
# and https://www.tumblr.com/themogaidragon/701717045607317504/pathological-demand-avoidance?source=share
d = draw.Drawing(500*2, 300*2)
draw_horiz_bars(d, ['#2cad74', '#98d570', '#ffc65b', 'white', '#ffc65b', '#f68249', '#e43546'])
draw_circle(d, 'white', size_ratio=0.6)
embed_icon(d, 'disability/aufinity2.png', {}, size_ratio=0.5)
filelocations = save_flag(d, 'autistic_ryg_belt_aufinity', outdir, same_folder=True, show_image=to_show)

# simple aufinity flag
d = draw.Drawing(500*2, 300*2)
draw_horiz_bars(d, ['#fbfbfb'])
embed_icon(d, 'disability/aufinity2.png', {}, size_ratio=1)
filelocations = save_flag(d, 'autistic_aufinity', outdir, same_folder=True, show_image=to_show)

# simple gold loop thanks to ryanyflags
d = draw.Drawing(500*2, 300*2)
draw_horiz_bars(d, ['#fbfbfb'])
embed_icon(d, 'disability/gold_infinity.svg', {}, size_ratio=1.2)
filelocations = save_flag(d, 'autistic_gold', outdir, same_folder=True, show_image=to_show)

# simple autism spectrum nautilus flag
d = draw.Drawing(500*2, 300*2)
draw_horiz_bars(d, ['#f7f7f7'])
spectrum_rainbow = ['#cf7280', '#dfa87c', '#eede77', '#95c77a', '#3bb07d', '#5bb9af', '#7bc2e0', '#97a7c0', '#b38da0']
draw_nautilus(d, spectrum_rainbow, orientation=HORIZONTAL, size_ratio=1.25, stretch_ratio=2.25)
filelocations = save_flag(d, 'autistic_nautilus', outdir, same_folder=True, show_image=to_show)



