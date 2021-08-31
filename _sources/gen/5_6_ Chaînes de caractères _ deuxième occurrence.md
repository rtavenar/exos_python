---
jupytext:
  formats: md:myst
  text_representation:
    extension: .md
    format_name: myst
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

# 5.6. Chaînes de caractères : deuxième occurrence

## Consignes

Étant donnée une chaîne de caractères entrée au clavier pouvant contenir la lettre `p`, `afficher l'indice de la deuxième occurrence de `p`. Si la lettre `p` n'apparait qu'une seule fois, afficher `-1`. Si la chaîne de caractères ne contient pas la lettre `p`, afficher `-2.``

## Exemple d'entrée #1

```
appropriate
```

## Exemple de sortie #1

```
2
```

## Exemple d'entrée #2

```
spare
```

## Exemple de sortie #2

```
-1
```

## Exemple d'entrée #3

```
reason
```

## Exemple de sortie #3

```
-2
```

## Aide

https://rtavenar.github.io/poly_python/content/intro.html#les-cha%C3%AEnes-de-caract%C3%A8res

https://docs.python.org/fr/3.6/library/stdtypes.html#common-sequence-operations

https://docs.python.org/fr/3.6/library/stdtypes.html#str.find
https://docs.python.org/fr/3.6/library/stdtypes.html#str.rfind

## Squelette

```{code-cell} ipython3

# Lire une chaîne de caractères :
# s = input()
# Afficher une chaîne de caractères :
# print(s)
# 
```

````{admonition} Cliquez ici pour voir la solution
:class: tip, dropdown

```python
s = input()
if 'p' in s:
  if s.find('p') == s.rfind('p'):
    print(-1)
  else:
    print(s.find('p') + s[s.find('p') + 1:].find('p') + 1)
else:
  print(-2)
```
````
