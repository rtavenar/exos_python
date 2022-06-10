# B.4 Fonctions : Argument avec une valeur par défaut

**Énoncé**

Codez une fonction somme qui permet d'ajouter au maximum 4 entiers. La fonction prend au minimum 1 entier en paramètre et 4 au maximum.

**Exemple d'appel de la fonction**

```
somme(1,2,3)
```

**Exemple de valeur de retour**

```
6
```

**Aide**

https://rtavenar.github.io/poly_python/content/struct.html#fonctions

<div id="pad"></div>
            <script>Pythonpad('pad', {'id': 'B.4', 'title': 'Testez votre solution ici', 'src': 'def somme():\n  # Codez votre fonction ici', 'files': {'.grader.py': {'type': 'text', 'body': 'import unittest\n\nclass TestExercise(unittest.TestCase):\n    def test_all(self):\n        self.assertIsInstance(somme, types.FunctionType)\n\nif __name__ == \'__main__\':\n    try:\n        from main import *\n    except:\n        print("Le code fourni n\'est pas valide")\n    suite = unittest.TestLoader().loadTestsFromTestCase(TestExercise)\n    output = unittest.TextTestRunner(verbosity=2).run(suite)\n\n    if output.wasSuccessful():\n        f = open(\'.passed.json\', \'w\')\n        f.close()\n        print(\'Bravo ! Le code fourni a passé les tests avec succès, il semble valide !\')'}}})</script>


````{admonition} Cliquez ici pour voir la solution
:class: tip, dropdown

```python
def somme(entier1, entier2=0, entier3=0, entier4=0):
  # Codez votre fonction ici
  return entier1+entier2+entier3+entier4
```
````
