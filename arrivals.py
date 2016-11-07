import probTable
import random 

typeDict =  probTable.generateDictOfProb('typeOfClient')

def generateTypeOfClient(amount, dict):
	'''Receiving an amount of arrivals, decides which type of client it is'''
	clientCount = 0
	noClientCount = 0
	preferencialCount = 0
	for i in range(amount):
		a = random.random()
		typeOfCustomer = str(probTable.getValueGivenNumber(dict, a))
		if typeOfCustomer == "noClient":
			noClientCount += 1
		elif typeOfCustomer == "client":
			clientCount += 1
		else:
			preferencialCount += 1
	return [noClientCount, clientCount, preferencialCount]

def simulateArrivals(dict):
	''' Simulates a random number of arrivals given the probability table.'''
	a = random.random()
	peopleAmount = int(probTable.getValueGivenNumber(dict, a))
	print str(peopleAmount) + " persons arrived"
	customers = generateTypeOfClient(peopleAmount, typeDict)
	return customers



