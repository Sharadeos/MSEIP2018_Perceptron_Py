import random

learningRate = 0.05
epoch = 10
input = 4
weights = []
bias = 0
correctCounter = 0
epochcounter = 0


def signActivation(input):
	if input >= 0:
		return 1.0;
	else:
		return -1.0;
		
def backPropagation(inputlist):
	global bias
	global weights
	loop = 0
	X = 0

	while(loop < input):
		X += inputlist[loop] * weights[loop]
		loop+=1
			
	X -= bias
	#X = (inputlist[0] * weights[0]) + (inputlist[1] * weights[1]) + (inputlist[2] * weights[2]) + (inputlist[3] * weights[3]) - bias
	Y = signActivation(X)
	print(X)
	error = inputlist[4] - Y
	
	
	
	backcount = 0
	
	while(backcount < input):
		weights[backcount] = weights[backcount] + (learningRate * inputlist[backcount]) * error
		backcount+=1
	#weights[0] = weights[0] + (learningRate * inputlist[0] * error)
	#weights[1] = weights[1] + (learningRate * inputlist[1] * error)
	#weights[2] = weights[2] + (learningRate * inputlist[2] * error)
	#weights[3] = weights[2] + (learningRate * inputlist[3] * error)
	bias += (learningRate * (-1) * error)
#we are using global variables right now hence no need to pass the weights
		#backcount+=1
	#print("Error: ", error, "Weight 0: ", weights[0], "Weight 1: ", weights[1], "Weight 2: ", weights[2], "Weight 3: ", weights[3])
	#backcount +=1
	
def checkWeights(inputlist):

	global bias
	global weights
	loop = 0
	X = 0

	while(loop < input):
		X += inputlist[loop] * weights[loop]
		loop+=1
			
	X -= bias
	Y = signActivation(X)

	if(Y == inputlist[4]):
		
		return 1;
	else:
		
		return 0;
	
	
	

#intialialze the random weights at the start
count = 0
while(count < input):
	weights.append(random.uniform(-1, 1))
	print("Weight",count, ": ", weights[count])
	count+=1

bias = random.uniform(-1, 1)
	
print("Bias:",bias)

	
	
import csv
epochcounter = 0	
while(epochcounter < epoch):	
	with open('iris-binary-normalized.csv', newline='') as csvfile:
		csvreader = csv.reader(csvfile, delimiter=',')
		
		for row in csvreader:
			slength = float(row[0])
			swidth = float(row[1])
			plength = float(row[2])
			pwidth = float(row[3])
			label = int(row[4])
				
			inputlist = [slength, swidth, plength, pwidth, label]
			#print(inputlist)
			backPropagation(inputlist)
			#section where we adjust the weights
			#print(epochcounter)
	epochcounter+=1
		

			

with open('iris-binary-normalized.csv', newline='') as csvfile:
	csvreader = csv.reader(csvfile, delimiter=',')
	#row_count = sum(1 for row in csvreader)
	#print(row_count)
	for row in csvreader:
		slength = float(row[0])
		swidth = float(row[1])
		plength = float(row[2])
		pwidth = float(row[3])
		label = int(row[4])
			
		inputlist = [slength, swidth, plength, pwidth, label]			
		correctCounter += checkWeights(inputlist)
			
			
print("Correct:",correctCounter)

		