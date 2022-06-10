# 6.4. While: Course à pied

## **Énoncé**

Vous êtes un athlète qui se prépare pour une course. Le premier jour de votre entrainement, vous courez _x_ kilomètres, et le jour de la course vous devrez être capable de courir _y_ kilomètres.

Écrivez un programme qui lit les nombres x et y dans cet ordre et affiche le nombre de jours d'entrainements requis pour atteindre le but y sachant que vous augmentez votre distance d'entrainement  10% chaque jour.

## **Exemple d'entrée**

```
10
30
```

## **Exemple de sortie**

```
13
```

## Aide

https://rtavenar.github.io/poly_python/content/struct.html#boucles-while

<div id="pad"></div>
            <script>Pythonpad('pad', {'id': '6.4.', 'title': 'Testez votre solution ici', 'src': '# Read an integer:\n# a = int(input())\n# Print a value:\n# print(a)\n'})</script>


````{admonition} Cliquez ici pour voir la solution
:class: tip, dropdown

```python
x = int(input())
y = int(input())
num_days = 1
while x < y:
  x *= 1.1
  num_days += 1
print(num_days)
```
````
