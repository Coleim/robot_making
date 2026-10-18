# Schéma de câblage — Robot Layla

## ⚠️ Règle d'or avant de commencer

**Toujours câbler avec le Raspberry Pi éteint et débranché.**
On ne branche l'alimentation qu'une fois tout le câblage vérifié.

## Vue d'ensemble des connexions

```
RASPBERRY PI 3B (GPIO, vue de dessus, broche 1 en haut à gauche)
┌─────────────────────────────────────────────┐
│ 1  3V3      5V   2                            │
│ 3  SDA ───────────────► OLED SDA             │
│ 5  SCL ───────────────► OLED SCL             │
│ 7  GPIO4 ──────────────► HC-SR04 TRIG         │
│ 9  GND                                        │
│ 11 GPIO17 ─────────────► DRV8833 AIN1         │
│ 13 GPIO27 ─────────────► DRV8833 AIN2         │
│ 15 GPIO22 ─────────────► DRV8833 BIN1         │
│ ...                                           │
│ 16 GPIO23 ─────────────► DRV8833 BIN2         │
│ 18 GPIO24 ─◄──(pont diviseur)──── HC-SR04 ECHO│
│ (3V3, GND également utilisés, voir détail)    │
└─────────────────────────────────────────────┘
```

> Les numéros exacts de GPIO sont ceux utilisés par le code fourni dans
> `src/`. Vous pouvez les changer, mais pensez à adapter `src/config.py`
> en conséquence.

## 1. Écran OLED SSD1306 (I2C)

| OLED | Raspberry Pi |
|---|---|
| VCC | 3V3 (broche 1) |
| GND | GND (broche 6, 9, 14, 20...) |
| SDA | GPIO2 / SDA (broche 3) |
| SCL | GPIO3 / SCL (broche 5) |

➡️ Il faudra activer l'I2C sur le Pi (voir `05-installation-logicielle.md`).

## 2. Capteur ultrason HC-SR04

Le HC-SR04 fonctionne en 5V, mais ses broches ne sont **pas** 3.3V-safe en
entrée sur le Pi pour le signal `ECHO`. On utilise un **pont diviseur de
tension** avec 2 résistances pour ramener 5V à environ 3V.

| HC-SR04 | Vers |
|---|---|
| VCC | 5V (broche 2 ou 4) |
| GND | GND |
| TRIG | GPIO4 (broche 7) — direct, pas besoin de diviseur (c'est une sortie du Pi) |
| ECHO | ➡️ via pont diviseur ➡️ GPIO24 (broche 18) |

### Pont diviseur pour ECHO

```
HC-SR04 ECHO ──[ R1 = 1kΩ ]──┬── GPIO24 (Pi)
                              │
                         [ R2 = 2kΩ ]
                              │
                             GND
```

Ce montage ramène les 5V du signal ECHO à environ 3.3V (5V × R2/(R1+R2) ≈ 3.3V),
sans danger pour le GPIO du Pi.

## 3. Driver moteur DRV8833

| DRV8833 | Vers |
|---|---|
| VM (alim moteurs) | + du pack 4×AA (6V) |
| GND (côté alim) | - du pack 4×AA **ET** GND du Pi (masse commune, important !) |
| VCC (logique, si séparé) | 3V3 du Pi |
| AIN1 | GPIO17 (broche 11) |
| AIN2 | GPIO27 (broche 13) |
| BIN1 | GPIO22 (broche 15) |
| BIN2 | GPIO23 (broche 16) |
| AOUT1 / AOUT2 | Moteur gauche (2 fils, sens indifférent au départ) |
| BOUT1 / BOUT2 | Moteur droit (2 fils) |

> Si en testant le robot il tourne en rond au lieu d'avancer droit : inversez
> simplement les 2 fils d'un des deux moteurs.

## 4. Alimentation générale

```
Powerbank USB 5V ───► Port USB/micro-USB du Raspberry Pi (alimentation Pi)

Pack 4×AA (6V) ──[interrupteur]──► VM du DRV8833 (alimentation moteurs)
                                 └─► GND commun avec le Pi
```

**Important** : reliez bien le GND du pack de piles au GND du Raspberry Pi
(un simple fil entre les deux), sinon les commandes moteur ne
fonctionneront pas correctement (c'est la "masse commune", indispensable
dès qu'on a 2 alimentations différentes dans un même circuit).

## Tableau récapitulatif des GPIO utilisés

| GPIO (BCM) | Broche physique | Usage |
|---|---|---|
| 2 (SDA) | 3 | Écran OLED |
| 3 (SCL) | 5 | Écran OLED |
| 4 | 7 | TRIG capteur ultrason |
| 17 | 11 | Moteur gauche IN1 |
| 27 | 13 | Moteur gauche IN2 |
| 22 | 15 | Moteur droit IN1 |
| 23 | 16 | Moteur droit IN2 |
| 24 | 18 | ECHO capteur ultrason (via pont diviseur) |

## Checklist avant la première mise sous tension

- [ ] Toutes les connexions GND sont bien communes (Pi + pack piles)
- [ ] Le pont diviseur est bien câblé sur ECHO (pas directement au GPIO)
- [ ] L'OLED est alimenté en 3.3V, pas en 5V
- [ ] Le pack de piles n'est **pas** branché sur l'alimentation du Pi
- [ ] Rien ne touche/court-circuite sous le châssis (fils bien rangés)
