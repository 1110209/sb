input.onButtonPressed(Button.A, function () {
    for (let index = 0; index < 3; index++) {
        basic.showLeds(`
            . # # # .
            . . # . .
            . . # . .
            . . # . .
            . # # # .
            `)
        basic.showLeds(`
            . # . # .
            # . # . #
            # . . . #
            . # . # .
            . . # . .
            `)
        basic.showLeds(`
            # . . . #
            # . . . #
            # . . . #
            # . . . #
            . # # # .
            `)
    }
})
input.onButtonPressed(Button.AB, function () {
    basic.showIcon(IconNames.Happy)
})
input.onButtonPressed(Button.B, function () {
    for (let index = 0; index < 3; index++) {
        basic.showIcon(IconNames.SmallHeart)
        basic.showIcon(IconNames.Heart)
        basic.showString("SB")
    }
})
