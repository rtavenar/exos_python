# 3.D. If/else: Échecs : case noire

## **Énoncé**

Étant donnés deux entiers indiquant une case de l'échiquier, affichez OUI si c'est une case noire (marron sur le dessin ci-dessous) ou NON sinon.



## **Exemple d'entrée** #1

```
1
1
```

## **Exemple de sortie** #1

```
OUI
```

## **Exemple d'entrée** #2

```
1
2
```

## **Exemple de sortie** #2

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
x1 = int(input())
y1 = int(input())

if (x1 + y1) % 2 == 0:
  print('OUI')
else:
  print('NON')
```
````
