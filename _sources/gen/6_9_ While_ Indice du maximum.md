# 6.9. While: Indice du maximum

## **Énoncé**

Étant donnée une séquence d'entiers positifs, où chaque entier est écrit sur une ligne distincte, affichez la position de la première occurrence du maximum des valeurs lues **avant** de rencontrer un 0 (on supposera que le 0 ne se trouve pas en première position).

## **Exemple d'entrée**

```
1
7
9
5
0
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
maximum = a = int(input())
maximum_index = 1
i = 1
while a != 0:
  a = int(input())
  i += 1
  if a > maximum:
    maximum = a
    maximum_index = i
print(maximum_index)
```
````
