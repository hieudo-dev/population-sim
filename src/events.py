def Event(func):
	def wrapper(person):
		def f(simulator):
			return func(person, simulator)
		return f 
	return wrapper

@Event
def BirthDayEvent(person, simulator):
	person.age += 1
	simulator.AddEvent(person, BirthDayEvent, simulator.time + 12)

@Event
def GiveBirthEvent(person, simulator):
	childs = person.GiveBirth()
	print("X Gave birth at age ", person.age)
	for child in childs:
		simulator.population.append(child)
		simulator.AddEvent(child, BirthDayEvent, simulator.time + 12)
	simulator.births += childs.__len__()