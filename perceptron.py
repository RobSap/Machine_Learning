import sys
import random
import csv
import random
from math import log



def perceptron( myList, bias, weightList, MaxIter, learningRate):
	for index in range(0,MaxIter):
		count =0
		random.shuffle(myList)
		for i in range(0,len(myList)):
				y=0.0
				a=0.0
				for j in range(0,len(myList[i]) -1):
#					print str(i)+ " " + str(j) + str(len(myList[i]))
					if(int(myList[i][j])==0):	
						a= a+  (weightList[j]*-1.0)
					else:
						a= a+ (weightList[j]*1.0)

			
				a = a+bias
				
				if(int(myList[i][-1])==0):
					y = -1.0
				else:
					y= 1.0		
				
				if(y*a <= 0.0):
					temp=0.0
					for k in range(0,len(myList[i])-1):		
						if(int(myList[i][k])==0):	
							temp=-1.0
						else:
							temp=1.0
						weightList[k] = weightList[k] + (y* temp)*learningRate
					bias = bias + y
				else:
					count = count +1
			
		if(count >= len(myList)):
			return weightList,bias

	#	print str(count) + " " + str(len(myList)-1)
	return weightList, bias


def checkZero(list):
	if(int(list)==0):
		temp = -1.0
	else:
		temp = 1.0

	return temp


def initializeWeights(trainingSet, weightList):
	for item in range(0, len( trainingSet) -1):
		#To randomize them (for better or worse results)
		weightList.append(random.uniform(-1.0,1.0))
		#To make all starting weights start at 0
		#weightList.append(0.0)
	return weightList

def perceptronTest(weights, bias, test):
#	print weights
#	print bias
#	print test[1]
	result = 0
	noresult=0
	for i in range(1,len(test)):
			a = 0.0
			for j in range(0,len(test[i]) -1):
	
				if(int(test[i][j])==0):
					a=a +(weights[j]*-1.0)
				else:	
					a=a +(weights[j]*1.0)
			
			a = a + bias	
	#		print a
			
			
			if(int(test[i][-1]) == 0 and a <=0.0):
				result = result + 1
#				print str(a) + " " + str(test[i][-1]) + "not fire"
		
			elif(int(test[i][-1]) == 1 and a >0.0):
				result = result +1
#				print str(a) + " " + str(test[i][-1]) + " fire"
			else:
				noresult = noresult + 1
#				print str(a) + " " + str(test[i][-1]) + "  ERROR"	


#	print "expected total " + str(total)
#	print "expected to fire " + str(count)

#	print "Result:" + str(result)
#	print "Miss / Error: " + str(noresult)
#	print "Total: " + str(result+noresult)
	correct = float(result)/ float(noresult+result)
#	error = float(noresult)/float(noresult+result)
#	print "accuracy = " + str(correct)
#	print "Percent error = " +   str(error)

#	print "bias " + str(bias)
	return correct





def main():
	try:
		trainingFile = sys.argv[1]
		validationFile = sys.argv[2]
		outputFile = sys.argv[3]
	except:
		print("Syntax: python " + str(sys.argv[0]) + " <training-set> <test-set> <model-file>")
		exit()

	trainingSet = []
	with open(trainingFile, 'r') as f:
		reader = csv.reader(f, delimiter=',')
		for row in reader:
			trainingSet.append(row)

	saveLabels = trainingSet[0]
	trainingSet.pop(0)	
	testSet = []
	with open(validationFile, 'r') as f:
		reader = csv.reader(f, delimiter=',')
		for row in reader:
			testSet.append(row)
	bias = 0.0
	weightList = []	
	weightList= initializeWeights(trainingSet[0] , weightList)
	
	MaxIter = 100
	learningRate = .5
	tuple = perceptron( trainingSet, bias, weightList, MaxIter, learningRate)

	
	print "Results will be printed to: " + outputFile
	sys.stdout = open(outputFile, "w")
	print "Bias =" + str( tuple[1])
	for i in range(0,len( weightList) -1):
		print saveLabels[i] + " " + str(weightList[i])

		
	print "accuracy = " + " " + str( perceptronTest(tuple[0], tuple[1], testSet))

main()



