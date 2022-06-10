# D.7. Objet : définition d'une classe et de son initialisateur

## Consignes

Écrire le code permettant de définir une classe Personne et son initialisateur. Les objets de classe Personne possèderont un attribut "`nom`" dont la valeur sera passée en paramètre à la construction de l'objet.

## Aide

https://docs.python.org/fr/3.6/tutorial/classes.html#a-first-look-at-classes

<div id="pad"></div>
            <script>Pythonpad('pad', {'id': 'D.7.', 'title': 'Testez votre solution ici', 'src': '# Écrire votre code ci-dessous\n', 'files': {'.grader.py': {'type': 'text', 'body': 'import unittest\n\nclass TestExercise(unittest.TestCase):\n    def test_all(self):\n        self.assertIsInstance(Personne(\'toto\').__init__, types.MethodType)\n\nif __name__ == \'__main__\':\n    try:\n        from main import *\n    except:\n        print("Le code fourni n\'est pas valide")\n    suite = unittest.TestLoader().loadTestsFromTestCase(TestExercise)\n    output = unittest.TextTestRunner(verbosity=2).run(suite)\n\n    if output.wasSuccessful():\n        f = open(\'.passed.json\', \'w\')\n        f.close()\n        print(\'Bravo ! Le code fourni a passé les tests avec succès, il semble valide !\')'}}})</script>


````{admonition} Cliquez ici pour voir la solution
:class: tip, dropdown

```python
# Écrire votre code ci-dessous
class Personne:
  def __init__(self, nom):
    self.nom = nom
```
````
