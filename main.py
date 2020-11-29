import kivy
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.core.window import Window
Window.size = (360, 640)

class WeightPicker(App):
	def build(self):
		return FloatLayout()

if __name__ == "__main__":
	WeightPicker().run()