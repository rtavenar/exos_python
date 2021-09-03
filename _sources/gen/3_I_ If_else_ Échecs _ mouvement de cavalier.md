# 3.I. If/else: Échecs : mouvement de cavalier

## **Énoncé**

Aux échecs, un cavalier se déplace en "L" : de deux cases dans une direction puis d'une case dans une direction perpendiculaire à la première.

Votre programme recevra une position de départ (une valeur pour la colonne, une pour la ligne) et une position d'arrivée (une valeur pour la colonne, une pour la ligne) et devra afficher OUI si un roi peut se déplacer de la position de départ à celle d'arrivée et NON sinon.




## Exemple d'entrée

```
2
4
3
2
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

dx = abs(x1 - x2)
dy = abs(y1 - y2)

if dx == 1 and dy == 2 or dx == 2 and dy == 1:
  print('OUI')
else:
  print('NON')
```
````
