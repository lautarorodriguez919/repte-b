input.onButtonPressed(Button.A, function on_button_pressed_a() {
    music._playDefaultBackground(music.builtInPlayableMelody(Melodies.Dadadadum), music.PlaybackMode.InBackground)
})
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    let melodia_personalizada = "G R F E D C"
    music.play(music.stringPlayable(melodia_personalizada, 100), music.PlaybackMode.UntilDone)
})
input.onGesture(Gesture.Shake, function movimiento() {
    let accelX = input.acceleration(Dimension.X)
    let accelY = input.acceleration(Dimension.Y)
    let nuevo_tempo = Math.sqrt(accelX * accelX + accelY * accelY)
    music.setTempo(nuevo_tempo)
})
