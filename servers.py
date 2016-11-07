import probTable
import random 
import arrivals

typeDict =  probTable.generateDictOfProb('typeOfClient')


'''
The next part should later be refactored so it just reads one file with all the info.

This arrays defines the order in which each type of server attends
Pref server attends with priority to preferencial, then customer, then no customer
Cust server attends with priority to customers, then preferencial, then no customer
No cust server attends with priority to no customers, then preferencial, then customer
'''

server0 =  probTable.generateDictOfProb('server')
server1 =  probTable.generateDictOfProb('server1')
server2 =  probTable.generateDictOfProb('server2')
server3 =  probTable.generateDictOfProb('server3')

serversForPref = [server0, server1]
serversForCust = [server2]
serversForNoCust = [server3]

serverLists = [serversForPref, serversForCust, serversForNoCust]

serverOrderList = [[2,1,0], [1,2,0], [0,2,1]]


def servePeople(customers):
	'''Attends a set of customers with a set of servers.'''
	serverId = 0

	print customers
	for serverType in serverLists:
		for server in serverType:
			a = random.random()
			serverRate = int(probTable.getValueGivenNumber(server, a))	
			print serverRate
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
		



