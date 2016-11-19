import probTable
import random 
import arrivals
import parseServerJson
import sys

typeDict =  probTable.generateDictOfProb('typeOfClient')
serverList =  parseServerJson.generateServerList('serverConfigs/' + str(sys.argv[1]) + '.json')

serversForPref = []
serversForCust = []
serversForNoCust = []

for server in serverList:
	if server.attend == "pref":
		serversForPref.append(server)
	elif server.attend == "customer":
		serversForCust.append(server)
	else:
		serversForNoCust.append(server)

serverLists = [serversForPref, serversForCust, serversForNoCust]
serverOrderList = [[2,1,0], [1,2,0], [0,2,1]]

def servePeople(customers):
	'''Attends a set of customers with a set of servers.'''
	serverId = 0

	print "Customers: " , customers
	for serverType in serverLists:
		for server in serverType:
			a = random.random()
			serverRate = float(probTable.getValueGivenNumber(server.serveRates, a))
			print server.name + " will attend " , serverRate , server.attend
			for x in serverOrderList[serverId]:
				if(serverRate > customers[x]):
					serverRate = serverRate - customers[x]
					customers[x] = 0
				elif(serverRate < customers[x]):
					customers[x] = customers[x] - serverRate
					serverRate = 0
			print customers
		serverId = serverId + 1
	return customers
		
def calculateSalary():
	cost = 0
	for server in serverList:
		cost = cost + server.hourSalary
	return cost





