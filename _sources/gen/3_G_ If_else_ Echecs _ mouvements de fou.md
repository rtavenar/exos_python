# 3.G. If/else: Échecs : mouvements de fou

## **Énoncé**

Aux échecs, un fou se déplace en diagonale d'un nombre quelconque de cases.


Votre programme recevra une position de départ (une valeur pour la colonne, une pour la ligne) et une position d'arrivée (une valeur pour la colonne, une pour la ligne) et devra afficher OUI si un fou peut se déplacer de la position de départ à celle d'arrivée et NON sinon.



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

if abs(x1 - x2) == abs(y1 - y2):
  print('OUI')
else:
  print('NON')
```
````
