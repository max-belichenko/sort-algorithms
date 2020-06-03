"""
You can use this module to print arrays and specified parts of arrays.
Also you can highlight some elements with different colors.

Module used to print arrays into console.
"""
import random


# Constant to store ANSI codes those change text color in console.
COLORS = {
    'black': '\033[30m',
    'red': '\033[31m',
    'green': '\033[32m',
    'yellow': '\033[33m',
    'blue': '\033[34m',
    'purple': '\033[35m',
    'cyan': '\033[36m',
    'white': '\033[37m',
}

# Constant to store ANSI codes those change text decoration in console.
FONTS = {
    'reset': '\033[0m',
    'bold': '\033[1m',
    'faded': '\033[2m',
    'italics': '\033[3m',
    'underlined': '\033[4m',
    'rare flash': '\033[5m',
    'frequent flash': '\033[6m',
    'invert': '\033[7m',
    'not implemented': ''
}


def color_text(text, color='white', font='not implemented'):
    """
    Receive text string.
    Return decorated text string with given color code (see COLOR constant) and font code (see FONT constant).
    :param text:
    :param color:
    :param font:
    :return: unicode string
    """
    return f"{FONTS[font]}{COLORS[color]}{text}{FONTS['reset']}"


def print_array(array, text='', start_idx=None, end_idx=None, idx_red=-1, idx_green=-1, idx_blue=-1):
    """
    Prints array to the console.

    Output format:
                   text : [array[0]][array[1]]..[array[len-1]]

    If start_idx and/or end_ix are given, print array in specified indexes.
    Elements that are not in index borders will be printed as empty: [  ]

    If idx_red, idx_green and/or idx_blue are given, these elements will be highlighted into specified colors.

    :param array: Any iterable and printable array of values.
    :param text: Precede array output with some text.
    :param start_idx: Before start_idx all elements will be printed as an empty [  ]
    :param end_idx: After end_idx all elements will be printed as an empty [  ]
    :param idx_red: This element will be highlighted into red color
    :param idx_green: This element will be highlighted into green color
    :param idx_blue: This element will be highlighted into blue color
    :return:
    """
    array_string = ''

    if start_idx is None:
        start_idx = 0
    if end_idx is None:
        end_idx = len(array) - 1

    for i in range(len(array)):
        if start_idx <= i <= end_idx:
            if 0 <= idx_red == i:
                array_string += '[{:>2}]'.format(color_text(str(array[i]), color='red', font='bold'))
            elif 0 <= idx_green == i:
                array_string += '[{:>2}]'.format(color_text(str(array[i]), color='green', font='bold'))
            elif 0 <= idx_blue == i:
                array_string += '[{:>2}]'.format(color_text(str(array[i]), color='blue', font='bold'))
            else:
                array_string += '[{:>2}]'.format(array[i])
        else:
            array_string += '[   ]'

    print('{:>30} : {}'.format(text, array_string))


def generate_array(array_size, is_unique=True, is_sorted=False):
    if is_unique:
        array = [x for x in range(array_size)]
        if not is_sorted:
            random.shuffle(array)
    else:
        array = [random.randint(0, 100) for _ in range(array_size)]
        if is_sorted:
            array.sort()
    return array