def on_button_pressed_a():
    music.play(music.tone_playable(196, music.beat(BeatFraction.WHOLE)),
        music.PlaybackMode.UNTIL_DONE)
    music.play(music.tone_playable(196, music.beat(BeatFraction.HALF)),
        music.PlaybackMode.UNTIL_DONE)
    music.play(music.tone_playable(220, music.beat(BeatFraction.WHOLE)),
        music.PlaybackMode.UNTIL_DONE)
    music.play(music.tone_playable(196, music.beat(BeatFraction.WHOLE)),
        music.PlaybackMode.UNTIL_DONE)
    music.play(music.tone_playable(262, music.beat(BeatFraction.WHOLE)),
        music.PlaybackMode.UNTIL_DONE)
    music.play(music.tone_playable(247, music.beat(BeatFraction.DOUBLE)),
        music.PlaybackMode.UNTIL_DONE)
    music.rest(music.beat(BeatFraction.WHOLE))
input.on_button_pressed(Button.A, on_button_pressed_a)
