import kivy
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.core.window import Window
from kivy.properties import ObjectProperty

#Window.size = (414, 896) #xr scaled down
Window.size = (360, 760) #s10+ scaled down
#Window.size = (360, 844) #i12 scaled down
#Window.size = (375, 667) #generic scaled down

class FloatLayout(FloatLayout):
	btn = ObjectProperty(None)
	bar = ObjectProperty(None)
	weight = ObjectProperty(None)
	output = ObjectProperty(None)

	def DoTheThing(self):
		weight = int(self.weight.text) - int(self.bar.text)
		plates = {"45":0, "35":0, "25":0, "10":0, "5":0,"2.5":0}
		output = "Weights On Each Side:\n\n"
		if weight%10 == 5 or weight%10 == 0:
			while weight > 0: 
				if weight >= 90:
					plates["45"] += 1
					weight -= 90
					pass
				elif weight >= 70:
					plates["35"] += 1
					weight -= 70
					pass
				elif weight >= 50:
					plates["25"] += 1
					weight -= 50
					pass
				elif weight >= 20:
					plates["10"] += 1
					weight -= 20
					pass
				elif weight >= 10:
					plates["5"] += 1
					weight -= 10
					pass
				elif weight >=5:
					plates["2.5"] += 1
					weight -= 5
					pass
		else:
			output = "Incorrect Input"
		
		for plate in plates:
			if plates[plate] > 0:
				output += f"{plates[plate]}x{plate} lbs\n\n"
		self.output.text = output

class WeightPicker(App):

	def build(self):
		return FloatLayout()

	


if __name__ == "__main__":
	WeightPicker().run()