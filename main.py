
def on_button_pressed_a():
    music._play_default_background(music.built_in_playable_melody(Melodies.DADADADUM), music.PlaybackMode.IN_BACKGROUND)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    melodia_personalizada = "G R F E D C"
    music.play(music.string_playable(melodia_personalizada, 100), music.PlaybackMode.UNTIL_DONE)
input.on_button_pressed(Button.B, on_button_pressed_b)

def movimiento():
    accelX=input.acceleration(Dimension.X)
    accelY=input.acceleration(Dimension.Y)
    nuevo_tempo = Math.sqrt((accelX * accelX) + (accelY * accelY))
    music.set_tempo(nuevo_tempo)
input.on_gesture(Gesture.SHAKE, movimiento)