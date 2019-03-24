from individuals import Female, Male, Person
from math import floor
from events import BirthDayEvent, GiveBirthEvent, MovingOn
from randoms import Uniform
from utils import logpop, logper, log, ExtractData, ResetLogFolder
import heapq


def IsDying(person):
	prob = 0
	if person.age < 12:
		prob = .25
	elif person.age < 45:
		prob = .1 if person is Male else .15
	elif person.age < 76:
		prob = .3 if person is Male else .35
	else:
		prob = .7 if person is Male else .65
	return Uniform() <= prob

class Simulator:
	population = []
	events = []
	eventKey = 0
	time = 0
	maxTime = 0

	# STATISTICS
	births = 0
	peakCount = 0
	deaths = 0
	avgPregnantAge = 0.0
	avgLifeExpectancy = 0.0


	def __init__(self, M, F, maxTime):
		self.GeneratePopulation(M, F)
		self.maxTime = maxTime
		
	def GeneratePopulation(self, M, F):
		self.population = []

		for i in range(M):
			rv = Uniform(12, 30)
			p = Male(floor(rv))
			self.population.append(p)
			self.AddEvent(p, BirthDayEvent)

		for i in range(F):
			rv = Uniform(12, 30)
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

			if not person.IsSingle():
				CrisisResult = person.HaveRelationshipCrisis()
				if CrisisResult:
					myDep, coupleDep, couple = CrisisResult
					self.AddEvent(person, MovingOn, self.time + myDep)
					self.AddEvent(couple, MovingOn, self.time + coupleDep)

			if type(person) is Female and not person.isPregnant:
				if person.TryForBaby(self.time):
					self.AddEvent(person, GiveBirthEvent, self.time + 9)

			if IsDying(person):
				person.isDead = True
				person.BreakUpCouple()
				self.population.remove(person)
				self.deaths += 1
				self.avgLifeExpectancy += person.age if self.avgLifeExpectancy != 0 else person.age * 2
				self.avgLifeExpectancy /= 2.0
				log("X Died at age ", person.age)

		logpop(self.population)
		log("Population: ", self.population.__len__())
		log("Deaths: ", self.deaths)
		log("Births: ", self.births)
		log("Peak Population: ", self.peakCount)
		log("Time: ", self.time)


ResetLogFolder()

for i in range(0,10000):
	s = Simulator(250,250, 1200)
	s.Execute()
	ExtractData(s)
