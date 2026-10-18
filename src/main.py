"""
Robot Layla — programme principal.

Comportement V1 :
- avance tout droit
- si un obstacle est détecté, recule un peu, tourne, puis repart
- les yeux réagissent à la situation (content en roulant, surpris face
  à un obstacle, endormi s'il reste immobile trop longtemps)

Ce fichier reste volontairement simple : toute la logique "matérielle"
est dans motors.py / sensors.py / eyes.py, pour pouvoir faire évoluer le
comportement ici sans toucher au reste.
"""

import time

import config
from motors import Motors
from sensors import DistanceSensor
from eyes import Eyes


def main():
    motors = Motors()
    sensor = DistanceSensor()
    eyes = Eyes()

    print("Robot Layla démarré ! (Ctrl+C pour arrêter)")

    try:
        while True:
            if sensor.is_obstacle_near():
                eyes.surprised()
                motors.stop()
                time.sleep(0.3)

                motors.backward()
                time.sleep(0.4)

                motors.turn_right()
                time.sleep(0.5)

                motors.stop()
                eyes.neutral()
            else:
                motors.forward()
                eyes.happy()
                eyes.maybe_blink()

            time.sleep(config.LOOP_DELAY_S)

    except KeyboardInterrupt:
        print("\nArrêt du robot...")
    finally:
        motors.stop()
        eyes.off()
        motors.cleanup()


if __name__ == "__main__":
    main()
