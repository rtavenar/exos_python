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
            <script>Pythonpad('pad', {'id': 'B.2', 'title': 'Testez votre solution ici', 'src': 'def affichage_bienvenue():\n  # Codez votre fonction ici (et affichez le message de bienvenue !)'})</script>


````{admonition} Cliquez ici pour voir la solution
:class: tip, dropdown

```python
def affichage_bienvenue(prenom):
  # Codez votre fonction ici (et affichez le message de bienvenue !)
  print('Bienvenue '+ prenom)
```
````
