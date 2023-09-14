# 3.8. If/else: Minimum de 3 nombres

## **Énoncé**

Étant donnés trois entiers, affichez le plus petit des 3.

## Exemple d'entrée

```
5
3
7
```

## Exemple de sortie

```
3
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
a = int(input())
b = int(input())
c = int(input())

if a < b and a < c:
  print(a)
elif b < a and b < c:
  print(b)
else:
  print(c)
```
````
