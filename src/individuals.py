from person import Person
from randoms import Uniform
from utils import log

class Male(Person):
	def FindCouple(self, population):
		for girl in population:
			if type(girl) is Female and self.Like(girl):
				self.GoOutWith(girl)
	

class Female(Person):
	isPregnant = False

	def TryForBaby(self, currentTime):

		if not self.IsSingle() and \
				self.childCount < min(self.DesiredChildrenCount(), self.couple.DesiredChildrenCount()):
			# Let's try for a baby :)
			prob = 0
			if self.age < 15:
				prob = .2
			elif self.age < 21:
				prob = .45
			elif self.age < 35:
				prob = .8
			elif self.age < 45:
				prob = .4
			elif self.age < 60:
				prob = .2
			elif self.age <= 125:
				prob = .05
			
			if Uniform() <= prob:
				self.isPregnant = True
				return True
		return False

	def GiveBirth(self):
		childCount = 0
		rv = Uniform()
		if rv < .7:
			childCount = 1
		elif rv < .86:
			childCount = 2
		elif rv < .94:
			childCount = 3
		elif rv < .98:
			childCount = 4
		else:
			childCount = 5

		childs = []
		for i in range(childCount):
			if Uniform() < .5:
				childs.append(Male())
			else:
				childs.append(Female())

		log("X gave birth at age ", self.age)
		self.isPregnant = False
		self.childCount += childs.__len__()
		return childs