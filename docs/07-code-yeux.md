# 07 — Code : les yeux animés

Le fichier concerné est [`src/eyes.py`](../src/eyes.py).

## Principe

On dessine des formes simples (cercles, arcs, lignes) sur une image en
mémoire avec la librairie **Pillow**, puis on envoie cette image à l'écran
OLED via la librairie `adafruit_ssd1306`.

## Émotions disponibles (V1)

| Méthode | Rendu | Utilisée quand... |
|---|---|---|
| `neutral()` | 2 ronds pleins | Par défaut |
| `happy()` | 2 arcs (sourire) | Le robot avance librement |
| `surprised()` | 2 grands ronds | Un obstacle est détecté |
| `sleepy()` | 2 lignes fines | Clignement / inactivité |
| `blink()` | neutral → sleepy → neutral | Appelé périodiquement |

## Tester uniquement les yeux

```python
# test_eyes.py
import time
from eyes import Eyes

e = Eyes()
e.neutral()
time.sleep(1)
e.happy()
time.sleep(1)
e.surprised()
time.sleep(1)
e.blink()
time.sleep(1)
e.off()
```

```bash
python3 test_eyes.py
```

## Ajouter une nouvelle émotion

C'est l'endroit idéal pour une activité créative avec votre fille : laissez-la
imaginer une émotion (en colère, amoureux, qui réfléchit...) et dessinez-la
ensemble !

```python
def angry(self):
    """Émotion fâché : sourcils obliques au-dessus des yeux."""
    self._clear()
    self._draw_round_eyes(radius=14)
    cx_left, cx_right = config.OLED_WIDTH // 3, (config.OLED_WIDTH // 3) * 2
    cy = config.OLED_HEIGHT // 2
    self.draw.line((cx_left - 16, cy - 22, cx_left + 4, cy - 14), fill=1, width=3)
    self.draw.line((cx_right + 16, cy - 22, cx_right - 4, cy - 14), fill=1, width=3)
    self._show()
```

Ajoutez ensuite cette méthode dans `eyes.py`, puis appelez `eyes.angry()`
depuis `main.py` au moment voulu (par exemple si le robot est bloqué trop
longtemps face à un mur).

➡️ Une fois le mouvement et les yeux testés séparément, passez à
`08-tests-calibration.md` pour tout assembler.
