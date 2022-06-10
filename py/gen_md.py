import os
import json


def replace_urls(text):
    """Applique les changements d'URLs spécifiés dans le fichier 
    `py/change_urls.json` pour pointer vers les bonnes sections du poly.
    """
    target_urls = json.load(open("py/change_urls.json", "r"))
    for modif in target_urls:
        text = text.replace(modif["source"], modif["target"])
    return text


def comment_code(code):
    """Commente toutes les lignes de la chaîne `code` en les débutant 
    par un symbole `#` si ce n'est pas déjà le cas.
    """
    output_code = ""
    for line in code.split("\n"):
        if not line.startswith("#"):
            output_code += "# " + line + "\n"
        else:
            output_code += line + "\n"
    return output_code

def format_code(code_skeleton, code_sol, files, problem_id, unit_test_file=None):
    """Traduit un squelette et une solution proposée en code HTML permettant
    de présenter le squelette dans un encadré Pythonpad et la solution dans une
    section caché que l'on peut afficher."""
    s = "\n\n"

    json_content = {
        "id": problem_id,
        "title": "Testez votre solution ici",
        "src": code_skeleton
    }
    if len(files) > 0:
        json_content["files"] = include_files(files)
    if unit_test_file is not None:
        with open(unit_test_file, "r") as fp:
            unit_test_contents = json.load(fp)
            unit_test_code = unit_test_contents["tests"][0]["code"].split("\n")
            
            content_ut = """import unittest

class TestExercise(unittest.TestCase):
    def test_all(self):
        {}

if __name__ == '__main__':
    try:
        from main import *
    except:
        print("Le code fourni n'est pas valide")
    suite = unittest.TestLoader().loadTestsFromTestCase(TestExercise)
    output = unittest.TextTestRunner(verbosity=2).run(suite)

    if output.wasSuccessful():
        f = open('.passed.json', 'w')
        f.close()
        print('Bravo ! Le code fourni a passé les tests avec succès, il semble valide !')""".format("\n        ".join(unit_test_code))
            
            json_content["files"] = json_content.get("files", {})
            json_content["files"].update(
                {
                    ".grader.py": {
                        "type": "text",
                        "body": content_ut
                    }
                }
            )
    
    json_str = str(json_content)
    s += """<div id="pad"></div>
            <script>Pythonpad('pad', %s)</script>\n\n\n""" % json_str
    
    s += "````{admonition} Cliquez ici pour voir la solution\n:class: tip, dropdown\n\n"
    s += "```python\n"
    s += code_sol
    if not s.endswith("\n"):
        s += "\n"
    s += "```\n````\n"

    return s


def read_instructions(fname_instructions, title_level_increment=0):
    """Lit les instructions contenues dans un fichier Markdown récupéré 
    depuis l'export repl.it et les met en forme pour les besoins de 
    notre Jupyter Book."""
    instructions = []
    for line in open(fname_instructions, "r").readlines():
        if line.startswith("#"):
            instructions.append(("#" * title_level_increment) + line.strip())
        else:
            instructions.append(line.strip())
    instructions = "\n".join(instructions)
    instructions = replace_urls(instructions)
    instructions = instructions.replace("\n```\n\n```", "")  # Ugly fix for the multiple input bug
    return instructions


def get_title(input_folder):
    """Récupère le nom de la section à partir du répertoire dans 
    lequel se trouvent les données repl.it correspondantes.
    
    Exemple
    -------
    
    >>> get_title("data/3.F. If/else: Échecs : mouvement du roi")
    '3.F. If/else: Échecs : mouvement du roi'
    """
    str_base_folder = "data/"
    pos = input_folder.find(str_base_folder) + len(str_base_folder)
    return input_folder[pos:]


def get_output_fname(input_folder):
    """Génère le nom du répertoire de sortie à partir du répertoire dans 
    lequel se trouvent les données repl.it correspondantes.
    
    Exemple
    -------
    
    >>> get_output_fname("data/3.F. If/else: Échecs : mouvement du roi")
    'book/gen/3_F_ If_else_ Échecs _ mouvement du roi.md'
    """
    title = get_title(input_folder)
    title = title.replace("/", "_").replace(":", "_")
    title = title.replace(".", "_")
    return os.path.join("book", "gen", title + ".md")


def get_full_path(partial_path):
    """Retourne le chemin vers le répertoire contenant le fichier d'instructions 
    à partir d'un nom de répertoire de base.
    
    Exemple
    -------
    
    >>> get_full_path("data/3.F. If/else: Échecs : mouvement du roi")
    'data/3.F. If/else: Échecs : mouvement du roi'
    """
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
    """Retourne la liste des exercices trouvés dans le répertoire `data/` 
    issu de l'export repl.it"""
    return [
        os.path.join(path, subpath)
        for subpath in os.listdir(path)
        if (not subpath.startswith(".") and os.path.isdir(os.path.join(path, subpath)))
    ]
    

def myst_header():
    """Retourne le header nécessaire pour nos fichiers pour une 
    intégration dans Jupyter Book."""
    
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
    """Fonction principale qui, à partir d'un répertoire de données issu
    de l'export repl.it, génère le contenu au format attendu par Jupyter Book.
    """
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
    ex_id = title[:title.find(" ")]
    
    fname_unit_test = os.path.join(input_folder, "unit-tests.json")
    if not os.path.exists(fname_unit_test):
        fname_unit_test = None
    fp.write(
        format_code(skeleton, sol, found_files(input_folder), ex_id,
                    unit_test_file=fname_unit_test)
    )
    
    fp.close()


def write_toc(list_content_files):
    """Construit le fichier YAML de table des matières à partir des sous-parties
    listées dans `py/parts.json` et de la liste des fichiers fournie en argument."""
    toc_chapters = json.load(open("py/parts.json", "r"))
    sorted_content_files = sorted(list_content_files)
    
    fp = open("book/_toc.yml", "w")
    fp.write("format: jb-book\nroot: index\nchapters:\n")
    for chap in toc_chapters:
        fname_chap = "gen/" + chap['preffix'] + " " + chap['title'].replace("/", "_") + ".md"
        open("book/" + fname_chap, "w").write(f"# {chap['preffix']} {chap['title']}\n\n{chap.get('text', '')}")
        fp.write(f"  - file: {fname_chap}\n")
        fp.write("    sections:\n")
        for fname in sorted_content_files:
            if fname.startswith(f"book/gen/{chap['preffix'].replace('.', '_')}"):
                sub_name = fname[5:].replace(':', '\\:')
                fp.write(f"    - file: {sub_name}\n")
    fp.close()


def found_files(input_folder):
    """Liste tous les fichiers d'un répertoire à l'exception des fichiers 
    "main.py", "instructions.md", "unit-tests.json".
    Cette fonction est utilisée pour lister les fichiers de données nécessaires 
    aux exercices de la section C. 
    
    Exemple
    -------
    >>> sorted(found_files("data/C.1 Fichiers : les fichiers texte plat"))
    ['data/C.1 Fichiers : les fichiers texte plat/a.txt', 'data/C.1 Fichiers : les fichiers texte plat/b.txt']
    """
    #listing des fichiers du dossier input_folder
    files = [f for f in os.listdir(input_folder) if os.path.isfile(os.path.join(input_folder, f))]
    #suppression des fichiers main.py instructions.md et unit-tests.json de la liste
    files = [os.path.join(input_folder, f) for f in files if f not in ["main.py", "instructions.md", "unit-tests.json"] and not f.startswith(".")]
    return files


def include_files(files):
    dict_files = {}
    for f in files:
        dict_files.update({os.path.basename(f): {
                    "type": "text",
                    "body": read_file(f)}})
    return dict_files

def read_file(file):
    with open(file, "r") as f:
        return f.read()

if __name__ == "__main__":
    list_output_files = []
    for ex in list_exercises():
        full_path = get_full_path(ex)
        list_output_files.append(get_output_fname(full_path))
        gen_content(full_path)
    write_toc(list_output_files)
