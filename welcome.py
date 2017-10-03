from kivy.app import App
from kivy.uix.label import Label

class MyApp(App):
	
	def build(App):
		return Label(text="Welcome to Nana Rover Spaceland")
		
		
if __name__=="__main__":
	MyApp().run()
