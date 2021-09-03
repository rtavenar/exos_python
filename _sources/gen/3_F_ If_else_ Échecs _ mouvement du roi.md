# 3.F. If/else: Échecs : mouvement du roi

## **Énoncé**

Aux échecs, le roi se déplace d'une case dans n'importe quelle direction.

Votre programme recevra une position de départ (une valeur pour la colonne, une pour la ligne) et une position d'arrivée (une valeur pour la colonne, une pour la ligne) et devra afficher OUI si un roi peut se déplacer de la position de départ à celle d'arrivée et NON sinon.



## Exemple d'entrée

```
4
4
5
5
```

## Exemple de sortie

```
OUI
```

## Aide

https://rtavenar.github.io/poly_python/content/struct.html#structures-de-controle

<div id="pad"></div>
            <script>Pythonpad('pad', {'title': 'Testez votre solution ici', 'src': '# Lire un entier :\n# a = int(input())\n# Afficher une valeur :\n# print(a)\n'})</script>


````{admonition} Cliquez ici pour voir la solution
:class: tip, dropdown

```python
x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())

if abs(x1 - x2) <= 1 and abs(y1 - y2) <= 1:
  print('OUI')
else:
  print('NON')
```
````
