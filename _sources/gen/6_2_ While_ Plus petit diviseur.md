# 6.2. While: Plus petit diviseur

## **Énoncé**

Étant donné un entier strictement plus grand que 1, afficher son plus petit diviseur strictement supérieur à 1.

## **Exemple d'entrée**

```
15
```

## **Exemple de sortie**

```
3
```

## Aide

https://rtavenar.github.io/poly_python/content/struct.html#boucles-while

## Codez votre solution ci-dessous

<py-config>
    [splashscreen]
        enabled = false
</py-config>
<py-repl>
    # Read an integer:
# a = int(input())
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
a = int(input())
i = 2
while a % i != 0:
  i += 1
print(i)
```
````
