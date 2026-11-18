from kivy.app import App
from kivy.uix.label import Label

class MonitorPatioApp(App):
    def build(self):
        return Label(text='Monitor Pátio - Rodando com Sucesso!')

if __name__ == '__main__':
    MonitorPatioApp().run()
  
