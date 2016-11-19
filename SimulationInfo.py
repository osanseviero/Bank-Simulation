from operator import add

class SimulationInfo:
	def __init__(self):
		self.salaryCost = 0
		self.waitingCustomerCost = 0
		self.customers = [0, 0, 0]
		self.timeIdx = 0
		self.remUsers = 0

	def addSalary(self, aSalary):
		self.salaryCost = self.salaryCost + aSalary

	def addCustomers(self, newCustomers):
		self.customers = map(add, self.customers, newCustomers)

	def addWaitingCost(self, multiplier):
		for idx, customer in enumerate(self.customers):
				self.waitingCustomerCost = self.waitingCustomerCost + customer * (idx * multiplier)

	def isEmpty(self):
		if self.customers == [0, 0, 0]:
			return True
		else:
			return False