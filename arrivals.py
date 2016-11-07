import probTable
import random 

arrivalDict =  probTable.generateDictOfProb('arrivals')
for i in range(10):
	a = random.random()
	print str(probTable.getValueGivenNumber(arrivalDict, a)) + " people arrived"
