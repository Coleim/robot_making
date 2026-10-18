"""
Module moteurs — Robot Layla.

Gère les 2 moteurs DC via le driver DRV8833, en pilotage simple
tout-ou-rien (avance / recule / tourne / stop), avec PWM logiciel pour
moduler la vitesse.

Pensé pour être utilisé indépendamment du reste (pas de dépendance aux
autres modules), afin de rester facile à réutiliser/étendre plus tard.
"""

import RPi.GPIO as GPIO

import config


class Motors:
    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)

        for pin in (config.MOTOR_LEFT_IN1, config.MOTOR_LEFT_IN2,
                    config.MOTOR_RIGHT_IN1, config.MOTOR_RIGHT_IN2):
            GPIO.setup(pin, GPIO.OUT)

        self._pwm_left_1 = GPIO.PWM(config.MOTOR_LEFT_IN1, config.PWM_FREQUENCY)
        self._pwm_left_2 = GPIO.PWM(config.MOTOR_LEFT_IN2, config.PWM_FREQUENCY)
        self._pwm_right_1 = GPIO.PWM(config.MOTOR_RIGHT_IN1, config.PWM_FREQUENCY)
        self._pwm_right_2 = GPIO.PWM(config.MOTOR_RIGHT_IN2, config.PWM_FREQUENCY)

        for pwm in (self._pwm_left_1, self._pwm_left_2,
                    self._pwm_right_1, self._pwm_right_2):
            pwm.start(0)

    def _set_motor(self, pwm_forward, pwm_backward, speed):
        """speed: -100 (recule à fond) à 100 (avance à fond), 0 = arrêt."""
        speed = max(-100, min(100, speed))
        if speed > 0:
            pwm_forward.ChangeDutyCycle(speed)
            pwm_backward.ChangeDutyCycle(0)
        elif speed < 0:
            pwm_forward.ChangeDutyCycle(0)
            pwm_backward.ChangeDutyCycle(-speed)
        else:
            pwm_forward.ChangeDutyCycle(0)
            pwm_backward.ChangeDutyCycle(0)

    def set_speeds(self, left_speed, right_speed):
        """Contrôle indépendant de chaque roue (-100 à 100)."""
        self._set_motor(self._pwm_left_1, self._pwm_left_2, left_speed)
        self._set_motor(self._pwm_right_1, self._pwm_right_2, right_speed)

    def forward(self, speed=config.DEFAULT_SPEED):
        self.set_speeds(speed, speed)

    def backward(self, speed=config.DEFAULT_SPEED):
        self.set_speeds(-speed, -speed)

    def turn_left(self, speed=config.DEFAULT_SPEED):
        self.set_speeds(-speed, speed)

    def turn_right(self, speed=config.DEFAULT_SPEED):
        self.set_speeds(speed, -speed)

    def stop(self):
        self.set_speeds(0, 0)

    def cleanup(self):
        self.stop()
        for pwm in (self._pwm_left_1, self._pwm_left_2,
                    self._pwm_right_1, self._pwm_right_2):
            pwm.stop()
        GPIO.cleanup()
