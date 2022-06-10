# 5.2. Chaînes de caratères : nombre de mots

## Consignes

Étant donnée une chaîne de caractères (entrée au clavier) représentant des mots séparés par des espaces, déterminer le nombre de mots la composant. Pour résoudre le problème, utiliser la méthode `split` des chaînes de caractères.

## Exemple d'entrée

```
Hello world
```

## Exemple de sortie

```
2
```

## Aide

https://rtavenar.github.io/poly_python/content/intro.html#les-cha%C3%AEnes-de-caract%C3%A8res

https://docs.python.org/fr/3.6/library/stdtypes.html#str.split

<div id="pad"></div>
            <script>Pythonpad('pad', {'id': '5.2.', 'title': 'Testez votre solution ici', 'src': '# Lire une chaîne de caractères :\n# s = input()\n# Afficher une chaîne de caractères :\n# print(s)\n'})</script>


````{admonition} Cliquez ici pour voir la solution
:class: tip, dropdown

```python
print(len(input().split()))
```
````
