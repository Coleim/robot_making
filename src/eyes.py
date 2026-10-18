"""
Module yeux — Robot Layla.

Anime des "yeux" sur l'écran OLED SSD1306, avec quelques émotions
simples (neutre, content, surpris, endormi) et un clignement
périodique pour donner vie au robot.

Pensé pour être facilement enrichi plus tard avec de nouvelles
émotions (voir docs/10-evolutions.md).
"""

import time

import board
import busio
import adafruit_ssd1306
from PIL import Image, ImageDraw

import config


class Eyes:
    def __init__(self):
        i2c = busio.I2C(board.SCL, board.SDA)
        self.oled = adafruit_ssd1306.SSD1306_I2C(
            config.OLED_WIDTH, config.OLED_HEIGHT, i2c,
            addr=config.OLED_I2C_ADDRESS,
        )
        self.image = Image.new("1", (config.OLED_WIDTH, config.OLED_HEIGHT))
        self.draw = ImageDraw.Draw(self.image)
        self._last_blink = time.time()

    def _show(self):
        self.oled.image(self.image)
        self.oled.show()

    def _clear(self):
        self.draw.rectangle(
            (0, 0, config.OLED_WIDTH, config.OLED_HEIGHT), outline=0, fill=0
        )

    def _draw_round_eyes(self, radius):
        cx_left, cx_right = config.OLED_WIDTH // 3, (config.OLED_WIDTH // 3) * 2
        cy = config.OLED_HEIGHT // 2
        for cx in (cx_left, cx_right):
            self.draw.ellipse(
                (cx - radius, cy - radius, cx + radius, cy + radius), fill=1
            )

    def neutral(self):
        """Émotion neutre : 2 ronds pleins."""
        self._clear()
        self._draw_round_eyes(radius=14)
        self._show()

    def happy(self):
        """Émotion joyeuse : yeux en forme de 'sourire' (demi-cercles)."""
        self._clear()
        cx_left, cx_right = config.OLED_WIDTH // 3, (config.OLED_WIDTH // 3) * 2
        cy = config.OLED_HEIGHT // 2
        r = 14
        for cx in (cx_left, cx_right):
            self.draw.arc((cx - r, cy - r, cx + r, cy + r), start=180, end=360, fill=1, width=4)
        self._show()

    def surprised(self):
        """Émotion surprise : grands yeux ronds."""
        self._clear()
        self._draw_round_eyes(radius=20)
        self._show()

    def sleepy(self):
        """Endormi : fines lignes horizontales."""
        self._clear()
        cx_left, cx_right = config.OLED_WIDTH // 3, (config.OLED_WIDTH // 3) * 2
        cy = config.OLED_HEIGHT // 2
        for cx in (cx_left, cx_right):
            self.draw.line((cx - 14, cy, cx + 14, cy), fill=1, width=4)
        self._show()

    def blink(self):
        """Petite animation de clignement, à appeler ponctuellement."""
        self.sleepy()
        time.sleep(0.15)
        self.neutral()

    def maybe_blink(self, every_s=4.0):
        """À appeler régulièrement depuis la boucle principale : clignote
        automatiquement toutes les `every_s` secondes environ."""
        now = time.time()
        if now - self._last_blink > every_s:
            self.blink()
            self._last_blink = now

    def off(self):
        self._clear()
        self._show()
