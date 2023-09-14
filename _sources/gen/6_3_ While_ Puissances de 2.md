# 6.3. While: Puissances de 2

## **Énoncé**

Étant donné un entier X, on cherche le plus grand entier **n** pour lequel **2ⁿ** est inférieur ou égal à X. Affichez **n** et **2ⁿ**.


## **Exemple d'entrée**

```
50
```

## **Exemple de sortie**

```
5 32
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
x = int(input())
n = 1
while 2 ** n <= x:
  n += 1
print(n - 1, 2 ** (n - 1))
```
````
