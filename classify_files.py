import os
import re
import shutil


def get_files(source_path):
    filespath = []
    for item in os.listdir(source_path):
        path = os.path.join(source_path, item)
        if os.path.isfile(path):
            filespath.append(path)
    return filespath


def analyze_file_type(filepath, pattern, destdir):
    destpath = None
    text = os.path.splitext(filepath)[1].split('.')[1]
    if pattern == text:
        destpath = os.path.join(destdir, text.upper())
    return destpath


def analyze_file_name(filepath, pattern):
    correct = None
    if re.search(pattern, filepath):
        correct = filepath
    return correct


def main():
    for item in get_files(r'E:\CommonFolders\Downloads\DOCX'):
        result = analyze_file_name(item, 'ass')
        if result is not None:
            shutil.move(result, r'E:\CommonFolders\Downloads\DOCX\Test2')


main()
