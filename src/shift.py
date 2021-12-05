import shutil
import dissect
from enum import Enum


class Mode(Enum):
    BNAME = 'reform file by name.'
    BTYPE = 'reform file by type.'


def reform(src, dst, mode=None, pattern=None):
    for item in dissect.listfiles(src):
        if mode == Mode.BNAME:
            filepath = dissect.filename(item, pattern)
            if filepath is not None:
                shutil.move(filepath, dissect.exists(dst))
        elif mode == Mode.BTYPE:
            dirpath = dissect.filetype(item, pattern, dst)
            if dirpath is not None:
                shutil.move(item, dissect.exists(dirpath))
        else:
            print('直接移动所有文件到目录下，并以文件后缀名格式创建一个目录')
