# 3.H. If/else: Échecs : mouvements de reine

## **Énoncé**

Aux échecs, une reine peut se déplacer horizontalement, verticalement et en diagonale d'un nombre quelconque de cases.

Votre programme recevra une position de départ (une valeur pour la colonne, une pour la ligne) et une position d'arrivée (une valeur pour la colonne, une pour la ligne) et devra afficher OUI si une reine peut se déplacer de la position de départ à celle d'arrivée et NON sinon.






## Exemple d'entrée

```
1
1
2
2
```

## Exemple de sortie

```
OUI
```

## Aide

https://rtavenar.github.io/poly_python/content/struct.html#structures-de-controle

## Codez votre solution ci-dessous

<py-config>
    [splashscreen]
        enabled = false
</py-config>
<py-repl>
    # Lire un entier :
# a = int(input())
# Afficher une valeur :
# print(a)
</py-repl>
<py-terminal id="my-terminal"></py-terminal>
<py-script>
from js import document as _DOC
def clear_term():
    ter = _DOC.getElementById("my-terminal").firstChild
    ter.innerHTML = ''
</py-script>
<button py-click="clear_term()" id="clear-terminal" class="py-button">Nettoyer la console de sortie</button>


````{admonition} Cliquez ici pour voir la solution
:class: tip, dropdown

```python
x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())

if x1 == x2 or y1 == y2 or abs(x1 - x2) == abs(y1 - y2):
  print('OUI')
else:
  print('NON')
```
````
