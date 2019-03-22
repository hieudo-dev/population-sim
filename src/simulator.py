from individuals import Female, Male, Person
from math import floor
from events import BirthDayEvent, GiveBirthEvent
from utils import logpop, logper, log
import heapq
import numpy as nmp

# Edad <  |   M   |    F 
#   12    |     .0005 
#   45    |  .001 | .002
#   76    |  .01  | .02
#   125   |  .1   | .2

def IsDying(person):
	prob = 0
	if person.age < 12:
		prob = .0005
	elif person.age < 45:
		prob = .001 if person is Male else .002
	elif person.age < 76:
		prob = .01 if person is Male else .02
	else:
		prob = .1 if person is Male else .2
	return nmp.random.uniform() <= prob

class Simulator:
	population = []
	events = []
	eventKey = 0
	time = 0
	maxTime = 0
	births = 0
	peakCount = 0
	deaths = 0

	def __init__(self, M, F, maxTime):
		self.GeneratePopulation(M, F)
		self.maxTime = maxTime
		
	def GeneratePopulation(self, M, F):
		self.population = []

		for i in range(M):
			rv = nmp.random.uniform(12, 30)
			p = Male(floor(rv))
			self.population.append(p)
			self.AddEvent(p, BirthDayEvent)

		for i in range(F):
			rv = nmp.random.uniform(12, 30)
			p = Female(floor(rv))
			self.population.append(p)
			self.AddEvent(p, BirthDayEvent)
			

	def AddEvent(self, person, event, time=-1):
		time = self.time if time == -1 else time
		self.eventKey += 1
		heapq.heappush(self.events, (time, self.eventKey, person, event(person)))


	def Execute(self):
		logpop(self.population)
		while self.events != []:
			time, secondarykey, person, event = heapq.heappop(self.events)
			self.time = time
			self.peakCount = max(self.peakCount, self.population.__len__())
			if time > self.maxTime:
				self.time = self.maxTime
				break

			if person.isDead:
				continue

			event(self)
			
			if type(person) is Male and person.age >= 12:
				person.FindCouple(self.population)

			if type(person) is Male and not person.IsSingle():
				person.HaveRelationshipCrisis()

			if type(person) is Female and not person.isPregnant:
				if person.TryForBaby(self.time):
					self.AddEvent(person, GiveBirthEvent, self.time + 9)


			if IsDying(person):
				person.BreakUpCouple()
				person.isDead = True
				self.population.remove(person)
				self.deaths += 1
				log("X Died at age ", person.age)

		# logpop(self.population)
		log("Population: ", self.population.__len__())
		log("Deaths: ", self.deaths)
		log("Births: ", self.births)
		log("Peak Population: ", self.peakCount)
		log("Time: ", self.time)

logging = True
s = Simulator(10,10, 1200)
s.Execute()
