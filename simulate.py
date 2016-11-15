import arrivals
import servers
import probTable
from operator import add

arrivalFiles = ['arrivals/a830_9', 'arrivals/a9_930', 'arrivals/a930_10', 'arrivals/a10_1030', 'arrivals/a1030_11',
					'arrivals/a11_1130', 'arrivals/a1130_12', 'arrivals/a12_1230', 'arrivals/a1230_13', 'arrivals/a13_1330',
					'arrivals/a1330_1400', 'arrivals/a1400_1430', 'arrivals/a1430_1500', 'arrivals/a15_1530']

timePeriods = ['8:30-9', '9-9:30', '9:30-10', '10-10:30', '10:30-11', '11-11:30', '11:30-12', '12-12:30', '12:30-13',
				'13-13:30', '13:30-14', '14-14:30', '14:30-15', '15-15:30', '15:30-16', '16-16:30', '16:30-17']


salaryCost = 0
waitingCustomerCost = 0
customers = [0, 0, 0]
timeIdx = 0
remUsers = 0
for idx, arrival in enumerate(arrivalFiles):
	print "\nSimulating " + timePeriods[idx]
	arrivalDict =  probTable.generateDictOfProb(arrival)
	salaryCost = salaryCost + servers.calculateSalary()
	for i in range(30):
		print "\nSimulating minute ", i+1
		newCustomers, remArrivals =  arrivals.simulateArrivals(arrivalDict, remUsers)
		customers = map(add, customers, newCustomers)
		customers = servers.servePeople(customers)
		for idx, customer in enumerate(customers):
			waitingCustomerCost = waitingCustomerCost + customer * (idx * 0.2)
	timeIdx = timeIdx + 1

while customers != [0, 0, 0]:
	print "\nThere are still customers in the system. Working more..."
	print "\nSimulating " + timePeriods[timeIdx]
	timeIdx = timeIdx + 1
	customers = servers.servePeople(customers)
	salaryCost = salaryCost + servers.calculateSalary() * 2
	for idx, customer in enumerate(customers):
		waitingCustomerCost = waitingCustomerCost + customer * (idx * 0.4)
	if timeIdx == 17:
		for idx, customer in enumerate(customers):
			waitingCustomerCost = waitingCustomerCost + customer * (idx * 0.6)
		customers = [0, 0, 0]
		print "Customers had to be dispatched, this is too late."


print "Total cost of salaryCost: " , salaryCost
print "Total cost of waiting customers: " , waitingCustomerCost
print "Total cost: ", salaryCost + waitingCustomerCost