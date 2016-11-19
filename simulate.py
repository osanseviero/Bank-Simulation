import arrivals
import servers
import probTable
from SimulationInfo import SimulationInfo
from WorkSheet import WorkSheet

arrivalFiles = ['arrivals/a830_9', 'arrivals/a9_930', 'arrivals/a930_10', 'arrivals/a10_1030', 'arrivals/a1030_11',
					'arrivals/a11_1130', 'arrivals/a1130_12', 'arrivals/a12_1230', 'arrivals/a1230_13', 'arrivals/a13_1330',
					'arrivals/a1330_1400', 'arrivals/a1400_1430', 'arrivals/a1430_1500', 'arrivals/a15_1530']

timePeriods = ['8:30-9', '9-9:30', '9:30-10', '10-10:30', '10:30-11', '11-11:30', '11:30-12', '12-12:30', '12:30-13',
				'13-13:30', '13:30-14', '14-14:30', '14:30-15', '15-15:30', '15:30-16', '16-16:30', '16:30-17']


simInfo = SimulationInfo()
ws = WorkSheet()

def simulateArrivalHours(simInfo, wb):
	'''Receives customers and then serve them'''

	for idx, arrival in enumerate(arrivalFiles):
		print "\nSimulating " + timePeriods[idx]
		row = 0
		col = 0
		worksheet = wb.getWorksheet(idx)


		wb.printBold(worksheet, row, col, "Time Period: ")
		wb.printBold(worksheet, row, col+1, timePeriods[idx])
		row += 2

		arrivalDict =  probTable.generateDictOfProb(arrival)
		wb.printBold(worksheet, row, col, "Cumulative Probability Table: ")
		row += 1
		for key, value in arrivalDict.iteritems():
			worksheet.write(row, col, value)
			worksheet.write(row, col+1, key)
			row += 1
		simInfo.addSalary(servers.calculateSalary()/2)
		for i in range(30):
			print "\nSimulating minute ", i+1
			newCustomers, simInfo.remUsers =  arrivals.simulateArrivals(arrivalDict, simInfo.remUsers)
			simInfo.addCustomers(newCustomers)
			simInfo.customers = servers.servePeople(simInfo.customers)
			simInfo.addWaitingCost(0.03)
		simInfo.timeIdx = simInfo.timeIdx + 1

def simulateAfterHours(simInfo):
	'''After the bank closes for new customers, the other customers need to be dispatched'''
	while not simInfo.isEmpty():
		print "\nThere are still customers in the system. Working more..."
		print "\nSimulating " + timePeriods[simInfo.timeIdx]
		simInfo.timeIdx = simInfo.timeIdx + 1
		simInfo.customers = servers.servePeople(simInfo.customers)
		simInfo.addSalary(servers.calculateSalary())
		for i in range(30):
			if(not simInfo.isEmpty()):
				print "\nSimulating minute ", i+1
				simInfo.customers = servers.servePeople(simInfo.customers)
				simInfo.addWaitingCost(0.8)
		if simInfo.timeIdx == 16:
			simInfo.addWaitingCost(2)
			simInfo.customers = [0, 0, 0]
			print "\nCustomers had to be dispatched, this is too late."


simulateArrivalHours(simInfo, ws)
simulateAfterHours(simInfo)

ws.analysis.write('A1', 'Total cost of salary cost')
ws.analysis.write('B1', simInfo.salaryCost)
ws.analysis.write('A2', 'Total cost of waiting customers')
ws.analysis.write('B2', simInfo.waitingCustomerCost)
ws.analysis.write('A3', 'Total cost: ')
ws.analysis.write('B3', simInfo.salaryCost + simInfo.waitingCustomerCost)

ws.close()

print "Total cost of salaryCost: " , simInfo.salaryCost
print "Total cost of waiting customers: " , simInfo.waitingCustomerCost
print "Total cost: ", simInfo.salaryCost + simInfo.waitingCustomerCost