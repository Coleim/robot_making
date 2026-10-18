# 00 — Vue d'ensemble du projet

## Le concept

Un petit robot en forme d'animal stylisé (tête ronde + 2 oreilles + corps ovoïde
sur roues), avec :

- des **yeux animés** sur un écran OLED (clignements, émotions simples) ;
- un **capteur de distance** en guise de "museau", pour détecter les obstacles ;
- **2 moteurs** pour se déplacer et les éviter automatiquement ;
- un cerveau **Raspberry Pi 3B** qui fait tourner le tout en Python.

Le robot est volontairement simple à construire en V1, mais son code et son
châssis sont pensés pour qu'on puisse ajouter des fonctionnalités plus tard
sans tout reconstruire.

## Architecture générale

```
                ┌─────────────────────────┐
                │     Raspberry Pi 3B      │
                │  (cerveau du robot)      │
                └───────┬───────┬─────────┘
                        │       │
         I2C (SDA/SCL)  │       │  GPIO (digital)
                        │       │
              ┌─────────▼──┐ ┌──▼─────────────┐
              │ Écran OLED │ │  Driver moteur  │
              │ (les yeux) │ │   (DRV8833)     │
              └────────────┘ └──┬──────────┬───┘
                                 │          │
                           ┌─────▼───┐ ┌────▼────┐
                           │ Moteur  │ │ Moteur  │
                           │ gauche  │ │ droit   │
                           └─────────┘ └─────────┘

              GPIO (digital) : capteur ultrason HC-SR04 (le "nez")
```

Deux circuits d'alimentation séparés (important !) :
- Le **Raspberry Pi** est alimenté par une batterie USB (powerbank) 5V.
- Les **moteurs** sont alimentés par un pack de piles séparé (4×AA, 6V) via le
  driver moteur.
- Les masses (GND) des deux circuits sont reliées entre elles (obligatoire
  pour que les signaux de commande fonctionnent).

On sépare l'alimentation moteur de celle du Pi car les moteurs créent des
pics de courant qui peuvent faire reboot le Pi s'ils partagent la même
alimentation.

## Étapes du tuto

| Fichier | Contenu |
|---|---|
| `01-bom.md` | Liste de courses complète avec budget |
| `02-impression-3d.md` | Impression des pièces du châssis |
| `03-assemblage-mecanique.md` | Montage du châssis, moteurs, roues |
| `04-cablage-electronique.md` | Câblage Pi / driver / capteur / écran |
| `05-installation-logicielle.md` | Préparation du Raspberry Pi |
| `06-code-mouvement.md` | Faire rouler le robot et éviter les obstacles |
| `07-code-yeux.md` | Animer les yeux sur l'écran OLED |
| `08-tests-calibration.md` | Vérifications et réglages |
| `09-personnalisation.md` | Déco, peinture, nom du robot — avec votre fille |
| `10-evolutions.md` | Pistes pour la suite (son, voix, caméra, app) |

## Ce qu'il vous faut avant de commencer

- Un Raspberry Pi 3B (vous l'avez déjà ✅)
- Accès à une imprimante 3D (vous avez dit pouvoir en trouver une ✅)
- Un fer à souder (optionnel, pour plus de fiabilité sur les moteurs)
- Tournevis cruciforme, pince coupante, colle (optionnel)
- Un après-midi (montage) + une soirée (code) — à faire en plusieurs fois avec
  votre fille, pas besoin de tout faire d'un coup !
