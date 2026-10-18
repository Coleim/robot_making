# 05 — Installation logicielle sur le Raspberry Pi

## 1. Flasher le système d'exploitation

1. Téléchargez [Raspberry Pi Imager](https://www.raspberrypi.com/software/).
2. Choisissez **"Raspberry Pi OS Lite (64-bit)"** si vous êtes à l'aise en
   ligne de commande, sinon **"Raspberry Pi OS (64-bit)"** (avec bureau).
   > Le Pi 3B supporte le 64-bit, et ça tourne un peu mieux qu'en 32-bit.
3. Dans les options avancées (icône ⚙️) :
   - Activez SSH
   - Configurez le Wi-Fi (nom + mot de passe)
   - Définissez un nom d'utilisateur/mot de passe
   - Définissez le nom d'hôte, ex: `robot-layla`
4. Flashez sur la carte SD, insérez-la dans le Pi, démarrez.

## 2. Se connecter au Pi

Depuis votre ordinateur, sur le même réseau Wi-Fi :

```bash
ssh pi@robot-layla.local
```

## 3. Mettre à jour le système

```bash
sudo apt update && sudo apt full-upgrade -y
sudo reboot
```

## 4. Activer I2C (pour l'écran OLED)

```bash
sudo raspi-config
```

→ `Interface Options` → `I2C` → `Yes` → redémarrer si demandé.

Vérifiez ensuite que l'écran est bien détecté :

```bash
sudo apt install -y i2c-tools
i2cdetect -y 1
```

Vous devriez voir une adresse apparaître dans la grille (souvent `3c` pour
les écrans SSD1306).

## 5. Installer Python et les dépendances

```bash
sudo apt install -y python3-pip python3-venv git
```

## 6. Récupérer le code du robot

Si vous avez un dépôt Git (ce projet), clonez-le directement sur le Pi.
Sinon, copiez simplement le dossier `src/` sur le Pi (via `scp` ou clé USB) :

```bash
scp -r src pi@robot-layla.local:/home/pi/robot-layla
```

## 7. Créer un environnement virtuel et installer les librairies

```bash
cd ~/robot-layla
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## 8. Premier test rapide

```bash
python3 -c "from board import SCL, SDA; import busio; i2c = busio.I2C(SCL, SDA); print('OK')"
```

Si ça affiche `OK` sans erreur, l'I2C fonctionne et vous êtes prêt pour
`06-code-mouvement.md` et `07-code-yeux.md`.

## (Optionnel) Lancer le robot au démarrage du Pi

Une fois tout testé et validé, vous pouvez faire en sorte que le robot
démarre tout seul à l'allumage, pratique pour votre fille (pas besoin de
taper de commande) :

```bash
sudo nano /etc/systemd/system/robot-layla.service
```

```ini
[Unit]
Description=Robot Layla
After=multi-user.target

[Service]
Type=simple
User=pi
WorkingDirectory=/home/pi/robot-layla
ExecStart=/home/pi/robot-layla/.venv/bin/python3 main.py
Restart=on-failure

[Install]
WantedBy=multi-user.target
```

```bash
sudo systemctl daemon-reload
sudo systemctl enable --now robot-layla.service
```
