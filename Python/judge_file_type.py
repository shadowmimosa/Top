import os
import struct
import filetype
from pathlib import Path


def get_file_type(filename):
    file_type_map = {
        '7790': 'exe',
        '7784': 'midi',
        '8075': 'zip',
        '8297': 'rar',
        '7173': 'gif',
        '6677': 'bmp',
        '13780': 'png',
        '255216': 'jpg',
    }

    fp = open(filename, 'rb')
    str_info = struct.unpack_from("BB", fp.read(2))
    str_code = '%d%d' % (str_info[0], str_info[1])
    fp.close()

    return 'unknown' if str_code not in file_type_map else file_type_map[
        str_code]


def use_filetype(filename):
    kind = filetype.guess(filename)

    if kind and kind.extension == 'mp4':
        print('is mp4')
        return True


def main():
    dirpath = 'C:/Users/ShadowMimosa/Desktop/Temp/world/730'

    for filename in Path(dirpath).iterdir():
        if not filename.is_file():
            continue

        file_type = use_filetype(str(filename))
        if not file_type:
            continue

        Path(filename).rename(filename.with_suffix('.mp4'))


if __name__ == '__main__':
    main()