from textnode import TextNode, TextType
from generator import generate_page

import shutil
import os


path_to_root = "/Users/christianhaas-frangi/workspace/boot/static-site-generator/"

path_to_static = path_to_root + "static/"
path_to_public = path_to_root + "public/"
path_to_index_md = path_to_root + "content/index.md"
path_to_template = path_to_root + "template.html"
path_to_index_html = path_to_public + "index.html"


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
    generate_page(path_to_index_md, path_to_template, path_to_index_html)


if __name__ == '__main__':
    main()