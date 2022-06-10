# 5.9. Chaînes de caractères : remplacer

## Consignes

Étant donnée une chaîne de caractères entrée au clavier contenant au moins une fois le caractère `1`, remplacer dans cette chaîne tous les nombres `1` par le mot `one`.

## Exemple d'entré

```
1+1=2
```

## Exemple de sortie

```
one+one=2
```

## Aide

https://docs.python.org/fr/3.6/library/stdtypes.html#str.replace

<div id="pad"></div>
            <script>Pythonpad('pad', {'id': '5.9.', 'title': 'Testez votre solution ici', 'src': '# Lire une chaîne de caractères :\n# s = input()\n# Afficher une chaîne de caractères :\n# print(s)\n'})</script>


````{admonition} Cliquez ici pour voir la solution
:class: tip, dropdown

```python
print(input().replace('1', 'one'))
```
````
