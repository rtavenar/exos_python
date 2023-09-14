# 6.A. While: Nombre d'éléments pairs

## **Énoncé**

Étant donnée une séquence d'entiers positifs, où chaque entier est écrit sur une ligne distincte, affichez le nombre de valeurs paires lues **avant** de rencontrer un 0.

## **Exemple d'entrée**

```
2
1
4
0
```

## **Exemple de sortie**

```
2
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
num_even = 0
while a != 0:
  if a % 2 == 0:
    num_even += 1
  a = int(input())
print(num_even)
```
````
