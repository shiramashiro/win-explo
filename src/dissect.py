import os
import re


def exists(src: str) -> str:
    """
    判断目录路径是否存在
    :param src: 目录路径
    :return: 目录存在就直接返回该目录路径；目录不存在就创建该目录，并且返回目录路径
    """
    if not os.path.exists(src):
        os.makedirs(src)
    return src


def listfiles(src: str) -> []:
    """
    列出目录下的所有文件。
    :param src: 目录路径
    :return: 返回一组文件的绝对路径
    """
    filespath = []
    for item in os.listdir(src):
        path = os.path.join(src, item)
        if os.path.isfile(path):
            filespath.append(path)
    return filespath


def listdirs(src: str) -> []:
    """
    列出 src 目录下所有的目录
    :param src: 列出 src 目录的所有目录
    :return: 返回一组目录的绝对路径
    """
    dirspath = []
    for item in os.listdir(src):
        path = os.path.join(src, item)
        if os.path.isdir(path):
            dirspath.append(path)
    return dirspath


def mold(src: str) -> str:
    """
    获得文件的后缀名。
    :param src: 文件路径
    :return: 后缀名
    """
    return os.path.splitext(src)[1].split('.')[1]


def filetype(src: str, pattern: str, dst: str) -> str:
    """
    分析文件类型是否与字符匹配。
    :param src: 文件路径
    :param pattern: 字符
    :param dst: 最终将文件输出到哪个目录下，即目标目录路径
    :return: 匹配成功返回该文件路径，且文件路径拼接该文件类型作为名称的目录；匹配失败返回None
    """
    dstdir = None
    filetype = mold(src)
    if pattern == filetype:
        dstdir = os.path.join(dst, filetype.upper())
    return dstdir


def filename(src: str, pattern: str) -> str:
    """
    分析文件名是否与字符匹配。
    :param src: 文件路径
    :param pattern: 字符
    :return: 匹配成功返回该文件路径；匹配失败返回None
    """
    matched = None
    if re.search(pattern, src):
        matched = src
    return matched
