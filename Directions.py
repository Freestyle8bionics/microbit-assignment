# Add your code here
from huskylens import Husk
huskylens.init_i2c()
huskylens.init_mode(protocolAlgorithm.ALGORITHM_OBJECT_TRACKING)

def on_forever():
    huskylens.request()
    if huskylens.is_appear(1, HUSKYLENSResultType_t.HUSKYLENS_RESULT_BLOCK):
        if huskylens.reade_box(1, Content1.X_CENTER) < 140:
            if huskylens.reade_box(1, Content1.Y_CENTER) < 100:
                basic.show_leds("""
                    # . . . .
                    . . . . .
                    . . . . .
                    . . . . .
                    . . . . .
                    """)
            elif huskylens.reade_box(1, Content1.Y_CENTER) > 140:
                basic.show_leds("""
                    . . . . .
                    . . . . .
                    . . . . .
                    . . . . .
                    # . . . .
                    """)
            else:
                basic.show_leds("""
                    . . . . .
                    . . . . .
                    # . . . .
                    . . . . .
                    . . . . .
                    """)
        elif huskylens.reade_box(1, Content1.X_CENTER) > 180:
            if huskylens.reade_box(1, Content1.Y_CENTER) < 100:
                basic.show_leds("""
                    . . . . #
                    . . . . .
                    . . . . .
                    . . . . .
                    . . . . .
                    """)
            elif huskylens.reade_box(1, Content1.Y_CENTER) > 140:
                basic.show_leds("""
                    . . . . .
                    . . . . .
                    . . . . .
                    . . . . .
                    . . . . #
                    """)
            else:
                basic.show_leds("""
                    . . . . .
                    . . . . .
                    . . . . #
                    . . . . .
                    . . . . .
                    """)
        else:
            if huskylens.reade_box(1, Content1.Y_CENTER) < 100:
                basic.show_leds("""
                    . . # . .
                    . . . . .
                    . . . . .
                    . . . . .
                    . . . . .
                    """)
            elif huskylens.reade_box(1, Content1.Y_CENTER) > 140:
                basic.show_leds("""
                    . . . . .
                    . . . . .
                    . . . . .
                    . . . . .
                    . . # . .
                    """)
            else:
                basic.show_leds("""
                    . . . . .
                    . . . . .
                    . . # . .
                    . . . . .
                    . . . . .
                    """)
    else:
        basic.show_icon(IconNames.SAD)
basic.forever(on_forever)
