import probTable
import random 

arrivalDict =  probTable.generateDictOfProb('arrivals')
typeDict =  probTable.generateDictOfProb('typeOfClient')
serviceDict1 =  probTable.generateDictOfProb('service')
serviceDict2 =  probTable.generateDictOfProb('service2')
serviceDict3 =  probTable.generateDictOfProb('service3')


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

def attendPeople(customers):
	'''Attends a set of customers with a set of servers.'''
	serversForPref = [serviceDict1]
	serversForCust = [serviceDict2]
	serversForNoCust = [serviceDict3]

	serverLists = [serversForPref, serversForCust, serversForNoCust]
	
	'''
	This arrays defines the order in which each type of server attends
	Pref server attends with priority to preferencial, then customer, then no customer
	Cust server attends with priority to customers, then preferencial, then no customer
	No cust server attends with priority to no customers, then preferencial, then customer
	'''

	serverOrderList = [[2,1,0], [1,2,0], [0,2,1]]
	serverOrder = 0

	print customers
	for serverType in serverLists:
		for server in serverType:
			a = random.random()
			serverRate = int(probTable.getValueGivenNumber(server, a))	
			print serverRate
			for x in serverOrderList[serverOrder]:
				if(serverRate > customers[x]):
					serverRate = serverRate - customers[x]
					customers[x] = 0
				elif(serverRate < customers[x]):
					customers[x] = customers[x] - serverRate
					serverRate = 0
			print customers
		serverOrder = serverOrder + 1
		


customers = simulateArrivals(arrivalDict)
attendPeople(customers)
