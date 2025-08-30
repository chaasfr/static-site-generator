from textnode import TextNode, TextType
from generator import generate_pages_recursive

import shutil
import os
import sys

from constant import *



def clean_dest_and_copy(src, dest):
    if os.path.exists(dest):
        shutil.rmtree(dest)
    os.mkdir(dest)
    for item in os.listdir(src):
        path_src = os.path.join(src, item)
        print(path_src)
        if os.path.isfile(path_src):
            shutil.copy(path_src, dest)
        else:
            path_dest = os.path.join(dest, item)
            clean_dest_and_copy(path_src, path_dest)

def main():
    basepath = '/'
    if len(sys.argv) > 1:
        basepath = sys.argv[1]

    clean_dest_and_copy(path_to_static, path_to_public)
    generate_pages_recursive(basepath, path_to_content, path_to_template, path_to_public)


if __name__ == '__main__':
    main()