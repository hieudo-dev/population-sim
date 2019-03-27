import os

logging = False

def logpop(pop):
	for i in pop:
		logper(i)

def logper(i):
	from individuals import Female
	if type(i) is Female:
		log("F ", i.age, i.IsSingle())
	else:
		log("M ", i.age, i.IsSingle())

def log(*args):
	if logging:
		print(*args)

def ResetLogFolder():
	f = open("log/remaining.txt", "w")
	f.write("remaining\n")
	f = open("log/avg_life_expectancy.txt", "w")
	f.write("age\n")
	f = open("log/endtime.txt", "w")
	f.write("time\n")
	f = open("log/pregnant_age.txt", "w")
	f.write("age\n")
	f = open("log/deaths.txt", "w")
	f.write("deaths\n")
	f = open("log/births.txt", "w")
	f.write("births\n")


def ExtractData(simulator):
	f = open("log/remaining.txt", "a")
	f.write(str(simulator.population.__len__()) + "\n")
	f = open("log/avg_life_expectancy.txt", "a")
	f.write(str(simulator.avgLifeExpectancy) + "\n")
	f = open("log/endtime.txt", "a")
	f.write(str(simulator.time) + "\n")
	f = open("log/pregnant_age.txt", "a")
	f.write(str(simulator.avgPregnantAge) + "\n")
	f = open("log/births.txt", "a")
	f.write(str(simulator.births) + "\n")
	f = open("log/deaths.txt", "a")
	f.write(str(simulator.deaths) + "\n")