# 5.A. Chaînes de caractères : retirer un caractère

## Consignes

Étant donnée une chaîne de caractères entrée au clavier, retirer tous les caractères `@` de cette chaîne.

## Exemple d'entrée

```
Bilbo.Baggins@bagend.hobbiton.shire.me
```

## Exemple de sortie

```
Bilbo.Bagginsbagend.hobbiton.shire.me
```

## Aide

https://docs.python.org/fr/3.6/library/stdtypes.html#str.replace

<div id="pad"></div>
            <script>Pythonpad('pad', {'id': '5.A.', 'title': 'Testez votre solution ici', 'src': '# Lire une chaîne de caractères :\n# s = input()\n# Afficher une chaîne de caractères :\n# print(s)\n'})</script>


````{admonition} Cliquez ici pour voir la solution
:class: tip, dropdown

```python
print(input().replace('@', ''))
```
````
