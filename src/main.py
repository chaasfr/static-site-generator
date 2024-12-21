from textnode import TextNode, TextType

import shutil
import os

path_to_static="/home/chaasfr/workspace/static-site/static"
path_to_public="/home/chaasfr/workspace/static-site/public"

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
    clean_dest_and_copy(path_to_static, path_to_public)


if __name__ == '__main__':
    main()