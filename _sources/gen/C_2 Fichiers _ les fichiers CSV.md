# C.2 Fichiers : les fichiers CSV

**Énoncé**

Codez une fonction qui compte le nombre de cellules non vides d'un fichier CSV séparé par des points-virgules.

**Exemple d'entrée**

```
print(nb_non_vides("a.csv"))
```

**Exemple de sortie**

```
8
```

**Aide**

https://rtavenar.github.io/poly_python/content/fichiers.html

<div id="pad"></div>
            <script>Pythonpad('pad', {'id': 'C.2', 'title': 'Testez votre solution ici', 'src': 'import csv\n\ndef nb_non_vides(nom_du_fichier):\n  # Codez votre fonction ici et modifiez la valeur de retour si besoin\n  return None\n', 'files': {'b.csv': {'type': 'text', 'body': '1;2;3\n4;5;6\n7;8;9\n10,10'}, 'a.csv': {'type': 'text', 'body': '12;7;8;9\n1;3;\n0;;0'}, '.grader.py': {'type': 'text', 'body': 'import unittest\n\nclass TestExercise(unittest.TestCase):\n    def test_all(self):\n        self.assertEquals(nb_non_vides("a.csv"), 8)\n        self.assertEquals(nb_non_vides("b.csv"), 10)\n\nif __name__ == \'__main__\':\n    try:\n        from main import *\n    except:\n        print("Le code fourni n\'est pas valide")\n    suite = unittest.TestLoader().loadTestsFromTestCase(TestExercise)\n    output = unittest.TextTestRunner(verbosity=2).run(suite)\n\n    if output.wasSuccessful():\n        f = open(\'.passed.json\', \'w\')\n        f.close()\n        print(\'Bravo ! Le code fourni a passé les tests avec succès, il semble valide !\')'}}})</script>


````{admonition} Cliquez ici pour voir la solution
:class: tip, dropdown

```python
import csv

def nb_non_vides(nom_de_fichier):
  reader = csv.reader(open(nom_de_fichier, "r", encoding="utf-8"), delimiter=";")
  n = 0
  for ligne in reader:
    for cellule in ligne:
      if cellule.strip() != "":
        n += 1
  return n
```
````