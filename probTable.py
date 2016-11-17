import collections

def generateDictOfProb(textFile):
	'''Generates a hash that maps cumulative probabilities to other data.'''
	f = open(textFile +'.txt', 'r')
	arrivalDict = {}
	prevProb = 0
	for line in f:
		nums = line.split()
		arrivalDict[float(nums[0])+prevProb] = nums[1]
		prevProb = float(nums[0]) + prevProb

	return collections.OrderedDict(sorted(arrivalDict.items()))

def generateDictOfProbJSON(json):
	'''Generates a hash that maps cumulative probabilities to other data.'''
	arrivalDict = {}
	prevProb = 0
	for key, value in json.iteritems():
		arrivalDict[float(value)+prevProb] = key
		prevProb = float(value) + prevProb

	return collections.OrderedDict(sorted(arrivalDict.items()))

def getValueGivenNumber(dict, num):
	''' Given a dictionary and a random number, return the value associated with the dict'''
	for key, value in dict.iteritems():
		if(num < key):
			return value
