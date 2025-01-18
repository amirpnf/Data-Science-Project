# US Counties and States Comprehensive Health Analysis

### Amirhossein Pouyanfar - Lorenzo Bravard - E3FI 1I


#### User Guide

1. Prérequis  

Avant de lancer le programme, il est indispensable d'installer les packages et
outils nécessaires, qui sont utilisés dans ce dernier. Pour ce faire, il suffit d'exécuter 
cette commande dans un terminal ouvert dans le dossier DATA-SCIENCE-PROJECT :  
 
```bash
python -m pip install -r requirements.txt
```

Cela installera les outils requis pour la bonne exécution du programme final.

2. Exécuter le programme : 

Il suffit de taper cela dans un terminal ouvert dans le dossier DATA-SCIENCE-PROJECT:

```bash
python3 main.py
```

Le programme fonctionne également en mode *offline*.


#### Data

Les données utilisées dans ce programme proviennent des CDC (*Centers for Disease Control and Prevention*).
Les CDC constituent la principale agence fédérale des États-Unis chargée de la protection de la santé publique.

Les centres produisent des informations visant à éclairer et améliorer les décisions gouvernementales en matière de santé. Ils œuvrent également à la promotion de la santé grâce à des partenariats avec les départements de la santé des différents États américains et diverses organisations. Les CDC, qui relèvent du département de la Santé et des Services sociaux des États-Unis, ont leur siège dans le comté de DeKalb, près d'Atlanta, en Géorgie.

Le dataset que nous utilisons, dans sa forme raw (pas encore filtré et nettoyé), contient essentiellement la prévalence des maladies et syndromes 
différents à travers les États-Unis. Nous en avons choisi les principaux, notemment l'obésité, sur laquelle nous 
centrons notre conclusion plus bas.


#### Developer Guide

La structure du programme est organisée comme suit :

Les callbacks sont centralisés dans un fichier nommé callback.py. Ce fichier contient une fonction `init_callbacks()`, qui regroupe tous les callbacks et les active dans le programme principal.

Pour ajouter une nouvelle page ou un nouveau composant au programme, il faut suivre les étapes suivantes :

1. Définir le layout de la page : Il est recommandé de créer un fichier dans le répertoire pages/components pour y définir la structure de la page.

2. Créer la figure ou le squelette : La figure ou le composant visuel doit être défini dans un fichier séparé, placé dans le répertoire utils. Ce fichier doit contenir au moins une fonction qui retourne la figure ou le squelette final.

3. Intégrer le layout : Ajouter un div ou un row dans le fichier homepage.py pour y inclure le layout que vous venez de créer.

4. Créer le callback : Enfin, il faut définir le callback correspondant et l'ajouter dans le fichier callbacks.py, au sein de la fonction `init_callbacks()`.


Nous utilisons un fichier **config.py** qui permet de mettre toutes les configurations techniques et 
esthétiques du projet dans un seul endroit, facilitant ainsi le debugging, et la modification éventuelle
des sturctures. 


### Rapport d'analyse

Nos données traitaient des différentes pathologies touchant les citoyens américains. Certaines étaient bénignes, comme la perte de dents, tandis que d'autres étaient plus graves, comme l'obésité.

La première observation à souligner est le taux élevé d'obésité chez les Américains, atteignant jusqu'à 43% dans l'État du Mississippi.
Il est important de noter que les plus hauts taux d'obésité se situent à l'est, tandis que la partie ouest est quant à elle moins concernée.

Nous pouvons remarquer des tendances au niveau des pathologies. Un comté fortement touché par l'obésité aura un taux élevé de diabète ou de cholestérol, par exemple.

Mais nous avons également pu conclure que toutes les pathologies n'étaient pas liées et que certaines semblaient indépendantes. C'est le cas du cancer, qui n'a pas de tendance géographique réellement notable.


#### Copyright

Nous déclarons sur l'honneur que le code fourni dans ce projet a été intégralement produit par nous-même, à l'exception des lignes ou parties de code mentionnées ci-dessous. Chaque emprunt de code est accompagné de sa référence et d'une explication de la syntaxe utilisée.


1. Fonctions **generate_choropleth_map\***:

Source : Documentation officielle de Plotly Express (`https://plotly.com/python/choropleth-maps`)

Explication : Cette fonction a été adaptée à partir des exemples fournis dans la documentation de Plotly pour créer des cartes choroplèthes interactives. Les modifications incluent l'ajout de paramètres personnalisés tels que hover_data et color_continuous_scale.

2. Le code pour la gestion des callbacks :

Source : Documentation de Dash (`https://dash.plotly.com/basic-callbacks`)

Explication : La structure de base des callbacks a été inspirée par la documentation officielle de Dash, puis adaptée pour répondre aux besoins spécifiques du projet.


3. Fonction **draw_histogram**:

Source : Documentation officielle de Plotly Express (`https://plotly.com/python/histograms`)

Explication : Cette fonction a été adaptée à partir des exemples fournis dans la documentation de Plotly pour créer des histogrammes. Les modifications incluent l'ajout de paramètres personnalisés.

4. Fonction **plot_grouped_bar_chart**

Source : Documentation officielle de Plotly Express (`https://plotly.com/python/bar-charts/`)

Explication : Cette fonction a été adaptée à partir des exemples fournis dans la documentation de Plotly pour créer des bar charts. Les modifications incluent l'ajout de paramètres personnalisés.

*Toute ligne de code non déclarée ci-dessus est réputée être produite par nous-même. Nous nous engageons à respecter les règles de propriété intellectuelle et à citer toute source externe utilisée dans ce projet.*
