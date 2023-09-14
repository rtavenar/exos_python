# 7.6. Lists: Nombre d'éléments distincts

## Consigne

À partir d'une liste de nombres entiers donnés en entrée (chaque nombre est séparé par un espace), avec tous les élements classés par ordre croissant, déterminer et afficher le nombre d'éléments distincts.

## Exemple d'entrée

```
1 2 2 3 3 3
```

## Exemple de sortie

```
3
```

## Aide

https://rtavenar.github.io/poly_python/content/listes.html

https://docs.python.org/fr/3/tutorial/datastructures.html#more-on-lists

## Codez votre solution ci-dessous

<py-config>
    [splashscreen]
        enabled = false
</py-config>
<py-repl>
    # Read a list of integers:
# a = [int(s) for s in input().split()]
# Print a value:
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
num_distinct = 1
a = [int(s) for s in input().split()]
for i in range(1, len(a)):
  if a[i - 1] != a[i]:
    num_distinct += 1
print(num_distinct)
```
````
