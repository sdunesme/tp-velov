# Python pour les géographes - TP Vélo'V
Ces travaux pratiques s'articulent en objectifs à atteindre. Un notebook est disponible pour chaque objectif. Vous y trouverez :
- Un petit cahier des charges des attendus
- Des éléments d'aide qui vous permettrons d'avancer

La première étape pour chaque objectif est de définir un algorithme qui permettra de réaliser l'objectif. Il n'existe pas un seul et unique algorithme et il n'y a pas de mauvaise solution tant que votre solution répond aux attentes. Il existe cependant des solutions plus optimales que d'autres. 

Une fois que vous avez une bonne vision de comment va s'articuler votre code, vous pouvez commencer à coder. Gardez bien en tête que l'algorithme n'est pas figé. Si vous êtes coincé quelque part, vous pouvez toujours changez de façon de faire, prendre un chemin de traverse pour débloquer la situation.

Toutes les ressources externes sont autorisées : 
- Les documentations officielles
  - [Python](https://docs.python.org/3/)
  - [pandas](https://pandas.pydata.org/docs/reference/index.html)
  - [geopandas](https://geopandas.org/en/stable/docs.html)
  - [shapely](https://shapely.readthedocs.io/en/stable/manual.html)
  - [rasterio](https://rasterio.readthedocs.io/en/stable/)
- Google
- StackOverflow
- Wikipedia
- ChatGPT
- La [pandas cheatsheet](https://pandas.pydata.org/Pandas_Cheat_Sheet.pdf)
- etc.

Le but de ce TP est de vous apprendre à rechercher vous-même des solutions techniques pour répondre aux attentes d'un cahier des charges. 

Vous pouvez rédiger votre code dans des notebook jupyter si vous en avez l'habitude, mais je vous encourage à plutôt rédiger des fichiers .py bien commentés. Placez tout votre code dans le dossier ```scripts```.

## Principaux packages étudiés
### pandas et geopandas

> pandas is a fast, powerful, flexible and easy to use open source data analysis and manipulation tool, built on top of the Python programming language.

Le package geopandas ajoute à pandas la gestion des géométries spatiales et un certain nombre de méthodes pour réaliser les opérations SIG les plus courantes. Techniquement, il utilise *shapely* pour la gestion des géométries.

### shapely

> Shapely is a Python package for set-theoretic analysis and manipulation of planar features using functions from the well known and widely deployed GEOS library. 

Quelques connaissances sur le fonctionnement de shapely sont indispensables pour pouvoir manipuler confortablement les données vectorielles de geopandas.

### rasterio

> Geographic information systems use GeoTIFF and other formats to organize and store gridded raster datasets such as satellite imagery and terrain models. Rasterio reads and writes these formats and provides a Python API based on Numpy N-dimensional arrays and GeoJSON.

Rasterio permet d'utiliser les librairies GDAL pour ouvrir, lire et écrire des données raster de façon bien plus conviviale que la librairie GDAL elle-même. 

## Démarrage rapide
### Accès aux supports de cours

Les supports de cours sont accessible via JupyterLite à l'addresse https://sdunesme.github.io/tp-velov.
Vous pouvez directement développer vos scripts dans cette interface, mais il est recommandé d'installer plutôt un environnement virtuel local sur votre machine.

### Installer dans un environnement virtuel avec pip (recommandé)
#### Windows
```powershell
# Installation initiale
python3.exe -m venv env --prompt tp-velov
./env/Scripts/activate
pip install -U pip
pip install -r requirements.txt

# Lancement du jupyter-lab
./env/Scripts/activate
jupyter-lab
```

#### Unix
```bash
# Installation initiale
python3 -m venv env --prompt tp-velov
source env/bin/activate
pip install -U pip
pip install -r requirements.txt

# Lancement du jupyter-lab
source env/bin/activate
jupyter-lab
```

### Installer dans un environnement virtuel avec conda
Les commandes suivantes sont à lancer dans un prompt Anaconda. 

```bash
# Installation initiale
conda create -y -n tp-velov 
conda activate tp-velov
conda install -y -c conda-forge rasterio geopandas jupyterlab

# Lancement du jupyter-lab
conda activate tp-velov
jupyter-lab
```

## Objectif 1 - Données Vélo'V

- Récupérer les données ponctuelles des stations Vélo'V avec leurs attributs en direct
- Transformer ces données en objets SIG

## Objectif 2 - Zone de desserte

- Définir la zone dans laquelle au moins un vélo est disponible à moins de 500m
- Exporter cette zone au format vectoriel

## Objectif 3 - Raster du vélo le plus proche

- Cartographier la distance à vol d'oiseau au vélo disponible le plus proche
- Exporter cette carte au format raster

## Objectif 4 - Raster du nombre de vélos dispo dans un rayon de 500m

- Cartographier le nombre de vélos disponibles dans un rayon de 500m
- Exporter cette carte au format raster

# Quelques idées pour continuer
## Fonction actualisation des données
Plutôt que de charger le tableau des stations pour créer les cartes des objectifs 3 et 4, écrire une fonction permettant de récupérer directement les données actualisées sur l'API au moment de créer la carte.

## Vectoriser les zones de haute disponibilité
En utilisant la carte du nombre de vélos dans un rayon de 500m, vectoriser les zones avec plus de 50 vélos disponibles dans un rayon de 500m.

## Refaire le TP avec les données historiques
Les données historiques de la disponibilité de vélos est disponible via une [API dédiée](https://data.grandlyon.com/portail/fr/jeux-de-donnees/stations-velo-v-de-la-metropole-de-lyon---disponibilites-temps-reel/info). Utiliser cette API pour réaliser l'exercice suivant : 
- Choisir un jour de la semaine.
- Récupérer des données de façon à constituer un jeu de données complètes toutes les 2h, de 6h à 18h.
- Réaliser une boucle pour exporter une des deux cartes des objectifs 1 et 2 en utilisant ces jeux de données.

Ces cartes devraient permettre d'illustrer des dynamiques de mouvements pendulaires.
