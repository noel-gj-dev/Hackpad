import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC
from kmk.modules.macros import Macros
from kmk.modules.rotary_encoder import RotaryEncoder
from kmk.modules.rgb import RGB

keyboard = KMKKeyboard()

# --- MODULES ---
macros = Macros()
keyboard.modules.append(macros)

encoder = RotaryEncoder()
keyboard.modules.append(encoder)

rgb = RGB(
    pixel_pin=board.GP29,    # DIN of SK6812MINI
    num_pixels=1,
    hue_default=0,
    sat_default=255,
    val_default=40,
)
keyboard.modules.append(rgb)

# --- SWITCH INPUT PINS ---
PINS = [
    board.GP1,   # SW1
    board.GP4,   # SW3
    board.GP3,   # SW4
    board.GP6,   # Encoder push button
]

keyboard.matrix = KeysScanner(
    pins=PINS,
    value_when_pressed=False,
)

# --- ROTARY ENCODER ---
encoder.pins = ((board.GP0, board.GP7),)
encoder.map = [
    (KC.VOLD, KC.VOLU),
]

# --- KEYMAP ---
keyboard.keymap = [
    [
        KC.N1,                   # SW1 → "1"
        KC.N2,                   # SW3 → "2"
        KC.N3,                   # SW4 → "3"
        KC.MEDIA_PLAY_PAUSE,     # Encoder press → Play / Pause
    ]
]

# --- RUN ---
if __name__ == '__main__':
    keyboard.go()
