# 3.5. If/else: Un seul positif

## **Énoncé**

Étant donnés deux entiers non nuls, affichez "OUI" si l'un des deux est positif (mais pas les deux) et "NON" sinon.

## Exemple d'entrée #1

```
-5
10
```

## Exemple de sortie #1

```
OUI
```

## Exemple d'entrée #2

```
5
10
```

## Exemple de sortie #2

```
NON
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
if a > 0 and b < 0 or a < 0 and b > 0:
  print('OUI')
else:
  print('NON')
```
````
