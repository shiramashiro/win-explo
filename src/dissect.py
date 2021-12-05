import os
import re


def exists(src):
    """
    判断目录路径是否存在
    :param src: 目录路径
    :return: 目录存在就直接返回该目录路径；目录不存在就创建该目录，并且返回目录路径
    """
    if not os.path.exists(src):
        os.makedirs(src)
    return src


def listfiles(src):
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


def filetype(src, pattern, dst):
    """
    分析文件类型是否与字符匹配。
    :param src: 文件路径
    :param pattern: 字符
    :param dst: 最终将文件输出到哪个目录下，即目标目录路径
    :return: 匹配成功返回该文件路径，且文件路径拼接该文件类型作为名称的目录；匹配失败返回None
    """
    dstdir = None
    filetype = os.path.splitext(src)[1].split('.')[1]
    if pattern == filetype:
        dstdir = os.path.join(dst, filetype.upper())
    return dstdir


def filename(src, pattern):
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
