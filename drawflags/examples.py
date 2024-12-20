"""
Examples of how to use the code in this directory.
"""
from pride_shapes import *

# some useful colours
intersex_yellow = '#FDD70A'
intersex_purple = '#7A01AA'
trans_pink = '#F5A9B8'
trans_blue = '#5BCEFA'
trans_stripes = [trans_pink, trans_blue, 'white', trans_blue, trans_pink]
disability_stripes = ['#CF7280', '#EEDE77', '#E8E8E8', '#7BC2E0', '#3CB07D']
disability_grey = '#595959'
rainbow_stripes = ['#E40303', '#FF8C00', '#FFED00', '#008026', '#24408E', '#732982']

if __name__ == '__main__':
    outdir = 'output/examples/'

    # example of vertical bars: the androgyne flag
    d = draw.Drawing(500, 300)
    draw_vert_bars(d, ['#FE007F', '#9832FF', '#00B8E7'])
    d.save_svg(outdir + 'androgyne.svg')

    # example of horizontal bars AND a pile: the demisexual flag
    d = draw.Drawing(500, 300)
    draw_horiz_bars(d, ['white', 'white', '#6e0170', '#d2d2d2', '#d2d2d2'])
    draw_pile(d, 'black', size_ratio=1.1)
    d.save_svg(outdir + 'demisexual.svg')

    # example of diagonal stripes: the disability pride flag
    d = draw.Drawing(500, 300)
    draw_diagonal_stripes(d, [disability_grey]*5 + disability_stripes + [disability_grey]*5)
    d.save_svg(outdir + 'disability.svg')

    # example of a ring flag: the intersex flag
    d = draw.Drawing(500, 300)
    draw_horiz_bars(d, [intersex_yellow])
    draw_transparent_ring(d, intersex_purple)
    d.save_svg(outdir + 'intersex.svg')

    # example of a segmented ring flag: the allodisabled-intersex flag (intersex with unrelated disability)
    d = draw.Drawing(500, 300)
    draw_horiz_bars(d, [intersex_yellow])
    draw_segmented_ring(d, disability_stripes[::-1], border_fill=disability_grey)
    d.save_svg(outdir + 'allodisabledintersex.svg')

    # example of a concentric ring flag: the codisabled-intersex flag (intersex with a frequently correlated disability)
    d = draw.Drawing(500, 300)
    draw_horiz_bars(d, [disability_grey])
    draw_concentric_rings(d, disability_stripes[::-1])
    d.save_svg(outdir + 'codisabledintersex.svg')

    # example of how you can combine a ring and a cross to get the ipsogender flag
    d = draw.Drawing(500, 300)
    draw_horiz_bars(d, [intersex_purple])
    draw_cross(d, intersex_yellow)
    draw_transparent_ring(d, intersex_yellow)
    d.save_svg(outdir + 'ipsogender.svg')

    # example of an inset flag: intersex and transgender flag
    d = draw.Drawing(500, 300)
    draw_inset_into_intersex(d, trans_stripes, intersex_yellow, intersex_purple, orientation=HORIZONTAL)
    d.save_png(outdir + 'intersextrans.png')
    d.save_svg(outdir + 'intersextrans.svg')

    # example of chevrons: queer intersex flag
    d = draw.Drawing(500, 300)
    draw_horiz_bars(d, [intersex_yellow])
    draw_chevrons(d, [intersex_purple, '#fcf5ec', intersex_purple])
    d.save_svg(outdir + 'queerintersex.svg')

    # trichevron pattern used in the queer chevron flag (shortcut to simplify calls to draw_chevrons)
    d = draw.Drawing(500, 300)
    draw_horiz_bars(d, ['#fcf5ec'])
    draw_trichevron(d, ['#bb7fc7', '#68436a'])
    d.save_svg(outdir + 'queer.svg')

    # example of vees: the varsex flag
    d = draw.Drawing(500, 300)
    draw_horiz_bars(d, ['black'])
    draw_vees(d, [intersex_purple, trans_blue, trans_pink, intersex_yellow, 'white', 'white'])
    d.save_svg(outdir + 'varsex.svg')

    # vees with unequal sizes: libidoist flag
    d = draw.Drawing(500, 300)
    draw_horiz_bars(d, ['#87232F'])
    draw_vees(d, ['#F58187'] + ['#CD101A']*3)
    d.save_svg(outdir + 'libidoist.svg')

    # example of reverse diagonal plus square plus diagonal-cut square: the endosex flag
    d = draw.Drawing(500, 300)
    draw_reverse_diagonal_stripes(d, ['#626eb7', '#c7d6ff'])
    draw_square(d, 'black')
    draw_diagonal_cut_square(d, 'white')
    d.save_png(outdir + 'endosex.png')
    d.save_svg(outdir + 'endosex.svg')

    # example of perisex symbol: the perisex flag
    d = draw.Drawing(500, 300)
    draw_horiz_bars(d, ['#626eb7'])
    draw_perisex(d, 'white')
    d.save_svg(outdir + 'perisex.svg')

    # example of altersex symbol: the altersex flag
    d = draw.Drawing(500, 300)
    draw_horiz_bars(d, ['#78e2bc', '#7da4e9', '#ffFFff', '#a269d4', '#e1899f'])
    draw_altersex_symbol(d, 'black', 'white')
    d.save_svg(outdir + 'altersex.svg')

    # example of text on a flag: the original polyamory flag
    d = draw.Drawing(500, 300)
    draw_horiz_bars(d, ['#0000FF', '#FF0000', 'black'])
    draw_text(d,  'π', '#FFFF00')
    d.save_svg(outdir + 'polyamory.svg')

    # example of concentric beziers: the mental health flag
    d = draw.Drawing(500, 300)
    draw_concentric_beziers(d, ['#1d351d', '#3c7737', '#5eb039', '#efd428'])
    d.save_svg(outdir + 'mentalhealth.svg')

    # example of a flag with a Métis lemniscate: the queer Métis flag
    d = draw.Drawing(500, 300)
    draw_horiz_bars(d, rainbow_stripes)
    draw_metis_lemniscate(d, 'white')
    d.save_svg(outdir + 'queermetis.svg')

    # example of how to add a border to a lemniscate: the intersex Métis flag
    d = draw.Drawing(500, 300)
    draw_horiz_bars(d, [intersex_yellow])
    draw_metis_lemniscate(d, intersex_purple, size_ratio=1.7)
    draw_metis_lemniscate(d, 'white', size_ratio=0.7)
    d.save_svg(outdir + 'metisintersex.svg')

    # example of concentric infinities: Autistic Pride Day flag
    d = draw.Drawing(500*3, 300*3)
    draw_horiz_bars(d, ['white'])
    draw_concentric_infinities(d, ['#2cad74', 'white', '#ffc65b', 'white', '#e43546'], 'white', size_ratio=0.7)
    d.save_svg(outdir + 'autisticprideday.svg')

    # example of nautilus symbol: Autism Spectrum pride flag
    d = draw.Drawing(500, 300)
    draw_diagonal_stripes(d,  disability_stripes + [disability_grey]*14 + disability_stripes)
    nautilus_colours = ['#cf7280', '#DFA87C', '#eede77', '#95C77A', '#3bb07d', '#5BB9AF', '#7bc2e0', '#97A7C0', '#B38DA0']
    draw_nautilus(d, nautilus_colours, border_colour=disability_grey)
    d.save_svg(outdir + 'autismspectrum.svg')

    # inner triangles: Bissu flag
    d = draw.Drawing(500, 300)
    draw_horiz_bars(d, ['#e01507'])
    draw_bissu(d, '#ffbd24', 'white')
    d.save_svg(outdir + 'bissu.svg')

    # closeted intersex flag
    d = draw.Drawing(500, 300)
    draw_reverse_diagonal_stripes(d, ['#626eb7', '#c7d6ff'])
    radius = draw_square(d, 'black', intersex_yellow)
    draw_diagonal_cut_square(d, 'white')
    draw_closet_symbol(d, intersex_purple, size_ratio=.4)
    d.save_svg(outdir + 'closetedintersex.svg')

    # tgirl flag
    d = draw.Drawing(500, 300)
    draw_concentric_tees(d, ['#f061b4', '#ffa1c9', '#ffd4db'])
    d.save_svg(outdir + 'tgirl.svg')

    # the refugee flag (intersex version)
    d = draw.Drawing(500, 300)
    draw_horiz_bars(d, ['#f06942'])
    linetop = draw_refugeeline(d, 'black')
    draw_transparent_ring(d, intersex_purple, hei=linetop)
    d.save_svg(outdir + 'intersex_refugee.svg')

    # ally flag: perisex allies of intersex people
    d = draw.Drawing(500, 300)
    draw_horiz_bars(d, ['black', 'white']*3)
    r = draw_intersex_ally(d, intersex_yellow, intersex_purple)
    d.save_svg(outdir + 'perisex_ally.svg')

    # ally flag with stripes: trans ally
    d = draw.Drawing(500, 300)
    draw_horiz_bars(d, (['black', 'white']*3)[:-1])
    r = draw_ally_stripes(d, trans_stripes)
    d.save_svg(outdir + 'cisgender_ally.svg')

    # heart in centre: queerplatonic
    d = draw.Drawing(500, 300)
    bh = draw_horiz_bars(d, ['#F89FC9', '#2E2826', '#7E7E7E', 'white', '#7E7E7E', '#2E2826', '#F89FC9'])
    draw_heart(d, '#FEE900', size_ratio=0.7)
    d.save_svg(outdir + 'queerplatonic.svg')

    # heart in corner: biromantic
    d = draw.Drawing(500, 300)
    bh = draw_horiz_bars(d, ['#D60270', '#D60270', '#9B4F96', '#0038A8', '#0038A8'])
    draw_heart(d, '#ccCCcc', hei=d.height/2, wid=d.height*.6)
    d.save_svg(outdir + 'biromantic.svg')

    # rotated heart: leather flag
    d = draw.Drawing(500, 300)
    bh = draw_horiz_bars(d, ['black', '#2A2A7F', 'black', '#2A2A7F', 'white', '#2A2A7F', 'black', '#2A2A7F', 'black'])
    draw_heart(d, '#E70039', wid=bh*4, hei=bh*4, x_start=bh/2, y_start=bh/4, orientation=DIAGONAL)
    d.save_svg(outdir + 'leather.svg')

    # rubber pride
    d = draw.Drawing(500, 300)
    bh = draw_horiz_bars(d, ['black'])
    draw_rubber_zigzags(d, '#ba1b10', '#fcc900', y_start=500)
    d.save_svg(outdir + 'rubber.svg')

    # triskelion example: bdsm emblem flag
    d = draw.Drawing(500, 300)
    bh = draw_horiz_bars(d, ['#ab0024', 'black', '#ab0024'])
    draw_triskelion(d, ['black'], size_ratio=1.05) # to create the black border
    draw_triskelion(d, ['white', 'black', '#ab0024'])
    d.save_svg(outdir + 'bdsm_emblem.svg')

    # triangle example: pink triangle flag
    d = draw.Drawing(500, 300)
    bh = draw_horiz_bars(d, ['black'])
    draw_inverted_triangle(d, '#ff66cc')
    d.save_svg(outdir + 'pink_triangle.svg')

    # pocket gender flag
    d = draw.Drawing(500, 300)
    bh = draw_vert_bars(d, ['#FFB1CB', '#01A6EA'])
    draw_pocketgender_hourglass(d, ['black', '#FFCC10', '#A649A4', 'black'])
    d.save_svg(outdir + 'pocketgender.svg')

    # example of concentric ellipses - not an actual flag, just for fun
    d = draw.Drawing(500, 300)
    draw_horiz_bars(d, [disability_grey])
    draw_concentric_ellipses(d, disability_stripes)
    d.save_svg(outdir + 'funconcentricdisability.svg')

    # example of concentric rectangles - not an actual flag, just for fun
    d = draw.Drawing(500, 300)
    draw_concentric_rectangles(d, trans_stripes)
    d.save_svg(outdir + 'funconcentrictrans.svg')

    # example of Seychelles lines - not an actual flag, just for fun
    d = draw.Drawing(500, 300)
    draw_seychelles(d, trans_stripes)
    d.save_svg(outdir + 'funseychellestrans.svg')

    # example of starburst pattern  - not an actual flag, just for fun
    d = draw.Drawing(500, 300)
    draw_starburst(d, disability_stripes)
    d.save_svg(outdir + 'fundisabilitystarburst.svg')

