import collections

def generateDictOfProb(textFile):
	'''Generates a hash that maps cumulative probabilities to other data.'''
	f = open(textFile +'.txt', 'r')
	arrivalDict = {}
	prevProb = 0
	for line in f:
		nums = line.split()
		arrivalDict[float(nums[0])+prevProb] = int(nums[1])
		prevProb = float(nums[0]) + prevProb

	return collections.OrderedDict(sorted(arrivalDict.items()))

def getValueGivenNumber(dict, num):
	''' Given a dictionary and a random number, return the value associated with the dict'''
	for key, value in dict.iteritems():
		if(num < key):
			return value

