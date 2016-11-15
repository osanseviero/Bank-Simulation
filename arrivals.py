import probTable
import random 

typeDict =  probTable.generateDictOfProb('typeOfClient')

def generateTypeOfClient(amount, dict):
	''' Decides which type of client arrives
		parameter: amount, # of people that arrive and dict, a dictionary of probability to decide the type of user
		returns: an array with the count for each type of client and the float number of users left (for the next run)
	'''
	clientCount = 0
	noClientCount = 0
	preferencialCount = 0
	for i in range(int(amount)):
		a = random.random()
		typeOfCustomer = str(probTable.getValueGivenNumber(dict, a))
		if typeOfCustomer == "noClient":
			noClientCount += 1
		elif typeOfCustomer == "client":
			clientCount += 1
		else:
			preferencialCount += 1
	return [noClientCount, clientCount, preferencialCount], amount%1

def simulateArrivals(dict, remUsers):
	''' Simulates a random number of arrivals given the probability table.'''
	a = random.random()
	peopleAmount = float(probTable.getValueGivenNumber(dict, a))
	print str(peopleAmount + remUsers) + " persons arrived"
	customers, rem = generateTypeOfClient(peopleAmount + remUsers, typeDict)
	return customers, rem



