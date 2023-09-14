# 6.6. While: Somme d'une séquence

## **Énoncé**

Étant donnée une séquence d'entiers positifs, où chaque entier est écrit sur une ligne distincte, affichez la somme des valeurs lues **avant** de rencontrer un 0.


## **Exemple d'entrée**

```
1
7
9
0
```

## **Exemple de sortie**

```
17
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
sum_of_sequence = 0
while a != 0:
  sum_of_sequence += a
  a = int(input())
print(sum_of_sequence)
```
````
