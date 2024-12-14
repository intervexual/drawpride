import doctest
import sys
import os
sys.path.insert(0, 'drawflags/')
from embedding_icons import *
from IPython.display import Image

def get_info_for_line(line_info, headers, keyword):
    """
    Return the value associatied with a given column when parsing a row of the csv input.
    :param headers: dictionary of csv headers
    :param line_info: partially parsed line of csv
    :param keyword: name of the column
    :return: the value within row specified by line_info that is at column of keyword
    >>> h =  {'hex': 0, 'association': 1, 'aka': 2, 'Hue-init': 3, 'Subhue-init': 4, 'Light-init': 5, 'sat': 6, 'Note': 7, 'meaning1': 8, 'meaning2': 9, 'block': 10, 'categ': 11, 'intersex?': 12, 'order': 13, 'place': 14, 'orient': 15, 'relsize': 16, 'satnote': 17, 'R': 18, 'G': 19, 'B': 20, 'okL': 21, 'okC': 22, 'okH': 23, 'hasmean?': 24, 'gender': 25, 'expression': 26, 'sex': 27, 'abstract': 28, 'attraction': 29, 'colour?': 30, '': 31, 'lchL': 32, 'lchC': 33, 'lchH': 34, 'hsvH': 35, 'hsvS': 36, 'hsvV': 37, 'labL': 38, 'labA': 39, 'labB': 40, 'oklabL': 41, 'oklabA': 42, 'oklabB': 43}
    >>> ln = ['#fef4f5', 'indigiqueer', '', 'white', '', '', '', '', '', '', '', 'gender', 'False', '6', 'icon', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '']
    >>> get_info_for_line(ln, h, 'hex')
    '#fef4f5'
    >>> get_info_for_line(ln, h, 'association')
    'indigiqueer'
    """
    assert keyword in headers, keyword + str(line_info) + str(headers)
    index = headers[keyword]
    return line_info[index]

def get_info_for_columns(line_info, headers, keywords):
    """
    Return the values associatied with given columns when parsing a row of the csv input.
    :param headers: dictionary of csv headers
    :param line_info: partially parsed line of csv
    :param keyword: name of the columns in question
    :return: the value within row specified by line_info that is at column of keyword
    >>> h =  {'hex': 0, 'association': 1, 'aka': 2, 'Hue-init': 3, 'Subhue-init': 4, 'Light-init': 5, 'sat': 6, 'Note': 7, 'meaning1': 8, 'meaning2': 9, 'block': 10, 'categ': 11, 'intersex?': 12, 'order': 13, 'place': 14, 'orient': 15, 'relsize': 16, 'satnote': 17, 'R': 18, 'G': 19, 'B': 20, 'okL': 21, 'okC': 22, 'okH': 23, 'hasmean?': 24, 'gender': 25, 'expression': 26, 'sex': 27, 'abstract': 28, 'attraction': 29, 'colour?': 30, '': 31, 'lchL': 32, 'lchC': 33, 'lchH': 34, 'hsvH': 35, 'hsvS': 36, 'hsvV': 37, 'labL': 38, 'labA': 39, 'labB': 40, 'oklabL': 41, 'oklabA': 42, 'oklabB': 43}
    >>> ln = ['#fef4f5', 'indigiqueer', '', 'white', '', '', '', '', '', '', '', 'gender', 'False', '6', 'icon', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '']
    >>> get_info_for_columns(ln, h, ['hex', 'association', 'aka'])
    {'hex': '#fef4f5', 'association': 'indigiqueer', 'aka': ''}
    >>> get_info_for_columns(ln, h, LOCATORS)
    {'order': '6', 'place': 'icon', 'relsize': '', 'orient': ''}
    """
    results = {}
    for keyword in keywords:
        results[keyword] = get_info_for_line(line_info, headers, keyword)
    return results


def get_info_by_column(line_info, headers, keywords):
    """
    Wrapper for get_info_for_columns and get_info_for_column
    :param line_info:
    :param headers:
    :param keywords:
    :return:
    """
    if type(keywords) == str:
        return get_info_for_line(line_info, headers, keywords)
    return get_info_for_columns(line_info, headers, keywords)


def get_headers(f, DELIM='\t'):
    """
    Read the first (next/current) line of f into a dictionary of headers
    :param f: file object (already opened)
    :param line:
    :param DELIM:
    :return:
    """
    csv_headers = {}
    raw_headers = f.readline().strip().split(DELIM)
    for i, h in enumerate(raw_headers):
        csv_headers[h] = i
    return csv_headers


def separate_svg_path(s):
    """
    Take a string representing an SVG path and turn it into a new string that
    represents the path in drawsvg.
    :param s: a path string. Must be all absolute.
    :return:
    >>> s = 'M233.14606,2008.031C659.81265,2747.0389999999998,1783.8721,2105.1105,1357.2055,1366.1024C1781.7582,619.3380099999999,2919.4029,1263.3265999999999,2484.9812,2004.3931M1366.1206,76.818124C507.12735,71.109224,498.21223,1371.7897,1357.2055,1366.1024M2637.1773000000003,1366.1184C2648.5952,-351.86798,65.859465,-351.90088,77.233765,1366.0864C88.458065,3061.4318,2625.91,3061.4641,2637.1773,1366.1184Z'
    >>> separate_svg_path(s)
    ['M233.14606,2008.031', 'C659.81265,2747.0389999999998,1783.8721,2105.1105,1357.2055,1366.1024', 'C1781.7582,619.3380099999999,2919.4029,1263.3265999999999,2484.9812,2004.3931', 'M1366.1206,76.818124', 'C507.12735,71.109224,498.21223,1371.7897,1357.2055,1366.1024', 'M2637.1773000000003,1366.1184', 'C2648.5952,-351.86798,65.859465,-351.90088,77.233765,1366.0864', 'C88.458065,3061.4318,2625.91,3061.4641,2637.1773,1366.1184', 'Z']
    >>> s = 'M 1366.1206,76.818124 C 507.12735,71.109224 498.21223,1371.7897 1357.2055,1366.1024'
    >>> separate_svg_path(s)
    ['M1366.1206,76.818124', 'C507.12735,71.109224498.21223,1371.78971357.2055,1366.1024']
    """
    s = s.replace(' ','')
    sections = []
    curr_section = ''
    for char in s:
        if char in ['M', 'S', 'L', 'Z', 'C', 'Q', 'A', 'H']: # any others?
            sections.append(curr_section)
            curr_section = ''
        curr_section += char
    sections.append(curr_section)
    return sections[1:]

def parse_svg_path(s, rounding_precision=3, firstx=0, firsty=0):
    """
    Take a string representing an SVG path and turn it into a new string that
    represents the path in drawsvg.
    :param s: a path string. Must be all absolute.
    :return:
    >>> s = 'M233.14606,2008.031C659.81265,2747.0389999999998,1783.8721,2105.1105,1357.2055,1366.1024C1781.7582,619.3380099999999,2919.4029,1263.3265999999999,2484.9812,2004.3931M1366.1206,76.818124C507.12735,71.109224,498.21223,1371.7897,1357.2055,1366.1024M2637.1773000000003,1366.1184C2648.5952,-351.86798,65.859465,-351.90088,77.233765,1366.0864C88.458065,3061.4318,2625.91,3061.4641,2637.1773,1366.1184Z'
    >>> parse_svg_path(s, rounding_precision=-2)
    #x coordinates
    x1 = x_start + 200.0*w
    x2 = x_start + 700.0*w
    x3 = x_start + 1800.0*w
    x4 = x_start + 1400.0*w
    x6 = x_start + 2900.0*w
    x7 = x_start + 2500.0*w
    x9 = x_start + 500.0*w
    x12 = x_start + 2600.0*w
    x14 = x_start + 100.0*w
    #y coordinates
    y1 = y_start + 2000.0*h
    y2 = y_start + 2700.0*h
    y3 = y_start + 2100.0*h
    y4 = y_start + 1400.0*h
    y5 = y_start + 600.0*h
    y6 = y_start + 1300.0*h
    y8 = y_start + 100.0*h
    y13 = y_start + -400.0*h
    y16 = y_start + 3100.0*h
    <BLANKLINE>
    p.M(x1, y1)
    p.C(x2, y2, x3, y3, x4, y4)
    p.C(x3, y5, x6, y6, x7, y1)
    p.M(x4, y8)
    p.C(x9, y8, x9, y4, x4, y4)
    p.M(x12, y4)
    p.C(x12, y13, x14, y13, x14, y4)
    p.C(x14, y16, x12, y16, x12, y4)
    p.Z()
    """
    s = s.replace(' ','')
    sections = separate_svg_path(s)
    varstart = {0:'x', 1:'y'}
    vars_seen = {'x':firstx, 'y':firsty}
    varnames = {'x':{}, 'y':{}}

    commands = []
    for cm in sections:
        cmd = cm[0]
        nums = cm[1:].split(',')
        vars = []
        if cmd not in ['Z']:
            for i, num in enumerate(nums):
                axis = varstart[i%2]
                vars_seen[axis] += 1

                numval = round(float(num), rounding_precision)
                if numval not in varnames[axis]:
                    varnames[axis][numval] = axis + str(vars_seen[axis])
                varname = varnames[axis][numval]
                vars.append(varname)


                #print(i, num, axis, varname)
        varlist = ', '.join(vars)
        commands.append(f'p.{cmd}({varlist})')


    #assert vars_seen['x'] == vars_seen['y']

    axisalters = {'x':'w', 'y':'h'}
    for axis in varnames: # print variable assignments
        print(f'#{axis} coordinates')
        for num in varnames[axis]:
            print(f'{varnames[axis][num]} = {axis}_start + {num}*{axisalters[axis]}')
    print()
    for cmd in commands:
        print(cmd)
    print('d.append(p)')

def save_flag(d, name, directory='output/', save_png=True, save_svg=True, show_image=False, suffix=''):
    assert directory.endswith('/')
    whether_save = {'png':save_png, 'svg':save_svg}
    saved_to = []
    for filetype in whether_save:
        if whether_save[filetype]:
            png_loc = directory + filetype + '/'
            png_name = png_loc + name + suffix + '.' + filetype
            if not os.path.exists(png_loc):
                os.makedirs(png_loc)
            if filetype == 'png':
                d.save_png(png_name)
                saved_to.append(png_name)
            else:
                d.save_svg(png_name)
                saved_to.append(png_name)

    if show_image:
        display(Image(filename=saved_to[0]))
    return saved_to


def round_percent_to_nearest_five_unless_90s(n):
    """
    Round n to the nearest 5, unless n is above 90.
    Then round to the nearest even number.
    Never round to 100 unless n is already 100.
    :param n: number
    :return: rounded integer
    >>> round_percent_to_nearest_five_unless_90s(32)
    30
    >>> round_percent_to_nearest_five_unless_90s(90.5)
    90
    >>> round_percent_to_nearest_five_unless_90s(91.5)
    92
    >>> round_percent_to_nearest_five_unless_90s(99.9)
    98
    >>> round_percent_to_nearest_five_unless_90s(97.6)
    98
    >>> round_percent_to_nearest_five_unless_90s(100)
    100
    >>> round_percent_to_nearest_five_unless_90s(105)
    100
    """
    if n < 90:
        return round_to_nearest_five(n)
    if n >= 100:
        return 100
    r = round_to_nearest_even_number(n)
    if r == 100:
        return 98
    return r

def round_to_nearest_five(n):
    """
    Round n to the nearest 5
    :param n: number
    :return: rounded integer to nearest 5
    >>> round_to_nearest_five(323)
    325
    >>> round_to_nearest_five(46.2)
    45
    >>> round_to_nearest_five(-10.5983)
    -10
    >>> round_to_nearest_five(0)
    0
    """
    return round(n/5)*5


def round_to_nearest_even_number(n):
    """
    Round n to the nearest even integer
    :param n: number to round
    :return: integer rounded to nearest even
    >>> round_to_nearest_even_number(23.1)
    24
    >>> round_to_nearest_even_number(24)
    24
    >>> round_to_nearest_even_number(24.9)
    24
    >>> round_to_nearest_even_number(-0.34)
    0
    >>> round_to_nearest_even_number(-3.6)
    -4
    >>> round_to_nearest_even_number(333)
    332
    """
    return round(n/2)*2




if __name__ == '__main__':
    doctest.testmod()
    #s = 'M233.14606,2008.031C659.81265,2747.0389999999998,1783.8721,2105.1105,1357.2055,1366.1024C1781.7582,619.3380099999999,2919.4029,1263.3265999999999,2484.9812,2004.3931M1366.1206,76.818124C507.12735,71.109224,498.21223,1371.7897,1357.2055,1366.1024M2637.1773000000003,1366.1184C2648.5952,-351.86798,65.859465,-351.90088,77.233765,1366.0864C88.458065,3061.4318,2625.91,3061.4641,2637.1773,1366.1184Z'
    #s = 'M233.14606,2008.031C659.81265,2747.0389999999998,1783.8721,2105.1105,1357.2055,1366.1024C1781.7582,619.3380099999999,2919.4029,1263.3265999999999,2484.9812,2004.3931'
    s = 'M 1366.1206,76.818124 C 507.12735,71.109224, 498.21223,1371.7897, 1357.2055,1366.1024'
    s2 = 'M233.14606,2008.031C659.81265,2747.0389999999998,1783.8721,2105.1105,1357.2055,1366.1024C1781.7582,619.3380099999999,2919.4029,1263.3265999999999,2484.9812,2004.3931'
    #
    s = 'M379.15048,326.71772C393.68423,333.48517,407.22473,335.5506,419.25373,335.5506C472.25023,335.5506,507.58173,294.00546999999995,507.58173,266.30796999999995C507.58173,244.48746999999995,490.52973,223.03871999999996,464.42798,223.03871999999996C449.82547999999997,223.03871999999996,437.16573,229.93696999999995,429.24248,240.83646999999996C433.04748,249.01546999999997,434.87148,257.68771999999996,434.87148,266.26546999999994C434.87148,295.65646999999996,412.54698,324.05521999999996,379.15048,326.71771999999993Z'
    #parse_svg_path(s2, 0, firstx=5, firsty=5)
    #parse_svg_path(s, 0)
    s2 = 'M375.98823,188.43522C375.98823,210.80997,392.97123,229.21796999999998,414.75122999999996,231.47271999999998C426.29322999999994,214.90221999999997,445.04272999999995,205.73096999999999,464.27747999999997,205.73096999999999C484.19647999999995,205.73096999999999,502.76147999999995,215.48696999999999,514.07948,231.88521999999998C509.78623,183.27846999999997,468.97273,145.16571999999996,419.25723,145.16571999999996C395.91398,145.16571999999996,375.98823,163.52821999999998,375.98823,188.43521999999996Z'
    #parse_svg_path(s2, 0, 18, 18)
    s = 'M196.46,232.73L128.18,191.22L60.07300000000001,233.01L78.45400000000001,155.24L17.66100000000001,103.38000000000001L97.30000000000001,96.83500000000001L127.84,22.991000000000014L158.678,96.70800000000001L238.34300000000002,102.93030000000002L177.76300000000003,155.03930000000003Z'
    s = 'M163.20014,98.298651L162.06588,99.373124L162.34792,100.91458L160.975,100.16554000000001L159.60208,100.91458L159.88412,99.373124L158.74985,98.298651L160.30216000000001,98.09227600000001L160.97500000000002,96.68125300000001L161.64783000000003,98.09227600000001Z'
    #parse_svg_path(s)
    s = 'M142.74646,113.87472C142.67576000000003,113.69057,142.61798000000002,112.94954,142.61798000000002,112.22798C142.61798000000002,100.0677,136.35897000000003,83.716184,117.64081000000002,46.975684C114.96350000000001,41.720604,112.77299000000002,37.362914,112.77299000000002,37.291934C112.77299000000002,37.220934,120.73131000000002,37.162864,130.45815000000002,37.162864H148.14333000000002L155.30282000000003,51.609114C172.96919000000003,87.25591399999999,177.75215000000003,100.28757999999999,177.75440000000003,112.78078L177.75465000000003,114.20952999999999H160.3148C144.60719,114.20952999999999,142.86218,114.17622999999999,142.74645999999998,113.87471999999998Z'
    #parse_svg_path(s, 0)