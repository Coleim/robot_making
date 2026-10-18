# 01 — Liste de courses (BOM)

> Budget visé : 70-150€, hors Raspberry Pi (déjà en votre possession) et hors
> imprimante 3D. Les prix sont indicatifs (2026), à vérifier au moment de l'achat.
> Recherchez sur un site généraliste de composants électroniques ou un
> marketplace, en cherchant les références données.

## Électronique

| # | Composant | Référence / recherche | Prix estimé | Notes |
|---|---|---|---|---|
| 1 | Driver moteur double | DRV8833 ou L298N mini | 4-8€ | Pilote 2 moteurs DC |
| 2 | Moteurs DC + roues | "TT motor gearbox + wheel kit" (jaune, classique robotique) | 8-12€ | Vendus souvent en kit moteur+roue |
| 3 | Roulette folle (caster) | "robot caster wheel ball" 1 pouce | 3-5€ | Pour stabiliser le 3e point d'appui |
| 4 | Capteur ultrason | HC-SR04 | 2-4€ | Détection d'obstacles |
| 5 | Écran OLED | SSD1306 I2C 0.96" (128x64, blanc ou bleu) | 5-8€ | Les yeux du robot |
| 6 | Pack piles AA + support | Support 4×AA avec interrupteur et connecteur fils | 4-6€ | Alimentation moteurs (6V) |
| 7 | Piles AA rechargeables (x4) | NiMH 1.2V 2000mAh+ | 8-12€ | Réutilisables, plus économique à terme |
| 8 | Powerbank USB 5V/2A | Toute batterie USB basique avec sortie micro-USB ou USB-C | 10-20€ | Alimente le Raspberry Pi |
| 9 | Câbles Dupont (M-M, M-F, F-F) | Lot de 120 pièces assorties | 5-7€ | Câblage sans soudure |
| 10 | Breadboard mini (optionnel) | 400 ou 170 points | 2-4€ | Pratique pour prototyper avant de fixer |
| 11 | Résistances 1kΩ et 2kΩ (x2 chacune) | Lot de résistances assorties | 3€ (lot) | Pont diviseur pour le capteur HC-SR04 |
| 12 | Interrupteur simple (optionnel) | Interrupteur ON/OFF à bascule | 2€ | Pratique sur le circuit moteur |
| 13 | Visserie M3 (vis + entretoises + écrous) | Kit visserie M3 pour électronique | 5-8€ | Fixation Pi / plaques |
| 14 | Carte micro SD (si besoin) | 16-32 Go, classe 10 | 6-10€ | Si vous n'en avez pas déjà une pour le Pi |

**Sous-total électronique : ~65-110€**

## Impression 3D

| # | Composant | Détail | Prix estimé |
|---|---|---|---|
| 15 | Filament PLA | 1 bobine 1kg, couleur au choix (ou plusieurs couleurs en petites bobines pour la déco) | 15-20€ |
| 16 | (optionnel) Filament couleur secondaire | Pour les oreilles/détails | 5-10€ (petite bobine) |

## Finitions / déco (avec votre fille)

| # | Composant | Détail | Prix estimé |
|---|---|---|---|
| 17 | Peinture acrylique / feutres posca | Pour personnaliser le robot | 5-10€ |
| 18 | Autocollants, yeux mobiles, etc. (optionnel, pour la déco externe en plus de l'écran) | — | 0-5€ |

## Total estimé

**~95-150€**, dans la fourchette visée, avec de la marge selon ce que vous avez
déjà sous la main (visserie, câbles, peinture...).

## Notes importantes avant l'achat

- Vérifiez que les moteurs DC achetés fonctionnent bien entre **3V et 6V**
  (la plupart des kits "TT motor" le font).
- Le HC-SR04 fonctionne en 5V, mais son **Echo** doit être abaissé à 3.3V
  pour le Pi (voir `04-cablage-electronique.md`) — d'où les résistances.
- Préférez un écran OLED **I2C** (4 fils : VCC, GND, SDA, SCL) plutôt que SPI,
  c'est plus simple à câbler sur un Pi.
- Le Raspberry Pi 3B consomme pas mal : prenez une powerbank qui délivre au
  moins **2A** en sortie, sinon le Pi peut être instable (icône éclair jaune).
