import probTable
import random 

arrivalDict =  probTable.generateDictOfProb('arrivals')
typeDict =  probTable.generateDictOfProb('typeOfClient')

def generateTypeOfClient(amount):
	'''Receiving an amount of arrivals, decides which type of client it is'''
	clientCount = 0
	noClientCount = 0
	preferencialCount = 0
	for i in range(amount):
		a = random.random()
		typeOfCustomer = str(probTable.getValueGivenNumber(typeDict, a))
		if typeOfCustomer == "noClient":
			noClientCount += 1
		elif typeOfCustomer == "client":
			clientCount += 1
		else:
			preferencialCount += 1
	return [noClientCount, clientCount, preferencialCount]

def simulateArrivals():
	''' Simulates a random number of arrivals given the probability table.'''
	a = random.random()
	peopleAmount = int(probTable.getValueGivenNumber(arrivalDict, a))
	print str(peopleAmount) + " persons arrived"
	customers = generateTypeOfClient(peopleAmount)
	print customers

simulateArrivals()
