# D.8. Objet : définition d'une méthode d'instance

## Consignes

Écrire le code permettant de définir une classe Personne et son initialisateur. Les objets de classe Personne possèderont des attributs "`nom`", "`age`", "`poids`" et "`taille`" dont les valeurs seront passées en paramètres à la construction de l'objet (dans cet ordre). Le poids sera donné en kilogrammes et la taille en mètres.

Ajouter à la classe Personne une méthode d'instance nommée "`imc`" permettant de calculer et de retourner l'IMC (Indice de Masse Corporelle) de la personne. L'IMC d'une personne est égal à son poids (en kilogrammes) divisé par le carré de sa taille (en mètres).

## Aide

https://docs.python.org/fr/3.6/tutorial/classes.html#a-first-look-at-classes

<div id="pad"></div>
            <script>Pythonpad('pad', {'id': 'D.8.', 'title': 'Testez votre solution ici', 'src': '# Écrire votre code ci-dessous\n', 'files': {'.grader.py': {'type': 'text', 'body': 'import unittest\n\nclass TestExercise(unittest.TestCase):\n    def test_all(self):\n        self.assertIsInstance(Personne,type)\n\nif __name__ == \'__main__\':\n    try:\n        from main import *\n    except:\n        print("Le code fourni n\'est pas valide")\n    suite = unittest.TestLoader().loadTestsFromTestCase(TestExercise)\n    output = unittest.TextTestRunner(verbosity=2).run(suite)\n\n    if output.wasSuccessful():\n        f = open(\'.passed.json\', \'w\')\n        f.close()\n        print(\'Bravo ! Le code fourni a passé les tests avec succès, il semble valide !\')'}}})</script>


````{admonition} Cliquez ici pour voir la solution
:class: tip, dropdown

```python
# Écrire votre code ci-dessous
class Personne:
  def __init__(self, nom, age, poids, taille):
    self.nom = nom
    self.age = age
    self.poids = poids
    self.taille = taille
  
  def imc(self):
    return self.poids/(self.taille**2)
```
````
