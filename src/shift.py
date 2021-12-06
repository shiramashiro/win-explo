import os.path
import shutil
import dissect
from enum import Enum


class Mode(Enum):
    BY_NAME = 'reform file by name.'
    BY_TYPE = 'reform file by type.'
    NO_MODE = 'not any mode, just move directly.'


def reform(src: str, dst: str, mode: Mode, pattern: str = None):
    """
    将目录下的文件移动到目标目录下。
    如果传入了 mode 为 Mode.BY_NAME，只会移动正确匹配了文件名中包含了 pattern 字符的文件。
    如果传入了 mode 为 Mode.BY_TYPE，只会移动正确匹配了文件后缀名包含了 pattern 字符的文件。
    如果传入了 mode 为 Mode.NO_MODE，在 src 目录中，创建一个以每个文件的后缀名的全大写的文件夹，并将其移动到对应的文件夹内。
        并且 pattern 不应该传入。
    :param src: 对 src 目录下的文件进行分类，传入 src 的绝对路径。
    :param dst: 将 src 目录下的文件移动到 dst 目录下，传入 dst 的绝对路径。
    :param mode: 源目录下的文件以何种模式进行分类。BY_NAME模式：匹配对应的文件，将它们移动到目标目录中；BY_TYPE：匹配对应的类型，将它们移动到目标目录中；
                NO_MODE：直接将源目录下的文件以文件后缀名命名，创建文件夹，把它们移动到对应文件夹内。
    :param pattern: 匹配的字符。BY_NAME模式：比如，匹配文件名包含 “abc” 的文件；BY_TYPE模式：比如，匹配文件类型为 zip 的文件。
    """
    files = dissect.listfiles(src)
    for file in files:
        if mode == Mode.BY_NAME:
            filepath = dissect.filename(file, pattern)
            if filepath:
                shutil.move(src=filepath, dst=dissect.exists(dst))
        elif mode == Mode.BY_TYPE:
            distpath = dissect.filetype(file, pattern, dst)
            if distpath:
                shutil.move(src=file, dst=dissect.exists(distpath))
        else:
            filetype = dissect.mold(file)
            distpath = os.path.join(dst, filetype.upper())
            shutil.move(src=file, dst=dissect.exists(distpath))