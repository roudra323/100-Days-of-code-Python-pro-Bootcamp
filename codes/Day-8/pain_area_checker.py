from math import ceil


def print_can(height, width, cover):
    """print area

    Args:
        height (float): [description]
        width (float): [description]
        cover (float): [description]
    """
    can = ceil((height*width)/cover)
    return print(can)


print_can(2, 4, 5)
