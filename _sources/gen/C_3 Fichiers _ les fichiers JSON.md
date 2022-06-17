# C.3 Fichiers : les fichiers JSON

**Énoncé**

Codez une fonction qui lit un fichier JSON et, pour un préfixe passé en argument, retourne le nombre de clés de premier niveau du fichier JSON qui commencent par le préfixe.

**Exemple d'entrée**

```
print(compte_cles_prefixe("a.json", "abc"))
```

**Exemple de sortie**

```
2
```

**Aide**

https://rtavenar.github.io/poly_python/content/fichiers.html

<div id="pad"></div>
            <script>Pythonpad('pad', {'id': 'C.3', 'title': 'Testez votre solution ici', 'src': 'import json\n\ndef compte_cles_prefixe(nom_du_fichier, prefixe):\n  # Codez votre fonction ici et modifiez sa valeur de retour si besoin\n  return None\n', 'files': {'a.json': {'type': 'text', 'body': '{\n  "abd": 12,\n  "abcdef": 1,\n  "cv": {\n    "abcd": 3\n  },\n  "abc": 2\n}'}, 'b.json': {'type': 'text', 'body': '{\n  "abcd": 12,\n  "abcdef": 1,\n  "cv": {\n    "abcd": 3\n  },\n  "abc": 2\n}'}, '.grader.py': {'type': 'text', 'body': 'import unittest\n\nclass TestExercise(unittest.TestCase):\n    def test_all(self):\n        self.assertEquals(compte_cles_prefixe("a.json", "abc"), 2)\n        self.assertEquals(compte_cles_prefixe("b.json", "abc"), 3)\n        \n\nif __name__ == \'__main__\':\n    try:\n        from main import *\n    except:\n        print("Le code fourni n\'est pas valide")\n    suite = unittest.TestLoader().loadTestsFromTestCase(TestExercise)\n    output = unittest.TextTestRunner(verbosity=2).run(suite)\n\n    if output.wasSuccessful():\n        f = open(\'.passed.json\', \'w\')\n        f.close()\n        print(\'Bravo ! Le code fourni a passé les tests avec succès, il semble valide !\')'}}})</script>


````{admonition} Cliquez ici pour voir la solution
:class: tip, dropdown

```python
import json

def compte_cles_prefixe(nom_du_fichier, prefixe):
  d = json.load(open(nom_du_fichier, "r", encoding="utf-8"))
  n = 0
  for k in d.keys():
    if k.startswith(prefixe):
      n += 1
  return n
```
````
