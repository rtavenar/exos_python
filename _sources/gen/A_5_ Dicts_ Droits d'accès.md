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

# A.5. Dicts: Droits d'accès

## Consigne

Un virus a attaqué le système de fichiers d'un superordinateur et a brisé le contrôle des droits d'accès aux fichiers. Pour chaque fichier, il existe un ensemble connu d'opérations qui peuvent lui être appliquées:


- write W (ecriture),
- read R (lecture),
- execute X (exécution)


La première ligne contient le nombre N (le nombre de fichiers contenus dans le système de fichiers). Les N lignes suivantes contiennent les noms des fichiers et les opérations autorisées sur eux, séparés par des espaces. La ligne suivante contient un entier M (le nombre d'opérations sur les fichiers). Dans les M lignes suivantes, spécifiez les opérations demandées pour les fichiers. Un fichier peut être demandé plusieurs fois.

Vous devez récupérer le contrôle sur les droits d'accès aux fichiers. Pour chaque requête, votre programme doit retourner "OK" si l'opération demandée est valide ou "Access denied" si l'opération n'est pas valide.

## Exemple d'entrée

```
4
helloworld.exe R X
pinglog W R
nya R
goodluck X W R
5
read nya
write helloworld.exe
execute nya
read pinglog
write pinglog
```

## Exemple de sortie

```
OK
Access denied
Access denied
OK
OK
```

## Theory

https://rtavenar.github.io/poly_python/content/dict.html

https://docs.python.org/fr/3/tutorial/datastructures.html#dictionaries

## Squelette

```{code-cell} ipython3

# Read a string:
# s = input()
# Print a value:
# print(s)
# 
```

````{admonition} Cliquez ici pour voir la solution
:class: tip, dropdown

```python
ACTION_TO_RIGHT = {
  'read': 'R',
  'write': 'W',
  'execute': 'X',
}

file_rights = {}
for _ in range(int(input())):
  filename, *rights = input().split()
  file_rights[filename] = set(rights)
for _ in range(int(input())):
  action, filename = input().split()
  if ACTION_TO_RIGHT[action] in file_rights[filename]:
    print('OK')
  else:
    print('Access denied')
```
````
