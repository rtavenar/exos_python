# D.5. Objet : utilisation d'une méthode sans paramètre

## Consignes

Écrire le code permettant de créer un objet de classe Cercle nommé "monCercle", avec un rayon de 20 et les valeurs par défaut pour les positions en X et Y du centre. Créer une variable "surface" contenant le résultat du calcul de la surface de l'objet "monCercle". Pour obtenir ce résultat vous devez utiliser uniquement l'objet monCercle créé sans écrire vous-même le calcul de la surface.

## Aide

https://docs.python.org/fr/3.6/tutorial/classes.html#a-first-look-at-classes

<div id="pad"></div>
            <script>Pythonpad('pad', {'id': 'D.5.', 'title': 'Testez votre solution ici', 'src': 'from math import pi\n\nclass Cercle:\n  def __init__(self, r=15, posX=0, posY=0):\n    self.rayon = r\t\t# attribut rayon du cercle\n    self.x = posX\t\t\t# attribut position en X du centre du cercle\n    self.y = posY\t\t\t# attribut position en Y du centre du cercle\n  \n  def calculerSurface(self):\n    return pi*self.rayon**2\n  \n# Écrire votre code ci-dessous\n\n', 'files': {'.grader.py': {'type': 'text', 'body': 'import unittest\n\nclass TestExercise(unittest.TestCase):\n    def test_all(self):\n        self.assertIsInstance(monCercle, object)\n\nif __name__ == \'__main__\':\n    try:\n        from main import *\n    except:\n        print("Le code fourni n\'est pas valide")\n    suite = unittest.TestLoader().loadTestsFromTestCase(TestExercise)\n    output = unittest.TextTestRunner(verbosity=2).run(suite)\n\n    if output.wasSuccessful():\n        f = open(\'.passed.json\', \'w\')\n        f.close()\n        print(\'Bravo ! Le code fourni a passé les tests avec succès, il semble valide !\')'}}})</script>


````{admonition} Cliquez ici pour voir la solution
:class: tip, dropdown

```python
from math import pi

class Cercle:
  def __init__(self, r=15, posX=10, posY=10):
    self.rayon = r		# attribut rayon du cercle
    self.x = posX			# attribut position en X du centre du cercle
    self.y = posY			# attribut position en Y du centre du cercle
  
  def calculerSurface(self):
    return pi*self.rayon**2
    
# Écrire votre code ci-dessous
monCercle = Cercle(20)
surface = monCercle.calculerSurface()
```
````
