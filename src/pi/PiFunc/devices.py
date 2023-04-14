from typing import Optional
import RPi.GPIO as GPIO
import time
from threading import Thread
from pi.models import Device
from random import random


class LED:
    ON: str = "O"
    OFF: str = "F"
    BLINK: str = "B"

    def __init__(self, device: Device) -> None:
        self.device: Device = device
        self._safe: float = random()
        self.LED_PIN = self.device.pin
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.LED_PIN, GPIO.OUT)

    def blink(self, times: Optional[int] = 5, blink_time: Optional[float] = 0.3) -> bool:
        if self.device.state != self.OFF:
            return False

        tread: Thread = Thread(
            target=self._blink_task,
            args=((times, blink_time, self._safe))
        )

        self.device.state = self.BLINK
        self.device.save()
        tread.start()
        return True

    def on(self) -> bool:
        if self.device.state != self.OFF:
            return False
        GPIO.output(self.LED_PIN, GPIO.HIGH)
        time.sleep(0.1)
        # GPIO.cleanup()
        self.device.state = self.ON
        self.device.save()
        return True

    def off(self) -> bool:
        if self.device.state != self.ON:
            return False

        GPIO.output(self.LED_PIN, GPIO.LOW)
        time.sleep(0.1)
        GPIO.cleanup()
        self.device.state = self.OFF
        self.device.save()
        return True

    def cleanup(self):
        GPIO.cleanup()

    def _blink_task(self, *args: tuple[int, float, float]) -> None:
        times: int = args[0]
        blink_time: float = args[1]

        if self._safe != args[2]:
            return

        for _ in range(times):
            GPIO.output(self.LED_PIN, GPIO.HIGH)
            time.sleep(blink_time)
            GPIO.output(self.LED_PIN, GPIO.LOW)
            time.sleep(blink_time)

        GPIO.cleanup()
        self.device.state = self.OFF
        self.device.save()
