from randoms import Exponential, Uniform
from math import ceil, floor

class Person:
	age = 0
	couple = None
	isDead = False
	isSad = False
	childCount = 0

	def __init__(self, age=0):
		self.age = age

	def IsSingle(self):
		return self.couple == None


	def WantsCouple(self):
		prob = 0
		if 12 <= self.age and self.age < 15:
			prob = .6
		elif self.age < 21:
			prob = .65
		elif self.age < 35:
			prob = .8
		elif self.age < 45:
			prob = .6
		elif self.age < 60:
			prob = .5
		elif self.age < 125:
			prob = .2
			
		return Uniform() <= prob

	def Like(self, individual):
		return not self.isSad and self.age >= 12 and self.IsSingle() and self.WantsCouple() and \
			not individual.isSad and individual.age >= 12 and	individual.IsSingle() and individual.WantsCouple()

	def GoOutWith(self, individual):
		ageDif = abs(self.age - individual.age)
		prob = 0
		if ageDif < 5:
			prob = .45
		elif ageDif < 10:
			prob = .4
		elif ageDif < 15:
			prob = .35
		elif ageDif < 20:
			prob = .25
		else:
			prob = .15
		
		if Uniform() <= prob:
			# They are officially a couple
			self.couple = individual
			individual.couple = self
			return True
			
		return False

	def HaveRelationshipCrisis(self):
		# The crisis can make the couple break up
		if Uniform() <= .2:
			# Break up :(
			self.BreakUpCouple()
			
	def HeartbreakDuration(self):
		lmda = 0
		if 12 < self.age and self.age < 15:
			lmda =  3
		elif self.age < 21:
			lmda = 6
		elif self.age < 35:
			lmda = 9
		elif self.age < 45:
			lmda = 12
		elif self.age < 60:
			lmda = 24
		elif self.age < 125:
			lmda = 48
			
		rv = Exponential(1 / lmda)
		return ceil(rv) if rv - floor(rv) >= .5 else floor(rv)

	def BreakUpCouple(self):
		if not self.IsSingle():
			self.couple.couple = None
			self.couple = None
		

	def WantsMoreChildren(self):
		return self.childCount < self.DesiredChildrenCount()

	def DesiredChildrenCount(self):
		# Amount of children:
		# 1: .20 
		# 2: .55 
		# 3: .15
		# 4: .8 
		# 5: .2
		rv = Uniform()
		if rv <= .2:
			return 1
		elif rv <= .75:
			return 2
		elif rv <= .90:
			return 3
		elif rv <= 98:
			return 4
		return 5