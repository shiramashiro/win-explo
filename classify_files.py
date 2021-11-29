import os
import shutil
import time


def dir_exists(dir):
    if not os.path.exists(dir):
        os.makedirs(dir)
    return dir


def time_sort(obj_path, time_order, dest_dir):
    """
    按照时间进行排序，可以按照年、月、日进行分类。月是年-月；日是年-月-日的形式进行分类。
    :param obj_path: 文件的绝对路径
    :param time_order: 是否以时间形式进行分类
    :param dest_dir: 移动到目标目录
    """
    # 获取文件最后修改的时间戳
    timestamp = os.path.getmtime(obj_path)
    # 格式化时间，并以-分割开来
    timesarr = time.strftime("%Y-%m-%d", time.localtime(timestamp)).split('-')
    # 以时间形式创造的目录
    build_dir = None
    if time_order == 'y':
        build_dir = dir_exists(os.path.join(dest_dir, timesarr[0]))
    elif time_order == 'm':
        build_dir = dir_exists(os.path.join(dest_dir, timesarr[0], timesarr[1]))
    elif time_order == 'd':
        build_dir = dir_exists(os.path.join(dest_dir, timesarr[0], timesarr[1], timesarr[2]))

    if build_dir is not None:
        shutil.move(obj_path, build_dir)


def sort(base_dir, sub_dir_name=None, time_order=None):
    """
    对当前目录进行文件分类。
        你可以选择给每一个对应的类型目录下再以时间进行分类存放。
        你可以选择在当前目录下创建一个子目录，然后再进行分类。
    :param base_dir: 当前目录，即你要操作的目录的绝对路径
    :param sub_dir_name: 是否在当前目录下创建一个子目录
    :param time_order: 是否以时间形式进行分类
    """
    # 列出目录下的所有文件以及文件夹
    objs = os.listdir(base_dir)
    # 对这些文件以及文件夹进行循环
    for obj in objs:
        # 获得该文件或者文件夹的绝对路径
        obj_path = os.path.join(base_dir, obj)
        # 根据绝对路径判断该对象是否为一个文件
        if os.path.isfile(obj_path):
            # 将文件名以及文件后缀名分割开来，例如 test.py => ['test', '.py']
            filename_suffix = os.path.splitext(obj)
            # 希望将当前目录下所有的文件存放到指定的子目录下
            child_dir = None
            if sub_dir_name is not None:
                child_dir = dir_exists(os.path.join(base_dir, sub_dir_name))
            # 有子目录或没有子目录的情况
            dest_dir = None
            if child_dir is not None:
                dest_dir = dir_exists(os.path.join(child_dir, filename_suffix[1].split('.')[1].upper()))
            else:
                dest_dir = dir_exists(os.path.join(base_dir, filename_suffix[1].split('.')[1].upper()))

            # 是否以时间进行分类
            if time_order is not None:
                # 以时间进行分类，然后再移动到对应类型的目录
                time_sort(obj_path, time_order, dest_dir)
            else:
                # 不以时间进行分类，直接移动到对应类型的目录
                shutil.move(obj_path, dest_dir)


def unsort(base_dir):
    """
    取消分类，将操作的目录下的所有文件移动到本目录下。
    :param base_dir: 操作的目录
    """
    # 1. 将目录下的所有文件移动到操作的目录下
    objs = os.listdir(base_dir)
    for obj in objs:
        print(os.listdir(os.path.join(base_dir, obj)))


# unsort(r'E:\CommonFolders\Downloads')
sort(r'E:\CommonFolders\Downloads', time_order='m')
