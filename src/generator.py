from convert import markdown_to_html_node
from extract import extract_title
import os



def generate_page(basepath, from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    
    with open(from_path, "r") as from_file:
        markdown = from_file.read()
        html_content = markdown_to_html_node(markdown).to_html()
        title = extract_title(markdown)
        with open(template_path, "r") as template:
            result = template.read()
            result = result.replace("{{ Title }}", title)
            result = result.replace("{{ Content }}", html_content)
            result = result.replace('href="/',f'href="{basepath}')
            result = result.replace('src="/',f'src="{basepath}')
            
            with open (dest_path, "w") as dest_file:
                dest_file.write(result)
                
def generate_pages_recursive(basepath, dir_path_content, template_path, dest_dir_path):
    print(f"recursive look in {dir_path_content} towards {dest_dir_path}")
    files = os.listdir(dir_path_content)
    for file in files:
        path_file = os.path.join(dir_path_content, file)
        dest_file = os.path.join(dest_dir_path,file)
        if not os.path.isfile(path_file):
            os.mkdir(dest_file)
            generate_pages_recursive(basepath, path_file, template_path, dest_file)
        elif path_file[-3:] == ".md":
            dest_file = dest_file.replace(".md",".html")
            generate_page(basepath, path_file, template_path, dest_file)