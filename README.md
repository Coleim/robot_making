# 🦊 Robot Layla — un petit robot animal à construire avec sa fille

Projet complet pour fabriquer, à la maison, un petit robot mignon en forme d'animal,
piloté par un Raspberry Pi 3B, avec des yeux animés sur écran OLED, capable de rouler
et d'éviter les obstacles. Pensé pour être **construit avec un enfant de 8 ans**, et
**évolutif** (son, voix, caméra, app mobile...).

## 🗂️ Structure du projet

```
robot-layla/
├── docs/        → le tuto complet, étape par étape (commencez ici !)
├── cad/         → fichiers 3D à imprimer (OpenSCAD, exportables en STL)
├── src/         → code Python du robot (modulaire et évolutif)
└── wiring/      → schémas de câblage électronique
```

## 🚀 Par où commencer ?

1. Lisez [`docs/00-overview.md`](docs/00-overview.md) pour la vue d'ensemble du projet.
2. Suivez les fichiers du dossier `docs/` dans l'ordre (numérotés).
3. Imprimez les pièces du dossier `cad/`.
4. Montez le robot avec votre fille 🎉.

## 💰 Budget visé

Environ **70-150€** (hors Raspberry Pi, hors imprimante 3D), filament inclus.
Détail complet dans [`docs/01-bom.md`](docs/01-bom.md).

## 🧩 Niveau

Bases en électronique/Raspberry Pi suffisantes. Pas de soudure obligatoire
(tout est en connecteurs Dupont / breadboard-friendly), mais un peu de soudure
peut améliorer la fiabilité (optionnel, voir doc).

## 🌱 Évolutivité prévue

Le code est organisé en modules (`motors.py`, `sensors.py`, `eyes.py`...) pour
ajouter facilement, plus tard :
- 🔊 Son & synthèse vocale
- 🎤 Micro & commandes vocales
- 📷 Caméra & suivi de visage
- 📱 Contrôle à distance depuis une app

Voir [`docs/10-evolutions.md`](docs/10-evolutions.md).
