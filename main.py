from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.anchorlayout import MDAnchorLayout
from kivy.properties import ObjectProperty
from kivymd.uix.screen import MDScreen
from kivymd.uix.label import MDLabel
from kivy.clock import Clock

Builder.load_file('style.kv')

class Style(MDAnchorLayout):
    manager=ObjectProperty()
    fake=ObjectProperty()
    back=ObjectProperty()
    number=1 

    def change_screen(self):
        self.manager.current='fake'
        Clock.schedule_interval(self.change_text,0.2) 
    
    def change_text(self,*args):
        if self.number==22:
            self.fake.text=''
        else:
            self.back.source=str(self.number)+'.jpg'
            self.fake.text=str(self.number)
            self.number+=1

class MainApp(MDApp):

    def build(self):
        self.theme_cls.theme_style='Dark'

        return Style()
    

MainApp().run()

