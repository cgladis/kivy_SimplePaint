import kivy
from kivy.app import App
from kivy.uix.widget import Widget

kivy.require('2.1.0')  # replace with your current kivy version !


class MyPaintWidget(Widget):
    pass


class MyPaintApp(App):

    def build(self):
        return MyPaintWidget()


if __name__ == '__main__':
    MyPaintApp().run()
