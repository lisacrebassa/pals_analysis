# pals_analysis

🧬 Analyse stratégique des Pals – Palworld
🎯 Objectif
Optimiser l’expérience de jeu dans Palworld en analysant les attributs de combat, de production et de comportement des Pals.
Cette étude permet :

une meilleure stratégie de combat,

une gestion efficace des ressources au campement,

et une exploration plus fine des mécaniques du jeu.

🧩 Problématique
L'étude des caractéristiques et du comportement des Pals peut se montrer utile pour développer une expérience de jeu plus attrayante. En gros, une optimisation plus efficace de votre stratégie de jeu.

🛠️ Technologies utilisées
Python 3.11+

Pandas, Matplotlib, Seaborn : Analyse et visualisation

MySQL : Stockage relationnel

Streamlit : Application interactive

Jupyter Notebook : Exploration interactive

Google Slides : Présentation synthétique

📂 Datasets utilisés (nettoyés et enrichis)
Table	Contenu principal
combat_attribute	Attributs de combat de base des Pals
job_skill	Compétences de production et de travail
hidden_attribute	Statistiques comportementales et métadonnées
refresh_area	Zones et niveaux d’apparition
ordinary_boss_attribute	Stats des Pals BOSS standards
tower_boss_attribute	Stats des Pals BOSS des Tours

🔍 Analyses réalisées
🎮 Attributs de combat
Répartition des tailles, PV, catégories et raretés

Corrélations entre les attributs (attaque, défense, PV…)

Top 10 des Pals les plus puissants

Comparaison des puissances des Boss (Tower & Ordinary)

Impact de la taille sur la puissance

Influence de la rareté sur les attributs

🛠️ Compétences de production
Répartition des compétences de travail

Pals les plus polyvalents

Pals efficaces pour la production de ressources (œufs, laine…)

Analyse des Pals nocturnes (nuit vs jour)

Identification des Pals à haut rendement

🧠 Stratégies optimales
Équipes équilibrées recommandées (combat + production)

Stratégie de capture basée sur la probabilité

Répartition géographique des Pals (zones d'apparition)

Analyse des zones d’exploration stratégiques

📊 Visualisations
Les principaux graphiques sont exportés dans ./graphs/ :

distribution_taille_categorie.png

distribution_pv_rarete.png

top_competences.png

production_ranch.png

pals_nocturnes.png

top_capture_probability.png

correlation_attributs.png

taille_vs_puissance.png

repartition_zones.png

top_tower_boss.png

top_ordinary_boss.png

🌐 Application Streamlit
L'application interactive Streamlit permet de :

Naviguer dans les graphes et stats clés

Filtrer les Pals selon vos critères

Obtenir des recommandations en direct

📦 Lancer l’application :
bash
Copier
Modifier
streamlit run app.py
🗃️ Base de données SQL
Les tables sont créées et peuplées via Python (voir insert_data.py).
Modèle relationnel structuré pour les analyses croisées.

📈 Présentation finale
Une présentation Google Slides générée automatiquement depuis les visuels avec contextualisation est disponible pour accompagner une soutenance ou un rendu d’analyse.

💡 Pistes d'amélioration
Ajout de la météo et de l’heure dans les comportements

Calcul dynamique d’équipe selon objectif (exploration / combat / ferme)

Système de recommandation d’équipe auto-adaptatif

Intégration avec des mods ou l’API du jeu (si existant)

👥
Projet réalisé dans le cadre d’une analyse de données sur Palworld.

