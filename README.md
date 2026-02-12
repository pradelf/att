# Bloc4

[TOC]

# Contexte

Ce projet est à réaliser pour valider partiellement la certification _Data Science - Fullstack : Certification RNCP35288 CDSD_ avec le bloc 4.  

**Bloc 4 - Analyse prédictive de données non-structurées par l'intelligence artificielle**

- Traiter des données non-structurées (image, texte, audio) par la création de fonction de traitements via l'utilisation de librairies de programmation comme TensorFlow ou Numpy pour les transformer en matrices afin de les rendre interprétables par un algorithme d'apprentissage automatique profond (Deep learning en anglais)
- Élaborer des réseaux de neurones adaptés (classiques, convolutifs ou recursifs) en superposant des couches neuronales via des librairies de programmation comme TensorFlow pour analyser des données non-structurées afin de détecter des signaux sur ces dernières
- Créer un algorithme robuste et précis en configurant un réseau de neurones pré-entrainé profond afin de répondre à des problématiques de prédiction sur des volumes de données massifs
- Créer des données non-structurées en élaborant des réseaux de neurones adverses afin de construire de nouvelles bases d'entrainement pour des applications d'intelligence artificielle
- Évaluer la performance d'un algorithme d'apprentissage automatique profond en évaluant des indicateurs sur des données d'entrainement et de validation afin d'industrialiser son utilisation

# AT&T Spam Detector

<img src="https://full-stack-assets.s3.eu-west-3.amazonaws.com/M08-deep-learning/AT%26T_logo_2016.svg" alt="AT&T LOGO" width="50%" />

## Présentation de l’entreprise 📇

AT&T Inc. est une entreprise multinationale américaine de télécommunications, dont le siège est situé à la Whitacre Tower, dans le centre-ville de Dallas, au Texas.  
C’est la plus grande entreprise de télécommunications au monde en termes de chiffre d’affaires et le troisième plus grand fournisseur de services de téléphonie mobile aux États-Unis.  

En 2022, AT&T était classée **13ᵉ** au classement Fortune 500 des plus grandes entreprises américaines, avec un chiffre d’affaires de **168,8 milliards de dollars** 😮

---

## Projet 🚧

L’un des principaux points de douleur rencontrés par les utilisateurs d’AT&T est leur exposition constante aux **messages SPAM**.

AT&T a, pendant un temps, été capable de signaler manuellement les messages indésirables, mais l’entreprise recherche désormais une **solution automatisée** permettant de détecter les spams afin de mieux protéger ses utilisateurs.

---

## Objectifs 🎯

Ton objectif est de construire un **détecteur de spam** capable de signaler automatiquement les messages indésirables au moment où ils arrivent, en se basant **uniquement sur le contenu des SMS**.

---

## Périmètre du projet 🖼️

Pour commencer, AT&T souhaite que tu utilises le jeu de données suivant :

<ins>Télécharger le jeu de données</ins>

---

## Aides 🦮

Pour t’aider à mener ce projet à bien, voici quelques conseils utiles :

### Commencer simplement

Un bon modèle de deep learning n’a pas nécessairement besoin d’être extrêmement complexe !

### Transfer learning

Tu n’as pas accès à une très grande quantité de données. Exploiter la puissance d’un modèle plus sophistiqué, entraîné sur des milliards d’observations, pourrait donc être une bonne approche.

---

## Livrables 📬

Pour valider ce projet, ton équipe devra :

- Rédiger un notebook qui effectue le prétraitement des données et entraîne un ou plusieurs modèles de deep learning afin de prédire si un SMS est un spam ou non (ham)
- Présenter clairement les performances obtenues

&nbsp;

---

## Prérequis

- Python 3.12.1

---

## Processus envisagé pour le projet : AT&T

Pour un projet comme AT&T, le déroulement pourrait être le suivant :

- [x] Trouver un bon modèle LLM capable de gérer la détection de spam  
- [x] L’entraîner et l’améliorer à l’aide des données disponibles  
- [x] Tester et comparer les performances avec les meilleurs modèles disponibles sur Hugging Face  

---

## Objectifs concrets

### Quels outils dois-tu utiliser ?

- Lightning AI pour l’entraînement et le fine-tuning des modèles a été choisi pour des raisons économiques et de performance (GPU à la demande)

### Quels processus dois-tu mettre en place ?

- Sélection d’un modèle pré-entraîné  
- Fine-tuning du ou des modèles  
- Évaluation des performances  

### À quelles questions dois-tu répondre ?

- Spam ou ham ? Telle est la question.

### Quels problèmes dois-tu résoudre ?

- Nettoyage et préparation des données  
- Fine-tuning du modèle (l'enfer des typages entre scikit-learn, Pytorch, Python)

### Quels fichiers spécifiques dois-tu rendre pour la certification ?

- Un notebook  
- Un court rapport présentant les résultats de l’évaluation des modèles

___

## Artefacts

L'énoncé du projet est donné dans le notebook : [01-AT&T_spam_detector.ipynb](./01-AT&T_spam_detector.ipynb).  
Pour le rendu, il faut se reporter au notebook : [01-AT&T_spam_detector_FPr.ipynb](./01-AT&T_spam_detector_FPr.ipynb).  

## Rapport court

Le rapport de ce projet dans un fichier séparé : [rapport.md](./rapport.md)
