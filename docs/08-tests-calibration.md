# 08 — Tests et calibration

## Lancer le robot complet

```bash
cd ~/robot-layla
source .venv/bin/activate
python3 main.py
```

Posez le robot au sol (pas sur une table, risque de chute !), face à un
espace dégagé, et observez :

1. Il doit avancer tout droit.
2. En approchant un obstacle (votre main, un livre), il doit s'arrêter,
   reculer, tourner, puis repartir.
3. Les yeux doivent changer d'expression selon la situation.

## Problèmes fréquents et solutions

| Symptôme | Cause probable | Solution |
|---|---|---|
| Le robot tourne en rond au lieu d'avancer | Un moteur tourne à l'envers | Inversez les 2 fils de ce moteur sur le driver |
| Le robot ne réagit jamais aux obstacles | Mauvais câblage du capteur / pont diviseur absent | Revérifiez `wiring/schema-cablage.md` |
| Le robot réagit "trop tard" ou "trop tôt" | Seuil de distance pas adapté | Ajustez `OBSTACLE_DISTANCE_CM` dans `config.py` |
| Rien ne s'affiche sur l'écran | Adresse I2C incorrecte ou mauvais câblage | Relancez `i2cdetect -y 1`, ajustez `OLED_I2C_ADDRESS` |
| Le Pi redémarre quand les moteurs démarrent | Alimentation moteur pas assez séparée / masse commune manquante | Revérifiez les masses communes |
| Le robot va trop vite / trop lentement | Vitesse par défaut | Ajustez `DEFAULT_SPEED` dans `config.py` (0-100) |

## Calibration fine

- **Distance de détection** (`OBSTACLE_DISTANCE_CM`) : testez différentes
  valeurs (15, 20, 30cm) selon la taille de la pièce où le robot évolue.
- **Vitesse** (`DEFAULT_SPEED`) : commencez bas (40-50) pour les premiers
  essais avec votre fille, augmentez progressivement.
- **Durée de rotation après obstacle** : dans `main.py`, le
  `time.sleep(0.5)` après `turn_right()` peut être ajusté si le robot ne
  tourne pas assez (ou trop) pour éviter l'obstacle.

## Checklist de sécurité avant de lâcher le robot à votre fille

- [ ] Pas de fils qui dépassent / qui pourraient se prendre dans les roues
- [ ] Le robot s'arrête bien quand on le soulève légèrement (les roues
      dans le vide ne doivent pas s'emballer dangereusement — sinon
      baissez `DEFAULT_SPEED`)
- [ ] Testé sur sol dégagé, loin des escaliers/bords de table
- [ ] Bouton d'arrêt facile d'accès (l'interrupteur du pack moteur, ou
      `Ctrl+C` si vous êtes connecté en SSH)

➡️ Une fois tout validé, place à la déco ! `09-personnalisation.md`.
