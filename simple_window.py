import pyglet
import sys

class SimpleWindow(pyglet.window.Window):
    def on_key_press(self, symbol, modifiers):
        print('key pressed: {0}'.format(str(symbol)))
        sys.stdout.flush()

    def on_key_release(self, symbol, modifiers):
        print('key released: {0}'.format(str(symbol)))
        sys.stdout.flush()

    def on_mouse_motion(self, x, y, dx, dy):
        print('mouse moved: dx={0}, dy={1}'.format(dx, dy))
        sys.stdout.flush()

window = SimpleWindow()
pyglet.app.run()
