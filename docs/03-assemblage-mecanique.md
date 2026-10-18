# 03 — Assemblage mécanique

👨‍👧 **Étapes marquées "👧" = parfaites à faire avec votre fille.**

## Ce qu'il vous faut sous la main

- Les pièces imprimées (base, tête, oreilles, support batterie)
- 2 moteurs DC + roues
- 1 roulette folle
- Vis M3 + entretoises
- Tournevis cruciforme
- Colle forte (optionnelle, pour la roulette folle si elle n'a pas de trous de fixation)

## Étape 1 — Fixer les moteurs sur la base 👧

1. Glissez chaque moteur dans son logement sur `base.scad` (les deux
   encoches rectangulaires à l'avant).
2. Si le moteur ne tient pas assez serré, ajoutez un point de colle chaude
   sur les côtés (pas sur l'axe !).
3. Faites essayer les roues à votre fille sur les axes des moteurs — elle
   peut faire cette étape seule, c'est juste de l'emboîtement.

## Étape 2 — Monter la roulette folle

1. Positionnez la roulette folle dans son support à l'arrière de la base.
2. Vissez avec 2-4 petites vis selon le modèle de roulette.

👉 Vérifiez que le robot touche le sol uniquement par les 2 roues motrices
et la roulette folle (pas par le châssis), en le posant sur une table.

## Étape 3 — Fixer le Raspberry Pi 👧

1. Posez le Raspberry Pi sur les 4 plots prévus au centre de la base.
2. Vissez avec 4 vis M3 (serrage léger, ne pas forcer sur le PCB).
3. Laissez votre fille brancher la carte SD dans le Pi (satisfaisant, un
   petit "clic").

## Étape 4 — Installer le support batterie

1. Fixez `support_batterie.scad` sous la base avec 2 vis M3, ou avec du
   velcro/scratch si vous préférez pouvoir le détacher facilement pour
   changer les piles.
2. Glissez le pack de piles dedans (sans les piles pour l'instant).

## Étape 5 — Préparer la tête

1. Glissez l'écran OLED dans son logement (`oled_card_slot`), face visible
   contre la fenêtre.
2. Glissez le capteur HC-SR04 dans son emplacement sous l'écran (le
   "museau").
3. Clipsez les 2 oreilles dans leurs trous respectifs. 👧 (votre fille peut
   choisir l'orientation/l'inclinaison si vous avez laissé un peu de jeu)

## Étape 6 — Assembler tête + base

1. Ne fixez pas encore la tête définitivement : faites d'abord tout le
   câblage (étape suivante), la tête doit rester amovible pour accéder
   facilement aux fils en cas de souci.
2. Une fois tout testé et validé (voir `08-tests-calibration.md`), fixez la
   tête avec 2 petites vis ou un point de colle démontable (pâte adhésive
   type "patafix" fonctionne très bien et reste amovible).

## ✅ Checklist avant de passer au câblage

- [ ] Les 2 moteurs tournent librement à la main (pas de frottement)
- [ ] La roulette folle pivote librement
- [ ] Le Pi est bien fixé, pas de jeu
- [ ] L'écran OLED est visible à travers la fenêtre de la tête
- [ ] Le capteur ultrason est bien aligné à l'avant (les 2 "yeux" visibles)

➡️ Passez à `04-cablage-electronique.md`.
