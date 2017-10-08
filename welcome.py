from kivy.app import App
from kivy.uix.label import Label
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.uix.gridlayout import GridLayout
from kivy.properties import NumericProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout


class WelcomeScreen(FloatLayout):

	def __init__(self, **kwargs):
		super(WelcomeScreen, self).__init__(**kwargs)
		
		self.add_widget(Label())
		
		self.add_widget(Button(text="Enter"))
		
		#self.BoxLayout(orientation="vertical")
		#label=Label(text="Welcome")
					


p = Builder.load_file("myapp.kv")


class MainApp(App):
	
	def build(self):
		return p
	


if __name__=="__main__":
	MainApp().run()
