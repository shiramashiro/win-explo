import os
import shutil
import dissect
import win32file
from enum import Enum


class Mode(Enum):
    BY_NAME = 'reform file by name.'
    BY_TYPE = 'reform file by type.'
    NO_MODE = 'not any mode, just move directly.'


def pack(src: str, dst: str, pattern: str, zipname: str):
    """
    匹配 src 目录下文件名包含 pattern 子串的文件，并把所有文件打包成 zip 格式的归档文件，然后再将其移动到 dst 目录下保存。
    :param src: 将 src 目录下的包含了 pattern 子串的文件进行压缩处理。
    :param dst: 将归档文件移动到 dst 目录下保存。
    :param pattern: 文件名称包含了 pattern 子串的文件。
    :param zipname: 归档文件的名称。
    """
    files = dissect.listfiles(src)
    root_dir = dissect.exists(os.path.join(src, zipname))
    base_dir = dissect.exists(os.path.join(src, zipname, zipname))
    for file in files:
        matched = dissect.filename(file, pattern)
        if matched:
            shutil.copy2(file, base_dir)
    zip_path = shutil.make_archive(zipname, 'zip', root_dir)
    shutil.rmtree(root_dir)
    shutil.move(zip_path, dst)


def extractname(src: str, dst: str, pattern: str):
    """
    将 src 目录下以及子目录中包含了 pattern 子串的文件名移动到 dst 目录下。
    将会递归的扫描 src 目录，直到 src 子目录的子目录...没有目录为止。
    :param src: 提取 src 目录下的全部文件。
    :param dst: 提取 src 目录下的全部文件到 dst 目录下 。
    :param pattern: 文件名包含了 pattern 子串。
    """
    files = dissect.listfiles(src)

    if len(files) > 0:
        for file in files:
            if win32file.GetFileAttributes(file) != 38:
                if dissect.filename(file, pattern):
                    dst_filename = os.path.split(file)[1]
                    dst_filepath = os.path.join(dissect.exists(dst), dst_filename)
                    if os.path.exists(dst_filepath):
                        os.remove(dst_filepath)
                    else:
                        shutil.move(file, dst)

    dircs = dissect.listdirs(src)
    if len(dircs) > 0:
        for dirc in dircs:
            extractname(dirc, dst, pattern)


def extractype(src: str, dst: str, format: str):
    """
    将 src 目录下以及子目录中指定类型的文件提取到 dst 目录下。
    将会递归的扫描 src 目录，直到 src 子目录的子目录...没有目录为止。
    :param src: 提取 src 目录下的全部文件。
    :param dst: 提取 src 目录下的全部文件到 dst 目录下 。
    :param format: 文件类型。
    :return:
    """
    files = dissect.listfiles(src)

    if len(files) > 0:
        for file in files:
            if win32file.GetFileAttributes(file) != 38:
                if dissect.filetype(file, format, dst):
                    dst_filename = os.path.split(file)[1]
                    dst_filepath = os.path.join(dissect.exists(dst), dst_filename)
                    if os.path.exists(dst_filepath):
                        os.remove(dst_filepath)
                    else:
                        shutil.move(file, dst)

    dircs = dissect.listdirs(src)
    if len(dircs) > 0:
        for dirc in dircs:
            extractype(dirc, dst, format)


def extractall(src: str, dst: str):
    """
    将 src 目录下以及子目录的文件全部提取到 dst 目录下。
    将会递归的扫描 src 目录，直到 src 子目录的子目录...没有目录为止。
    :param src: 提取 src 目录下的全部文件。
    :param dst: 提取 src 目录下的全部文件到 dst 目录下 。
    """
    files = dissect.listfiles(src)

    if len(files) > 0:
        for file in files:
            if win32file.GetFileAttributes(file) != 38:
                dst_filename = os.path.split(file)[1]
                dst_filepath = os.path.join(dissect.exists(dst), dst_filename)
                if os.path.exists(dst_filepath):
                    os.remove(dst_filepath)
                else:
                    shutil.move(file, dst)

    dircs = dissect.listdirs(src)
    if len(dircs) > 0:
        for dirc in dircs:
            extractall(dirc, dst)


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
