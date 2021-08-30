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

# 5.8. Chaînes de caratères : inverser une partie

## Consignes

Étant donnée une chaîne de caractères entrée au clavier contenant au moins deux fois la lettre `h`, inverser la séquence de caractères se trouvant entre la première et la dernière occurrence de `h`.

## Exemple d'entrée

```
In the hole in the ground there lived a hobbit
```

## Exemple de sortie

```
In th a devil ereht dnuorg eht ni eloh ehobbit
```

## Aide

https://docs.python.org/fr/3.6/library/stdtypes.html#common-sequence-operations

https://docs.python.org/fr/3.6/library/stdtypes.html#str.find

https://docs.python.org/fr/3.6/library/stdtypes.html#str.rfind

## Squelette

```{code-cell} python
# Lire une chaîne de caractères :
# s = input()
# Afficher une chaîne de caractères :
# print(s)
```

````{dropdown} Proposition de solution

```python
s = input()
first_pos, last_pos = s.find('h') + 1, s.rfind('h')
left, middle, right = s[:first_pos], s[first_pos:last_pos], s[last_pos:]
print(left + middle[::-1] + right)
```
````
