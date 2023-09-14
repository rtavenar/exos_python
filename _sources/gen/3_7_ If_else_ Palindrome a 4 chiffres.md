# 3.7. If/else: Palindrome à 4 chiffres

## **Énoncé**

Étant donné un nombre à 4 chiffres, affichez "OUI" si c'est un palindrome (c'est-à-dire qu'on obtient la même valeur en le lisant de droite à gauche ou de gauche à droite) et "NON" sinon.

## Exemple d'entrée #1

```
1221
```

## Exemple de sortie #1

```
OUI
```

## Exemple d'entrée #2

```
1234
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
x = int(input())
milliers = x // 1000
centaines = x // 100 % 10
dizaines = x // 10 % 10
unites = x % 10
if milliers == unites and centaines == dizaines:
  print('OUI')
else:
  print('NON')
```
````
