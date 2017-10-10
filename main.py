from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.scatter import Scatter 
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image

class SimpleApp(App):
	
	
	def build(self): 
		f=FloatLayout()
		b=Button(text="enter", 
				font_size=30)
		i=Image(source="enter.jpg")
		f.add_widget(i)
		i.add_widget(b)
		
		return f
	
	
if __name__=="__main__":
	SimpleApp().run()
