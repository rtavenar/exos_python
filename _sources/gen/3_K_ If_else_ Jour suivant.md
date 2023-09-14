# 3.K. If/else: Jour suivant

## **Énoncé**

Étant donnés un numéro de jour (entier entre 1 et 31) et un mois (entier entre 1 et 12) représentant à eux deux une date, vous afficherez la date du lendemain sous la forme d'un numéro de jour et d'un mois.

On supposera qu'il s'agit d'une date d'une année non bissextile.

## Exemple d'entrée #1

```
30
3
```

(30 Mars)

## Exemple de sortie #1

```
31
3
```

## Exemple d'entrée #2

```
31
3
```

(31 Mars)

## Exemple de sortie #2

```
1
4
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
jour = int(input())
mois = int(input())

if ((jour == 30) and (mois == 4 or mois == 6 or mois == 9 or mois == 11)
    or (jour == 28) and (mois == 2)
    or (jour == 31)):
  mois += 1
  jour = 1
else:
  jour += 1
if mois == 13:
  mois = 1

print(jour)
print(mois)
```
````