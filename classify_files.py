import os
import shutil
import time


def pathexists(filepath):
    """
    判断文件或文件夹是否存在
    :param filepath: 传入一个文件或文件夹的绝对路径
    :return: 无论是否存在，都会返回一个绝对路径
    """
    if not os.path.exists(filepath):
        os.makedirs(filepath)
    return filepath


def typesort(filepath, filetype, basepath):
    """
    按照文件类型进行分类
    :param filepath: 文件的绝对路径
    :param filetype: 文件类型，比如 .zip .rar .png .jpg ...
    :param basepath: 分类之后保存的目标路径,之所以是base命名，是因为在后续操作中会凭借路径
    """
    filepatt = os.path.splitext(filepath)[1].split('.')[1]
    if filetype == filepatt:
        destdir = pathexists(os.path.join(basepath, filepatt.upper()))
        shutil.move(filepath, destdir)


def timesort(filepath, timemode, basepath):
    """
    按照时间进行分类。
    :param filepath: 文件路径
    :param timemode: 时间模式，年、月、日三种模式
    :param basepath: 分类之后保存的目标路径，之所以是base命名，是因为在后续操作中会凭借路径
    """
    timestamp = os.path.getmtime(filepath)
    timenodes = time.strftime("%Y-%m-%d", time.localtime(timestamp)).split('-')
    if timemode == 'y':
        destdir = pathexists(os.path.join(basepath, timenodes[0]))
    elif timemode == 'm':
        destdir = pathexists(os.path.join(basepath, timenodes[0], timenodes[1]))
    else:
        destdir = pathexists(os.path.join(basepath, timenodes[0], timenodes[1], timenodes[2]))
    shutil.move(filepath, destdir)


def mtsort(filepath, basepath, timemode, filetype):
    print('先按时间进行分类，然后再将该类型的文件进行分类')

def tmsort(filepath, basepath, filetype, timemode):
    print('先将该类型的文件进行分类，然后再按时间分类')


def sortfiles(usefuldir, destdir, timemode=None, filetype=None, order=None):
    """
    对指定目录下的文件进行分类
    :param usefuldir: 可实际操作的目录
    :param destdir: 目标目录
    :param timemode: 时间模式
    :param filetype: 文件类型
    :param order: 时间和文件类型排序顺序，mt：时间在前，类型在后；tm：类型在前，时间在后
    """
    files = os.listdir(usefuldir)
    for file in files:
        filepath = os.path.join(usefuldir, file)
        if os.path.isfile(filepath):
            print(filepath)
            if timemode is not None:
                timesort(filepath, timemode, destdir)
            elif filetype is not None:
                typesort(filepath, filetype, destdir)


sortfiles(usefuldir=r'E:\CommonFolders\Downloads', destdir=r'E:\CommonFolders\Downloads', filetype='zip')


def unsort(base_dir):
    """
    取消分类，将操作的目录下的所有文件移动到本目录下。
    :param base_dir: 操作的目录
    """
    # 1. 将目录下的所有文件移动到操作的目录下
    objs = os.listdir(base_dir)
    for obj in objs:
        print(os.listdir(os.path.join(base_dir, obj)))
