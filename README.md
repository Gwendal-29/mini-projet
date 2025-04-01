
# Projet d'Analyse des Données - Cancer Oral

Ce projet consiste à analyser un jeu de données relatif au **cancer oral**. L'objectif est d'explorer les corrélations entre différentes variables du dataset, avec un accent particulier sur les facteurs comme le **tabagisme** et la **consommation d'alcool**. Le projet inclut également un test statistique pour analyser si fumer ou boire augmente les risques de cancer oral.

## Dépendances nécessaires

Avant de commencer, assurez-vous que vous avez installé les bibliothèques suivantes. Vous pouvez les installer via `pip` :

```
pip install pandas matplotlib seaborn scikit-learn scipy
```

### Liste des dépendances :
- **pandas** : Pour la manipulation des données.
- **matplotlib** et **seaborn** : Pour la visualisation des données (graphes et heatmap).
- **scikit-learn** : Pour l'encodage des variables catégorielles.
- **scipy** : Pour effectuer le test statistique de Chi-Carré.

## Étapes pour exécuter le projet

### 1. Télécharger le jeu de données
Téléchargez le fichier **oral_cancer_prediction_dataset.csv** et placez-le dans le même répertoire que ce script Python. Ce fichier contient les informations sur les caractéristiques des patients et la présence de cancer oral.

### 2. Exécuter le script
Lancez le script Python en utilisant la commande suivante dans votre terminal :

```
python projet.py
```

### 3. Résultats attendus
Le script effectue plusieurs analyses :

1. **Matrice de Corrélation :** Affichage d'une heatmap montrant les corrélations entre toutes les variables numériques du dataset.
2. **Corrélation avec la Présence du Cancer Oral :** Une liste des 10 variables les plus corrélées avec la présence du cancer oral et un graphique en barre visualisant ces corrélations.
3. **Test du Chi-Carré :** Test de l'association entre le **tabagisme** et la **consommation d'alcool** avec la présence de cancer oral. Les résultats du test du Chi-Carré sont affichés avec leurs **p-values**.

### 4. Interprétation des résultats
- Si la **p-value** du test du Chi-Carré est inférieure à **0.05**, cela signifie qu'il existe une association significative entre le facteur étudié (tabagisme ou alcool) et la présence de cancer oral.
- Le graphique de **corrélation** vous permet de visualiser les variables les plus influentes pour la présence de cancer oral.

## Structure du Projet

```
/oral_cancer_prediction_dataset.csv  # Le fichier CSV contenant les données
/projet.py                            # Le script Python d'analyse des données
README.md                           # Ce fichier README
```



