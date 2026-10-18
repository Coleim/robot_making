# 06 — Code : mouvement et évitement d'obstacles

Le code se trouve dans le dossier [`src/`](../src/).

## Fichiers concernés

- `config.py` — tous les réglages (numéros de GPIO, vitesses, seuils)
- `motors.py` — pilotage des 2 moteurs via le driver DRV8833
- `sensors.py` — lecture du capteur ultrason HC-SR04
- `main.py` — boucle principale qui assemble tout

## Comment ça marche

### `motors.py`

Chaque moteur est piloté par 2 broches GPIO en PWM (modulation de largeur
d'impulsion), ce qui permet de régler la vitesse (0 à 100) en plus du sens
de rotation. 4 méthodes simples : `forward()`, `backward()`, `turn_left()`,
`turn_right()`, plus `stop()`.

### `sensors.py`

Le HC-SR04 fonctionne en envoyant une impulsion ultrason et en mesurant le
temps que met l'écho à revenir. `distance_cm()` retourne la distance
mesurée, `is_obstacle_near()` retourne `True`/`False` selon un seuil réglable
dans `config.py` (`OBSTACLE_DISTANCE_CM`, 20cm par défaut).

### `main.py`

Boucle simple :
1. Mesure la distance.
2. Si obstacle proche → recule, tourne, repart.
3. Sinon → avance tout droit.

## Tester uniquement le mouvement (sans les yeux)

Pratique pour débugger étape par étape. Créez un script de test :

```python
# test_motors.py
import time
from motors import Motors

m = Motors()
m.forward()
time.sleep(1)
m.stop()
m.turn_left()
time.sleep(0.5)
m.stop()
m.cleanup()
```

```bash
cd ~/robot-layla
source .venv/bin/activate
python3 test_motors.py
```

Le robot doit avancer 1 seconde, puis tourner sur lui-même brièvement.
Si les roues tournent dans le mauvais sens, inversez les 2 fils du moteur
concerné sur le driver (plus simple que de changer le code).

## Tester uniquement le capteur

```python
# test_sensor.py
import time
from sensors import DistanceSensor

s = DistanceSensor()
while True:
    print(s.distance_cm(), "cm")
    time.sleep(0.5)
```

Approchez votre main du capteur : la distance affichée doit diminuer.

➡️ Une fois ces deux tests validés, passez à `07-code-yeux.md`.
