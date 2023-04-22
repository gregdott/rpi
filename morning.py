# Simple thing for phasing in light from dim to a comfortable warm light
# This is the start for what will be used to create my morning light
# Saving this so things don't get lost :)

import time
import board
import neopixel


pixel_pin = board.D18

num_pixels = 300

# For RGBW NeoPixels, simply change the ORDER to RGBW or GRBW.
ORDER = neopixel.GRB

pixels = neopixel.NeoPixel(
    pixel_pin, num_pixels, brightness=0.1, auto_write=False, pixel_order=ORDER
)

def increase_brightness(brightness, shift_delay):
    if brightness < 1.0:
        return brightness + (shift_delay/5)
    else:
        return 1.0

shift_delay = 0.01
grb = (0, 0, 0)
steps = 0

while grb[1] < 255:
    steps = steps + 1
    print(grb)
    pixels.fill(grb)
    pixels.brightness = increase_brightness(pixels.brightness, shift_delay)
    print(pixels.brightness)
    pixels.show()
    grb = tuple(map(lambda i, j: i + j, grb, (0, 1, 0)))
    time.sleep(shift_delay)

while grb[2] < 15:
    pixels.brightness = increase_brightness(pixels.brightness, shift_delay)
    print(pixels.brightness)
    steps = steps + 1
    pixels.fill(grb)
    pixels.show()
    grb = tuple(map(lambda i, j: i + j, grb, (0, 0, 1)))
    time.sleep(shift_delay)
    print(grb)

while grb[0] < 65:
    steps = steps + 1
    print(grb)
    pixels.fill(grb)
    pixels.brightness = increase_brightness(pixels.brightness, shift_delay)
    print(pixels.brightness)
    pixels.show()
    grb = tuple(map(lambda i, j: i + j, grb, (1, 0, 0)))
    time.sleep(shift_delay)

print(steps)

