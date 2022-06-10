# B.1 Fonctions : retourne un affichage

**Énoncé**


Codez une fonction `affichage_bienvenue` qui affiche le message "Bienvenue". La fonction ne prend aucun paramètre.


**Exemple d'appel de la fonction**


```
affichage_bienvenue()
```

**Exemple de sortie**


```
Bienvenue
```

**Aide**

https://rtavenar.github.io/poly_python/content/struct.html#fonctions

<div id="pad"></div>
            <script>Pythonpad('pad', {'id': 'B.1', 'title': 'Testez votre solution ici', 'src': 'def affichage_bienvenue():\n  # Codez votre fonction ici (et affichez le message de bienvenue !)', 'files': {'.grader.py': {'type': 'text', 'body': 'import unittest\n\nclass TestExercise(unittest.TestCase):\n    def test_all(self):\n        affichage_bienvenue()\n        self.assertEquals(sys.stdout.getvalue()[:-1], \'Bienvenue\')\n\nif __name__ == \'__main__\':\n    try:\n        from main import *\n    except:\n        print("Le code fourni n\'est pas valide")\n    suite = unittest.TestLoader().loadTestsFromTestCase(TestExercise)\n    output = unittest.TextTestRunner(verbosity=2).run(suite)\n\n    if output.wasSuccessful():\n        f = open(\'.passed.json\', \'w\')\n        f.close()\n        print(\'Bravo ! Le code fourni a passé les tests avec succès, il semble valide !\')'}}})</script>


````{admonition} Cliquez ici pour voir la solution
:class: tip, dropdown

```python
def affichage_bienvenue():
  # Codez votre fonction ici (et affichez le message de bienvenue !)
  print('Bienvenue')
```
````
