# Scripts et données pour la génération automatique de GH Page contenant les exos Python

## Structure

* `data/` contient les données extraites de <repl.it>
* `book/` contient la structure fixe du Jupyter Book (tout ce qui ne dépend pas du contenu de `data/`)
* `py/` contient les scripts Python nécessaires pour enrichir le Jupyter Book avec les exercices issus de <repl.it>
* `.github/` contient la GitHub Action qui :
  1. génère les fichiers Markdown à partir du contenu de `data/`
  2. compile le bouquin au format HTML 
  3. le publie sur GitHub Pages

## TODO list

* Ajouter un historique des exercices faits / pas faits / partiellement faits en utilisant le `localStorage` en JS. Peut se faire en :
  1. regardant pour quels exercices il y a une entrée du type "Pythonpad-save-files-C.2" dans le `localStorage`
  2. Parmi ceux-là, pour lesquels il y a un fichier `.passed.json` dans les fichiers listés dans le dictionnaire en question
  3. Afficher une icone simple verte disant que c'est fait (en utilisant https://fontawesome.com/v5/icons/check?style=solid&s=solid ?)
  4. On pourrait même avoir une icone orange pour les exercices en cours : ce sont ceux pour lesquels il y a une entrée "Pythonpad-save-src-C.2" dans le `localStorage`
* Vérifier le rendu visuel des blocs dans lequels on code sur plusieurs supports
* Implémenter les unit tests pour tester automatiquement une solution proposée
  * OK pour les unit tests, reste les input-output-matching
* Revoir un peu les exercices
* Question : comment implémenter ces améliorations ?
  * Option 1 : on s'y met à 3 sur qqs jours et on avance le + possible
  * Option 2 : on le propose comme projet extra-scolaire à un petit groupe d'étudiants triés sur le volet
  * Option 3 : on fait une sorte de hackathon, impliquant possiblement des étudiants, profs, etc, et qui soit ouvert à de plus larges améliorations
