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
		wb.row = 0
		wb.col = 0
		worksheet = wb.getWorksheet(idx)

		wb.printBold(worksheet, "Time Period: ")
		wb.col = 2
		wb.printBold(worksheet, timePeriods[idx])
		wb.col = 0
		wb.row += 5

		# Create the dictionary of arrivals
		arrivalDict =  probTable.generateDictOfProb(arrival)
		wb.printBold(worksheet, "Cumulative Probability Table of Arrivals current Time Period: ")
		wb.row += 1
		for key, value in arrivalDict.iteritems():
			worksheet.write(wb.row, wb.col, value)
			wb.col = 1
			worksheet.write(wb.row, wb.col, key)
			wb.row += 1
			wb.col = 0

		wb.row += 5

		simInfo.addSalary(servers.calculateSalary()/2)

		# Simulates 30 minutes with the arrival rate
		for i in range(30):
			wb.printBold(worksheet, "Simulating minute: " + str(i+1))
			wb.row += 1
			newCustomers, simInfo.remUsers =  arrivals.simulateArrivals(arrivalDict, simInfo.remUsers, wb, worksheet)
			simInfo.addCustomers(newCustomers)

			simInfo.customers = servers.servePeople(simInfo.customers, wb, worksheet)
			simInfo.addWaitingCost(0.03)     
		simInfo.timeIdx = simInfo.timeIdx + 1

def simulateAfterHours(simInfo, wb):
	'''After the bank closes for new customers, the other customers need to be dispatched'''
	ws = wb.worksheet15
	wb.row = 0
	wb.col = 0
	while not simInfo.isEmpty():
		wb.printBold(ws, "There are still customers in the system. Servers need to work more (this is costly).")
		wb.row += 1
		wb.printBold(ws, "Simulating " + timePeriods[simInfo.timeIdx])
		wb.row += 2

		simInfo.timeIdx = simInfo.timeIdx + 1
		simInfo.customers = servers.servePeople(simInfo.customers, wb, ws)
		simInfo.addSalary(servers.calculateSalary())
		for i in range(30):
			if(not simInfo.isEmpty()):
				wb.printBold(ws, "Simulating minute: " + str(i+1))
				wb.row += 1
				simInfo.customers = servers.servePeople(simInfo.customers, wb, ws)
				simInfo.addWaitingCost(0.8)
		if simInfo.timeIdx == 16:
			simInfo.addWaitingCost(2)
			simInfo.customers = [0, 0, 0]
			wb.printBold(ws, "Customers had to be dispatched, this is too late.")

simulateArrivalHours(simInfo, ws)
simulateAfterHours(simInfo, ws)

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