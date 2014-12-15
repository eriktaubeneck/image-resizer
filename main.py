import os
import sys
from PIL import Image


def crop_coordinates(insize, outsize):
    in_x, in_y = insize
    out_x, out_y = outsize
    in_ratio = in_x/float(in_y)
    out_ratio = out_x/float(out_y)
    if in_ratio < out_ratio:
        diff = in_y - (in_x / out_ratio)
        return (0, int(round(diff/2.0)),
                in_x, int(round(in_y - diff/2.0)))
    elif in_ratio > out_ratio:
        diff = in_x - (in_y * out_ratio)
        return (int(round(diff/2.0)), 0,
                int(round(in_x - diff/2.0)), in_y)
    else:
        return (0, 0, in_x, in_y)


def img_resize(infile, outfile, size=(120, 120), quality=60):
    im = Image.open(infile)
    im_format = im.format
    im = im.crop(crop_coordinates(im.size, size))
    im = im.resize(size, Image.ANTIALIAS)
    im.save(outfile, im_format, quality=quality)
    return outfile


if __name__ == '__main__':
    if len(sys.argv[1:]) >= 1:
        full_filename = sys.argv[1]
    if len(sys.argv[1:]) >= 2:
        quality = int(sys.argv[2])
    if len(sys.argv[1:]) == 3:
        resize = int(sys.argv[3])
        resize = (int(resize), int(resize))
    elif len(sys.argv[1:]) == 4:
        resize_width, resize_height = sys.argv[3:]
        resize = (int(resize_width), int(resize_height))

    filename, file_ext = os.path.splitext(os.path.split(full_filename)[1])

    outfilename = os.path.join(
        'output', '{}_{}_{}{}'.format(
            filename, resize[0], resize[1], file_ext))

    with open(outfilename, 'w') as outfile:
        with open(full_filename, 'r') as infile:
            img_resize(infile, outfile, resize, quality)
