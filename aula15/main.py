import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.config import Config

class MyWidget(BoxLayout):
    pass

class BasicApp(App):
    def build(self):
        return MyWidget()

if __name__ == '__main__':
    Config.set('graphics','resizable',True)
    BasicApp().run()