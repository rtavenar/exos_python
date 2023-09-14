# 3.A. If/else: Nombres égaux

## **Énoncé**

Étant donnés 3 nombres, affichez combien sont égaux entre eux. Le programme devra écrire: 3 (si tous les nombres sont égaux), 2 (si deux d'entre eux sont égaux et que le troisième est différent) ou 0 (si tous les nombres sont différents).

## Exemple d'entrée

```
10
5
10
```

## Exemple de sortie

```
2
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
c = int(input())

if a == b and a == c:
  print(3)
elif a == b or a == c or b == c:
  print(2)
else:
  print(0)
```
````
