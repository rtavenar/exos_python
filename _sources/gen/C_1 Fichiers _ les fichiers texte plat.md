# C.1 Fichiers : les fichiers texte plat

**Énoncé**

Codez une fonction `compte_mots` qui prend en entrée un nom de fichier et retourne le nombre de "mots" dans le fichier en question (séparés par des espaces).

**Exemple d'entrée**

```
print(compte_mots("a.txt"))
```

**Exemple de sortie**

```
5
```

**Aide**

https://rtavenar.github.io/poly_python/content/fichiers.html

<div id="pad"></div>
            <script>Pythonpad('pad', {'id': 'C.1', 'title': 'Testez votre solution ici', 'src': 'def compte_mots(nom_du_fichier):\n  # Codez ici votre fonction et modifiez la valeur de retour si besoin\n  return None', 'files': {'b.txt': {'type': 'text', 'body': 'Celui-ci en contient quatre'}, 'a.txt': {'type': 'text', 'body': 'Ce fichier contient cinq mots'}, '.grader.py': {'type': 'text', 'body': 'import unittest\n\nclass TestExercise(unittest.TestCase):\n    def test_all(self):\n        self.assertEquals(compte_mots("a.txt"), 5)\n        self.assertEquals(compte_mots("b.txt"), 4)\n\nif __name__ == \'__main__\':\n    try:\n        from main import *\n    except:\n        print("Le code fourni n\'est pas valide")\n    suite = unittest.TestLoader().loadTestsFromTestCase(TestExercise)\n    output = unittest.TextTestRunner(verbosity=2).run(suite)\n\n    if output.wasSuccessful():\n        f = open(\'.passed.json\', \'w\')\n        f.close()\n        print(\'Bravo ! Le code fourni a passé les tests avec succès, il semble valide !\')'}}})</script>


````{admonition} Cliquez ici pour voir la solution
:class: tip, dropdown

```python
def compte_mots(nom_de_fichier):
  texte = open(nom_de_fichier, "r", encoding="utf-8").read()
  return len(texte.split())
```
````
