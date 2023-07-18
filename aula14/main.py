import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.config import Config

class MyWidget(BoxLayout):
    def press(self, btn):
        if (self.ids['text'].text == '0'):
            self.ids['text'].text = ''
        self.ids['text'].text += btn
        
    def clear(self):
        self.ids['text'].text = '0'
        
    def delete(self):
        self.ids['text'].text = self.ids['text'].text[:-1]
        
    def result(self):
        self.ids['text'].text = str(eval(self.ids['text'].text))

class BasicApp(App):
    def build(self):
        return MyWidget()

if __name__ == '__main__':
    Config.set('graphics','resizable',True)
    BasicApp().run()