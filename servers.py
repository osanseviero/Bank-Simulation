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

def servePeople(customers, wb, ws):
	'''Attends a set of customers with a set of servers.'''
	serverId = 0

	wb.row += 1
	wb.printBold(ws, "Customers at this point: ")
	wb.row +=1

	ws.write(wb.row, wb.col, "No Customer: ")
	ws.write(wb.row, wb.col+1, customers[0])
	wb.row += 1

	ws.write(wb.row, wb.col, "Customer: ")
	ws.write(wb.row, wb.col+1, customers[1])
	wb.row += 1

	ws.write(wb.row, wb.col, "Preferencial: ")
	ws.write(wb.row, wb.col+1, customers[2])
	wb.row += 2

	for serverType in serverLists:
		for server in serverType:
			a = random.random()
			serverRate = float(probTable.getValueGivenNumber(server.serveRates, a))
			text = server.name + " will attend " + str(serverRate) + ' giving priority to: ' + str(server.attend)
			ws.write(wb.row, wb.col, text)
			wb.row += 1
			for x in serverOrderList[serverId]:
				if(serverRate > customers[x]):
					serverRate = serverRate - customers[x]
					customers[x] = 0
				elif(serverRate < customers[x]):
					customers[x] = customers[x] - serverRate
					serverRate = 0
		serverId = serverId + 1

	wb.row += 1
	wb.printBold(ws, "Customers after serving:: ")
	wb.row +=1

	ws.write(wb.row, wb.col, "No Customer: ")
	ws.write(wb.row, wb.col+1, customers[0])
	wb.row += 1

	ws.write(wb.row, wb.col, "Customer: ")
	ws.write(wb.row, wb.col+1, customers[1])
	wb.row += 1

	ws.write(wb.row, wb.col, "Preferencial: ")
	ws.write(wb.row, wb.col+1, customers[2])
	wb.row += 4

	return customers
		
def calculateSalary():
	cost = 0
	for server in serverList:
		cost = cost + server.hourSalary
	return cost





