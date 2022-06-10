# D.7. Objet : définition d'une classe et de son initialisateur

## Consignes

Écrire le code permettant de définir une classe Personne et son initialisateur. Les objets de classe Personne possèderont un attribut "`nom`" dont la valeur sera passée en paramètre à la construction de l'objet.

## Aide

https://docs.python.org/fr/3.6/tutorial/classes.html#a-first-look-at-classes

<div id="pad"></div>
            <script>Pythonpad('pad', {'id': 'D.7.', 'title': 'Testez votre solution ici', 'src': '# Écrire votre code ci-dessous\n'})</script>


````{admonition} Cliquez ici pour voir la solution
:class: tip, dropdown

```python
# Écrire votre code ci-dessous
class Personne:
  def __init__(self, nom):
    self.nom = nom
```
````
