"""
Configuration centrale du robot — Robot Layla.

Tous les numéros de GPIO et constantes réglables sont ici, pour pouvoir
tout ajuster à un seul endroit si votre câblage diffère du tuto.
"""

# --- Moteurs (connectés au driver DRV8833) ---
MOTOR_LEFT_IN1 = 17
MOTOR_LEFT_IN2 = 27
MOTOR_RIGHT_IN1 = 22
MOTOR_RIGHT_IN2 = 23

# Fréquence du PWM logiciel pour contrôler la vitesse (Hz)
PWM_FREQUENCY = 100

# Vitesse par défaut (0-100)
DEFAULT_SPEED = 60

# --- Capteur ultrason HC-SR04 ---
SENSOR_TRIG = 4
SENSOR_ECHO = 24

# Distance (cm) en dessous de laquelle le robot évite l'obstacle
OBSTACLE_DISTANCE_CM = 20

# --- Écran OLED ---
OLED_WIDTH = 128
OLED_HEIGHT = 64
OLED_I2C_ADDRESS = 0x3C

# --- Comportement général ---
LOOP_DELAY_S = 0.05  # pause entre chaque cycle de la boucle principale
