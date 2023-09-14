# 6.C. While: Deuxième plus grande valeur

## **Énoncé**

Étant donnée une séquence d'entiers positifs, où chaque entier est écrit sur une ligne distincte, affichez la deuxième plus grande valeur lue **avant** de rencontrer un 0 (on supposera que le 0 ne se trouve pas en première ni en deuxième position).

## **Exemple d'entrée**

```
1
7
9
0
```

## Exemple de sortie

```
7
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
maximum = int(input())
second_maximum = int(input())
if second_maximum > maximum:
  second_maximum, maximum = maximum, second_maximum
a = -1
while a != 0:
  a = int(input())
  if a > maximum:
    second_maximum, maximum = maximum, a
  elif a > second_maximum:
    second_maximum = a
print(second_maximum)
```
````
