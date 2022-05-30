import kivy
from kivy.app import App
from kivy.graphics import Color, Ellipse
from kivy.uix.widget import Widget

kivy.require('2.1.0')  # replace with your current kivy version !


class MyPaintWidget(Widget):
    def on_touch_down(self, touch):
        with self.canvas:
            Color(1, 1, 0)
            d = 30.
            Ellipse(pos=(touch.x - d / 2, touch.y - d / 2), size=(d, d))


class MyPaintApp(App):

    def build(self):
        return MyPaintWidget()


if __name__ == '__main__':
    MyPaintApp().run()
