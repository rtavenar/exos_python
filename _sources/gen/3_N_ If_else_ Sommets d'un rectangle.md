# 3.N. If/else: Sommets d'un rectangle

## **Énoncé**

Étant données les coordonnés de 3 des sommets d'un rectangle dont les côtés sont parallèles aux axes du repère, afficher les coordonnées du quatrième sommet.




## Exemple #1

```
1
5
7
5
1
10
```

les 3 sommets sont (1, 5), (7, 5), (1, 10)

## Exemple de sortie #1

```
7
10
```

## Exemple d'entrée #2

```
1
5
7
10
1
10
```

## Exemple de sortie #2

```
7
5
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
x2 = int(input())
y2 = int(input())
x3 = int(input())
y3 = int(input())

if x1 == x2:
  x4 = x3
elif x1 == x3:
  x4 = x2
else:
  x4 = x1
  
if y1 == y2:
  y4 = y3
elif y1 == y3:
  y4 = y2
else:
  y4 = y1
  
print(x4)
print(y4)
```
````
