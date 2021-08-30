import os
import json

def format_code(code_skeleton, code_sol, title_level=2):
    s = "\n\n"
    
    s += ("#" * title_level) + " Squelette\n\n"
    s += "```{code-cell} python\n"
    # s += "```python\n"
    s += code_skeleton
    if not s.endswith("\n"):
        s += "\n"
    s += "```\n\n"
    
    s += "````{dropdown} Proposition de solution\n\n"
    # s += "```{code-cell} python\n"
    s += "```python\n"
    s += code_sol
    if not s.endswith("\n"):
        s += "\n"
    s += "```\n````\n"
    
    return s


def read_instructions(fname_instructions, title_level_increment=0):
    instructions = []
    for line in open(fname_instructions, "r").readlines():
        if line.startswith("#"):
            instructions.append(("#" * title_level_increment) + line.strip())
        else:
            instructions.append(line.strip())
    return "\n".join(instructions)


def get_title(input_folder):
    str_base_folder = "data/"
    pos = input_folder.find(str_base_folder) + len(str_base_folder)
    return input_folder[pos:]


def get_output_fname(input_folder):
    title = get_title(input_folder)
    return os.path.join("book", "gen", title.replace("/", "_").replace(":", "_") + ".md")


def get_full_path(partial_path):
    if os.path.exists(os.path.join(partial_path, "instructions.md")):
        return partial_path
    subdirs = [
        path 
        for path in os.listdir(partial_path) 
        if (not path.startswith(".") and os.path.isdir(os.path.join(partial_path, path)))
    ]
    assert len(subdirs) == 1
    return get_full_path(os.path.join(partial_path, subdirs[0]))


def list_exercises(path="data/"):
    return [
        os.path.join(path, subpath)
        for subpath in os.listdir(path)
        if (not subpath.startswith(".") and os.path.isdir(os.path.join(path, subpath)))
    ]
    

def myst_header():
    return """---
jupytext:
  formats: md:myst
  text_representation:
    extension: .md
    format_name: myst
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

"""

def gen_content(input_folder):
    title = get_title(input_folder)
    output_fname = get_output_fname(input_folder)
    
    # instructions.md
    fname_instructions = os.path.join(input_folder, 
                                      "instructions.md")
    instructions = read_instructions(fname_instructions,
                                     title_level_increment=1)
    
    # main.py
    fname_skeleton = os.path.join(input_folder, 
                                  "main.py")
    skeleton = open(fname_skeleton, "r").read()
    
    # solution/main.py
    fname_sol = os.path.join(input_folder, 
                             "solution",
                             "main.py")
    sol = open(fname_sol, "r").read()
    
    # Generate output
    fp = open(output_fname, "w")
    
    # fp.write(myst_header())
    fp.write(f"# {title}\n\n")
    fp.write(instructions)
    fp.write(format_code(skeleton, sol, title_level=2))
    
    fp.close()


def write_toc(list_content_files):
    toc_chapters = json.load(open("py/parts.json", "r"))
    sorted_content_files = sorted(list_content_files)
    
    fp = open("book/_toc.yml", "w")
    fp.write("format: jb-book\nroot: index\nchapters:\n")
    for chap in toc_chapters:
        fname_chap = "gen/" + chap['preffix'] + " " + chap['title'].replace("/", "_") + ".md"
        open("book/" + fname_chap, "w").write(f"# {chap['preffix']} {chap['title']}\n\nCette section contient des exercices.")
        fp.write(f"  - file: {fname_chap[:-3]}\n")
        fp.write("    sections:\n")
        for fname in sorted_content_files:
            if fname.startswith(f"book/gen/{chap['preffix']}"):
                sub_name = fname[5:-3].replace(':', '\\:')
                fp.write(f"    - file: {sub_name}\n")
    fp.close()

if __name__ == "__main__":
    list_output_files = []
    for ex in list_exercises():
        full_path = get_full_path(ex)
        list_output_files.append(get_output_fname(full_path))
        gen_content(full_path)
    write_toc(list_output_files)
