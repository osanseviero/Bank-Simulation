class Server:
	def __init__(self, parsed_json):
		self.name = parsed_json["name"]
		self.hourSalary = parsed_json["hourSalary"]
		self.attend = parsed_json["attend"]
		self.serveRates = parsed_json["serveRate"]

	def printData(self):
		print "Server name: " + self.name
		print "Hour salary " + str(self.hourSalary)
		print "This server attends: " + self.attend
		print "The rates of serving are: " , self.serveRates
		print "______"