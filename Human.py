class Human(object):
	"""docstring for Human"""
	def __init__(self, age,hairColor,eyeColor,skinColor,race):
		self.age = age
		self.hairColor = hairColor
		self.eyeColor = eyeColor
		self.skinColor = skinColor
		self.race = race

	def humanDefinition(self):
		print ("Hi im a human and I got: "+str(self.age)+" years on my back, im "+self.race+", with "+self.eyeColor+" eyes and im "+self.hairColor)

	def growUp(self):
		setattr(self,"age",age+1)

human1 = Human(22,"Black","Brown","Pale","Caucasian")
human1.humanDefinition()
print("hello")
