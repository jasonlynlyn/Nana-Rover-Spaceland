import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty




class ScreenTwo(Screen):
	pass


class ScreenOne(Screen):
	pass


class Manager(ScreenManager):
	
	screen_one=ObjectProperty(None)
	screen_two=ObjectProperty(None)
	




class ScreenApp(App):

	def build(self):
		return Manager()
		
if __name__=="__main__":
	ScreenApp().run()
