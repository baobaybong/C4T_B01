import datetime
import pyglet
sound = pyglet.media.load("Sample.wav")
alarmed = False
while not alarmed:
    now = str(datetime.datetime.now().time())
    if now >= "18:09:00.0":
        alarmed = True
        sound.play()
        pyglet.app.run()