# 3.C. If/else: Échecs : mouvement de tour

## **Énoncé**

Aux échecs, les tours se déplacent horizontalement ou verticalement, d'un nombre de cases quelconque.

Le programme reçoit 4 valeurs entre 1 et 8 dans l'ordre suivant :

1. numéro de colonne de la case de départ
2. numéro de ligne de la case de départ
3. numéro de colonne de la case d'arrivée
4. numéro de ligne de la case d'arrivée

Le programme devra afficher `OUI` si une tour peut aller de la case de départ à la case d'arrivée ou `NON` sinon.



## **Exemple d'entrée**

```
4
4
5
5
```

## **Exemple de sortie**

```
NON
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

if x1 == x2 or y1 == y2:
  print('OUI')
else:
  print('NON')
```
````