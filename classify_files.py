import os
import shutil

'''
这是一个自动化分类文件的模块
'''


'''
对目录中的文件进行分类，并且可以按照时间进行再分类。
'''
def classify(basedir, timelen):
    files = os.listdir(basedir)
    # 遍历 base_dir 目录下的所有文件以及目录
    for file in files:
        # 当前遍历的数组元素，以 . 分割，得到一个文件名以及后缀名的数组
        filename = os.path.splitext(file)
        # 判断目录下的当前对象是否为文件，文件则返回 True，目录则返回 False
        source = os.path.join(basedir, file)
        if os.path.isfile(source):
            # 该文件类型的目录
            destdir = os.path.join(basedir, filename[1].split('.')[1].upper())
            # 如果存放该文件的目录不存在，则创建
            if not os.path.exists(destdir):
                os.mkdir(destdir)
            # 将该文件存放到符合的目录中
            shutil.move(source, destdir)


classify(r'E:\CommonFolders\Downloads')