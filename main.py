def on_button_pressed_a():
    for index in range(3):
        basic.show_leds("""
            . # # # .
            . . # . .
            . . # . .
            . . # . .
            . # # # .
            """)
        basic.show_leds("""
            . # . # .
            # . # . #
            # . . . #
            . # . # .
            . . # . .
            """)
        basic.show_leds("""
            # . . . #
            # . . . #
            # . . . #
            # . . . #
            . # # # .
            """)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    basic.show_icon(IconNames.HAPPY)
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    for index2 in range(3):
        basic.show_icon(IconNames.SMALL_HEART)
        basic.show_icon(IconNames.HEART)
        basic.show_string("SB")
input.on_button_pressed(Button.B, on_button_pressed_b)
