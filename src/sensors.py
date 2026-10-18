"""
Module capteur — Robot Layla.

Mesure de distance avec un capteur ultrason HC-SR04.
"""

import time

import RPi.GPIO as GPIO

import config


class DistanceSensor:
    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(config.SENSOR_TRIG, GPIO.OUT)
        GPIO.setup(config.SENSOR_ECHO, GPIO.IN)
        GPIO.output(config.SENSOR_TRIG, False)
        time.sleep(0.5)  # laisse le capteur se stabiliser au démarrage

    def distance_cm(self, timeout=0.04):
        """Retourne la distance mesurée en cm, ou None si pas de mesure
        valide dans le délai imparti (timeout en secondes)."""
        GPIO.output(config.SENSOR_TRIG, True)
        time.sleep(0.00001)  # impulsion de 10 microsecondes
        GPIO.output(config.SENSOR_TRIG, False)

        start_time = time.time()
        stop_time = time.time()
        deadline = start_time + timeout

        # Attend le début de l'écho
        while GPIO.input(config.SENSOR_ECHO) == 0:
            start_time = time.time()
            if start_time > deadline:
                return None

        # Attend la fin de l'écho
        while GPIO.input(config.SENSOR_ECHO) == 1:
            stop_time = time.time()
            if stop_time > deadline:
                return None

        elapsed = stop_time - start_time
        # vitesse du son ≈ 34300 cm/s, aller-retour donc /2
        distance = (elapsed * 34300) / 2
        return round(distance, 1)

    def is_obstacle_near(self, threshold_cm=config.OBSTACLE_DISTANCE_CM):
        distance = self.distance_cm()
        return distance is not None and distance < threshold_cm
