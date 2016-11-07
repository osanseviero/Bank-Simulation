import arrivals
import servers
import probTable

arrivalDict =  probTable.generateDictOfProb('arrivals')
customers = arrivals.simulateArrivals(arrivalDict)
servers.servePeople(customers)