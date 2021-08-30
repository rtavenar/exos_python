# Scripts et données pour la génération automatique de GH Page contenant les exos Python

## Structure

* `data/` contient les données extraites de <repl.it>
* `book/` contient la structure fixe du Jupyter Book (tout ce qui ne dépend pas du contenu de `data/`)
* `py/` contient les scripts Python nécessaires pour enrichir le Jupyter Book avec les exercices issus de <repl.it>
* `.github/` contient la GitHub Action qui :
  1. génère les fichiers Markdown à partir du contenu de `data/`
  2. compile le bouquin au format HTML 
  3. le publie sur GitHub Pages
