# 7.9. Lists: Inversion du min et du max

## Consigne

À partir d'une liste de nombres entiers distincts donnés en entrée (chaque nombre est séparé par un espace), inverser le minimum et le maximum et afficher la liste résultat.

## Exemple d'entrée

```
3 4 5 2 1
```

## Exemple de sortie

```
3 4 1 2 5
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
a = [int(s) for s in input().split()]
pos_min = a.index(min(a))
pos_max = a.index(max(a))
a[pos_min], a[pos_max] = a[pos_max], a[pos_min]
print(*a)
```
````
