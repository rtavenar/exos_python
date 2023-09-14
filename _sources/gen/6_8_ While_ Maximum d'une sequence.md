# 6.8. While: Maximum d'une séquence

## **Énoncé**

Étant donnée une séquence d'entiers positifs, où chaque entier est écrit sur une ligne distincte, affichez la plus grande valeur lue **avant** de rencontrer un 0 (on supposera que le 0 ne se trouve pas en première position).

## **Exemple d'entrée**

```
1
2
3
2
1
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
while a != 0:
  a = int(input())
  if a >= maximum:
    maximum = a
print(maximum)
```
````
