class Human(object):
	"""docstring for Human"""
	def __init__(self, age,hairColor,eyeColor,skinColor,race):
		self.age = age
		self.hairColor = hairColor
		self.eyeColor = eyeColor
		self.skinColor = skinColor
		race = race

	def humanDefinition(self):
		return "Hi im a human and I got: "+age+" years on my back, im "+race+", with "+eyeColor+" eyes and im "+hairColor+""

	def growUp(self):
		setattr(self,"age",age+1)

human1 = Human(22,"Black","Brown","Pale","Caucasian")
print(human1.humanDefinition)


