# 3.M. If/else: Minimum de 5 nombres

## **Énoncé**

Étant donnés 5 nombres, afficher leur minimum.

## Exemple d'entrée

```
10
20
30
40
50
```

## Exemple de sortie

```
10
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
least = int(input())

new_integer = int(input())
if new_integer < least:
  least = new_integer

new_integer = int(input())
if new_integer < least:
  least = new_integer
  
new_integer = int(input())
if new_integer < least:
  least = new_integer
  
new_integer = int(input())
if new_integer < least:
  least = new_integer
  
print(least)
```
````
