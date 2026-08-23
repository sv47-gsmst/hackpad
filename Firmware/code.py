import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.encoder import EncoderHandler
from kmk.extensions.media_keys import MediaKeys



keyboard = KMKKeyboard()




keyboard.col_pins = (
    board.GP2,   # Column 1
    board.GP3,   # Column 2
    board.GP4,   # Column 3
)

keyboard.row_pins = (
    board.GP5,   # Row 1
    board.GP6,   # Row 2
)


keyboard.diode_orientation = DiodeOrientation.COL2ROW



keyboard.keymap = [
    [
        KC.PGUP,   # Key 1
        KC.UP,     # Key 2
        KC.PGDN,   # Button 3

        KC.LEFT,   # Key 4
        KC.DOWN,   # Key 5
        KC.RIGHT,  # Key 6
    ]
]



# Rotary encoder/Knob

encoder_handler = EncoderHandler()


encoder_handler.pins = (
    (
        board.GP1,   # Encoder A
        board.GP7,   # Encoder B
        board.GP9,   # Encoder push switch
    ),
)



encoder_handler.map = [
    (
        KC.VOLD,    # Counterclockwise- Volume Down
        KC.VOLU,    # Clockwise- Volume Up
        KC.NO,      # Encoder button- Mute
    ),
]

keyboard.modules.append(encoder_handler)


keyboard.extensions.append(MediaKeys())



if __name__ == "__main__":
    keyboard.go()