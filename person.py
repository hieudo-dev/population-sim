class Person:
	age = 0
	couple = None
	isDead = False
	childCount = 0
	coupleReadyTime = -1			# Simulator's time at which this person will be available

	def __init__(self, age=0):
		self.age = age

	def isSingle(self):
		return self.couple == None

	


	def FindCouple(self, population):
		pass


	def WantsCouple(self):
		pass

	def SuitableCouple(self, individual):
		pass

	def MakeCouple(self, individual):
		pass

	def BreakUpCouple(self):
		pass
	

	def WantsMoreChildren(self):
		pass

	def DesiredChildrenCount(self):
		pass