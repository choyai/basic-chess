from PIL import ImageColor

def get_normalized_color(hex_color):
    ''' I want to sample color from color hunt
    '''
    dec_color = ImageColor.getrgb(hex_color)

    return ( i/256 for i in dec_color )