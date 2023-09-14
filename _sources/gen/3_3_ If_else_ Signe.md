# 3.3. If/else: Signe

## Énoncé

Étant donné un entier, afficher `1` s'il est positif, `-1` s'il est négatif, ou `0` s'il est nul.

Essayez d'utiliser la syntaxe `if-elif-else` pour cela.

## Exemple d'entrée

```
179
```

## Exemple de sortie

```
1
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
x = int(input())
if x > 0:
  print(1)
elif x < 0:
  print(-1)
else:
  print(0)
```
````
