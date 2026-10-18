# 04 — Câblage électronique

Référez-vous au schéma détaillé : [`wiring/schema-cablage.md`](../wiring/schema-cablage.md).

## Ordre conseillé

1. **Pi éteint, débranché.**
2. Câblez l'écran OLED (4 fils : VCC, GND, SDA, SCL).
3. Câblez le capteur ultrason, **avec le pont diviseur de tension** sur ECHO
   (ne sautez pas cette étape, sinon vous risquez d'abîmer le GPIO du Pi).
4. Câblez le driver moteur DRV8833 (logique vers le Pi, puissance vers le
   pack de piles).
5. Reliez les masses (GND) : Pi ↔ driver moteur ↔ pack de piles.
6. Relisez la checklist en bas du schéma de câblage avant de brancher quoi
   que ce soit sous tension.

## Conseil pratique

Faites d'abord tout le câblage **sur une breadboard mini**, posée à côté du
robot, avant de câbler "en dur" dans le châssis. Ça permet de tester et
corriger facilement sans défaire des fils déjà fixés.

## Une fois câblé : premier test sous tension

1. Branchez d'abord **uniquement** le Pi (powerbank), **pas encore** le pack
   moteur.
2. Le Pi doit démarrer normalement (LED verte clignote, pas de rond jaune
   d'alerte tension persistant).
3. Si tout va bien, éteignez le Pi, branchez le pack moteur, puis rallumez
   le Pi.

➡️ Si quelque chose ne fonctionne pas comme prévu, revérifiez chaque
connexion avec le schéma avant de passer à la suite — ne forcez jamais une
connexion qui ne "rentre pas" naturellement.

➡️ Passez à `05-installation-logicielle.md`.
