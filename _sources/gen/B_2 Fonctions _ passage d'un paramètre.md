# B.2 Fonctions : passage d'un paramètre

**Énoncé**

Codez une fonction affichage_bienvenue qui affiche le message "Bienvenue XXX" et ajoute le prénom d'une personne ('XXX'). La fonction prend en paramètre le prénom de la personne.

**Exemple d'appel de la fonction**

```
affichage_bienvenue('Régis')
```

**Exemple de sortie**

```
Bienvenue Régis
```

**Aide**

https://rtavenar.github.io/poly_python/content/struct.html#fonctions

<div id="pad"></div>
            <script>Pythonpad('pad', {'id': 'B.2', 'title': 'Testez votre solution ici', 'src': 'def affichage_bienvenue():\n  # Codez votre fonction ici (et affichez le message de bienvenue !)', 'files': {'.grader.py': {'type': 'text', 'body': 'import unittest\n\nclass TestExercise(unittest.TestCase):\n    def test_all(self):\n        self.assertIsInstance(affichage_bienvenue, types.FunctionType)\n\nif __name__ == \'__main__\':\n    try:\n        from main import *\n    except:\n        print("Le code fourni n\'est pas valide")\n    suite = unittest.TestLoader().loadTestsFromTestCase(TestExercise)\n    output = unittest.TextTestRunner(verbosity=2).run(suite)\n\n    if output.wasSuccessful():\n        f = open(\'.passed.json\', \'w\')\n        f.close()\n        print(\'Bravo ! Le code fourni a passé les tests avec succès, il semble valide !\')'}}})</script>


````{admonition} Cliquez ici pour voir la solution
:class: tip, dropdown

```python
def affichage_bienvenue(prenom):
  # Codez votre fonction ici (et affichez le message de bienvenue !)
  print('Bienvenue '+ prenom)
```
````
