# B.5 Fonctions : appels récursifs

**Énoncé**

Codez une fonction `somme_entiers` qui calcule la somme des `n` premiers entiers (`n` étant un paramètre de cette fonction) de manière récursive (c'est-à-dire que le calcul de `somme_entiers(n)` devra utiliser un (au moins) autre appel à `somme_entiers` avec un argument différent de `n`).

**Exemple d'appel de la fonction**

```
somme_entiers(10)
```

**Exemple de valeur de retour**

```
55
```

**Aide**

https://rtavenar.github.io/poly_python/content/struct.html#fonctions

<div id="pad"></div>
            <script>Pythonpad('pad', {'id': 'B.5', 'title': 'Testez votre solution ici', 'src': 'def somme_entiers(n):\n  # Codez votre fonction ici (et changez sa valeur de retour !)\n  return -1', 'files': {'.grader.py': {'type': 'text', 'body': 'import unittest\n\nclass TestExercise(unittest.TestCase):\n    def test_all(self):\n        self.assertEquals(somme_entiers(10), 55)\n        self.assertEquals(somme_entiers(1), 1)\n\nif __name__ == \'__main__\':\n    try:\n        from main import *\n    except:\n        print("Le code fourni n\'est pas valide")\n    suite = unittest.TestLoader().loadTestsFromTestCase(TestExercise)\n    output = unittest.TextTestRunner(verbosity=2).run(suite)\n\n    if output.wasSuccessful():\n        f = open(\'.passed.json\', \'w\')\n        f.close()\n        print(\'Bravo ! Le code fourni a passé les tests avec succès, il semble valide !\')'}}})</script>


````{admonition} Cliquez ici pour voir la solution
:class: tip, dropdown

```python
def somme_entiers(n):
  if n == 0:
    return 0
  return n + somme_entiers(n-1)
```
````
