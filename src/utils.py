logging = True

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