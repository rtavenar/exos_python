# 8.7. Listes 2D : damier

## Consignes

Étant donnés deux entiers positifs `n` et `m` entrés au clavier, créer une liste 2D de taille `n×m` et la remplir avec les caractères "`.`" et "`*`" alternés en ligne et en colonne afin d'obtenir un motif en damier. Le coin haut gauche du damier doit contenir le caractère "`.`" .

## Exemple d'entrée

```
6 8
```

## Exemple de sortie

```
. * . * . * . *
* . * . * . * .
. * . * . * . *
* . * . * . * .
. * . * . * . *
* . * . * . * .
```

## Aide

https://docs.python.org/fr/3.6/library/stdtypes.html#lists

https://docs.python.org/fr/3.6/tutorial/datastructures.html#list-comprehensions

https://docs.python.org/fr/3.6/tutorial/datastructures.html#nested-list-comprehensions

## Codez votre solution ci-dessous

<py-config>
    [splashscreen]
        enabled = false
</py-config>
<py-repl>
    # Lire une liste d'entiers :
# a = [int(s) for s in input().split()]
# Afficher la valeure de a :
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
n, m = [int(s) for s in input().split()]
a = [['.' if (i + j) % 2 == 0 else '*']
     for i in range(n)
     for j in range(m)]
for line in a:
  print(*line)
```
````
