# 10 — Pistes d'évolution

Le projet a été conçu dès le départ pour grandir par étapes. Voici des
pistes concrètes, dans un ordre de complexité croissante.

## V2 — Son et voix

**Matériel à ajouter** : petit haut-parleur USB ou mini ampli + haut-parleur
sur GPIO (I2S), ~10-15€.

**Logiciel** : librairie `pyttsx3` (hors-ligne) ou `espeak-ng` pour la
synthèse vocale en français. Nouveau module `voice.py` avec une méthode
`say(text)`, appelée depuis `main.py` aux moments clés (ex: "Attention,
obstacle !" quand `eyes.surprised()` est déclenché).

## V3 — Commandes vocales simples

**Matériel à ajouter** : micro USB basique, ~8-10€.

**Logiciel** : reconnaissance de mots-clés simples hors-ligne avec
`Vosk` (léger, fonctionne sur Pi 3B) plutôt qu'une solution cloud. Nouveau
module `listening.py` qui détecte des mots comme "avance", "stop", "tourne".

## V4 — Caméra et vision

**Matériel à ajouter** : module caméra Raspberry Pi (v1/v2) ou webcam USB,
~15-25€.

**Logiciel** : `OpenCV` pour une détection de visage basique (modèle
Haar Cascade, suffisant pour le Pi 3B — évitez les modèles deep learning
lourds, trop lents sur ce modèle de Pi). Le robot pourrait "suivre du
regard" (tourner les yeux/la tête vers le visage détecté) avant d'envisager
un suivi avec déplacement.

> ⚠️ Le Pi 3B a des ressources limitées (1Go RAM, CPU ARM Cortex-A53).
> Pour la vision, privilégiez des traitements légers et une fréquence
> d'analyse basse (ex: 1 image par seconde) plutôt que du temps réel.

## V5 — Contrôle à distance (app/smartphone)

**Option simple** : une petite interface web (Flask) hébergée directement
sur le Pi, accessible depuis le navigateur du téléphone sur le même Wi-Fi,
avec des boutons flèches pour piloter le robot manuellement.

**Option plus avancée** : app mobile dédiée (Flutter/React Native)
communiquant avec le Pi via une API REST ou WebSocket.

## Autres idées en vrac

- Ajouter une **batterie rechargeable intégrée** (18650 + module BMS + bouton
  marche/arrêt) pour ne plus dépendre d'un powerbank externe.
- Ajouter un **capteur de ligne** (suiveur de ligne infrarouge) pour des
  jeux de parcours.
- Ajouter une **boussole/IMU** pour des déplacements plus précis.
- Faire un **mode "suivi"** où le robot suit une source lumineuse (LDR) ou
  une télécommande infrarouge simple.
- Créer des **mini-défis** avec votre fille : labyrinthe en Lego, parcours
  d'obstacles, "fais réagir le robot" (lui faire peur, le câliner via un
  capteur tactile...).

## Comment intégrer proprement une évolution

Le code est organisé en modules indépendants exprès pour ça :

1. Créez un nouveau fichier (`voice.py`, `vision.py`...) avec sa propre
   classe, sans toucher aux modules existants.
2. Ajoutez les éventuels nouveaux réglages dans `config.py`.
3. Importez et utilisez le nouveau module depuis `main.py`, en ajoutant
   des branches à la logique existante plutôt qu'en la réécrivant.

Cette approche permet de faire évoluer le robot pendant des mois/années,
au rythme de votre fille, sans jamais repartir de zéro.
