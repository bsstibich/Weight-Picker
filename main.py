import kivy
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.core.window import Window
#Window.size = (414, 896) #xr scaled down
Window.size = (360, 760) #s10+ scaled down
#Window.size = (360, 844) #i12 scaled down
#Window.size = (375, 667) #generic scaled down





class WeightPicker(App):
	def build(self):
		return FloatLayout()

if __name__ == "__main__":
	WeightPicker().run()