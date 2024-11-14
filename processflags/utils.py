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
        if char in ['M', 'S', 'L', 'Z', 'C', 'Q', 'A']: # any others?
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


def save_flag(d, name, directory, save_png=True, save_svg=True, show_image=False):
    whether_save = {'png':save_png, 'svg':save_svg}
    saved_to = []
    for filetype in whether_save:
        if whether_save[filetype]:
            png_loc = directory + filetype + '/'
            png_name = png_loc + name + '.' + filetype
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


if __name__ == '__main__':
    #doctest.testmod()
    #s = 'M233.14606,2008.031C659.81265,2747.0389999999998,1783.8721,2105.1105,1357.2055,1366.1024C1781.7582,619.3380099999999,2919.4029,1263.3265999999999,2484.9812,2004.3931M1366.1206,76.818124C507.12735,71.109224,498.21223,1371.7897,1357.2055,1366.1024M2637.1773000000003,1366.1184C2648.5952,-351.86798,65.859465,-351.90088,77.233765,1366.0864C88.458065,3061.4318,2625.91,3061.4641,2637.1773,1366.1184Z'
    #s = 'M233.14606,2008.031C659.81265,2747.0389999999998,1783.8721,2105.1105,1357.2055,1366.1024C1781.7582,619.3380099999999,2919.4029,1263.3265999999999,2484.9812,2004.3931'
    s = 'M 1366.1206,76.818124 C 507.12735,71.109224, 498.21223,1371.7897, 1357.2055,1366.1024'
    s2 = 'M233.14606,2008.031C659.81265,2747.0389999999998,1783.8721,2105.1105,1357.2055,1366.1024C1781.7582,619.3380099999999,2919.4029,1263.3265999999999,2484.9812,2004.3931'
    #
    s = 'M379.15048,326.71772C393.68423,333.48517,407.22473,335.5506,419.25373,335.5506C472.25023,335.5506,507.58173,294.00546999999995,507.58173,266.30796999999995C507.58173,244.48746999999995,490.52973,223.03871999999996,464.42798,223.03871999999996C449.82547999999997,223.03871999999996,437.16573,229.93696999999995,429.24248,240.83646999999996C433.04748,249.01546999999997,434.87148,257.68771999999996,434.87148,266.26546999999994C434.87148,295.65646999999996,412.54698,324.05521999999996,379.15048,326.71771999999993Z'
    #parse_svg_path(s2, 0, firstx=5, firsty=5)
    parse_svg_path(s, 0)
    s2 = 'M375.98823,188.43522C375.98823,210.80997,392.97123,229.21796999999998,414.75122999999996,231.47271999999998C426.29322999999994,214.90221999999997,445.04272999999995,205.73096999999999,464.27747999999997,205.73096999999999C484.19647999999995,205.73096999999999,502.76147999999995,215.48696999999999,514.07948,231.88521999999998C509.78623,183.27846999999997,468.97273,145.16571999999996,419.25723,145.16571999999996C395.91398,145.16571999999996,375.98823,163.52821999999998,375.98823,188.43521999999996Z'
    parse_svg_path(s2, 0, 18, 18)