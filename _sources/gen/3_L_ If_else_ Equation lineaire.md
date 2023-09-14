# 3.L. If/else: Équation linéaire

## **Énoncé**

Écrivez un programme qui résout une équation linéaire _ax = b_ pour des entiers.

Étant donné deux entiers _a_ et _b_ (_a_ pouvant valoir 0), affichez l'entier racine de l'équation s'il existe, "pas de solution" ou "multiples solutions" sinon.

## Exemple d'entrée #1

```
1
-2
```

## Exemple de sortie #1

```
-2
```

## Exemple d'entrée #2

```
2
-1
```

## Exemple de sortie #2

```
pas de solution
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

if a == 0:
  if b == 0:
    print('multiples solutions')
  else:
    print('pas de solution')
elif b % a == 0:
  print(b // a)
else:
  print('pas de solution')
```
````
