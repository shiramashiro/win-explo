import os
import shutil


def classify(base_dir):
    files = os.listdir(base_dir)
    # 遍历 base_dir 目录下的所有文件以及目录
    for file_item in files:
        # 当前遍历的数组元素，以 . 分割，得到一个文件名以及后缀名的数组
        filetext = os.path.splitext(file_item)
        # 判断目录下的当前对象是否为文件，文件则返回 True，目录则返回 False
        source_obj = os.path.join(base_dir, file_item)
        if os.path.isfile(source_obj):
            # 该文件类型的目录
            dest_dir = os.path.join(base_dir, filetext[1].split('.')[1].upper())
            # 如果存放该文件的目录不存在，则创建
            if not os.path.exists(dest_dir):
                os.mkdir(dest_dir)
            # 将该文件存放到符合的目录中
            shutil.move(source_obj, dest_dir)


classify(r'E:\CommonFolders\Pictures')