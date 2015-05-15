#!/usr/bin/python

from copy import copy
import random
import sys

def dieresh(startingMessageWith0A,devisorA): #this function is dividing the message+0*length(devisor) with the devisor
       	upolipoA=[] #this array will contain the remaining bits of the division
	for k in range(0,len(devisorA)):
		upolipoA.append(startingMessageWith0A[k]) #it gets the length of the devisor and the first bits of the message
	for i in range(0,len(startingMessageWith0A)-len(devisorA)): #Note to self: need to add more commends later
		if upolipoA[0]==1:
			for j in range(1,len(devisorA)):
				if upolipoA[j]==devisorA[j]:
					upolipoA[j-1]=0
				else:
					upolipoA[j-1]=1
		else:
			for j in range(1,len(devisorA)):
				if upolipoA[j]==0:
					upolipoA[j-1]=0
				else:
					upolipoA[j-1]=1
		upolipoA[len(devisorA)-1] = startingMessageWith0A[i+len(devisorA)]
	return upolipoA

def printingBits(bitsToPrintA):
	for i in range(0,len(bitsToPrintA)):
		print bitsToPrintA[i],
	print
	return

def checkRemain(remain):
	for i in range(0,len(remain)):
		if remain[i]!= 0:
			return 0
	        return 1


print (sys.version)
print 'how many random messages you want to be generated?'
helper0I=0
while helper0I==0:
	print 'Give number: ',
	s= (raw_input())
	try:
		s= int(s)
		if s>0:
			helper0I=1
			nymberOfMessagesI= s
		else:
			print 'need positive number'
	except ValueError:
		print 'Need number'
print 'How big you want the devisor to be? '
helper1I=0
while helper1I==0:
	s=(raw_input("Give length: "))
	try:
		s= int(s)
		helper1I=1
	except ValueError:
		print 'Need number'
devisorA=[0]
for i in range(0,s-1):
	devisorA.append(0)
helper1I=0
for i in range(0,len(devisorA)):
	while helper1I==0:
		print 'Give devisors ',i+1,'st number: ',
		s= (raw_input())
		try:
			s= int(s)
			if s==0 or s==1:
				helper1I=1
				devisorA[i]=s
			else:
				print 'need binary number'
		except ValueError:
			print 'Need number'
	helper1I=0
print 'Devisor is: ',
printingBits(devisorA)
print 'How much % you want the error rate on channel to be?'
helper1I=0
while helper1I==0:
	print 'Give number %: ',
	s= (raw_input())
	try:
		s= int(s)
		if s>=0 and s<=100:
			helper1I=1
			errorRate=s
		else:
			print 'need number %'
	except ValueError:
		print 'Need number'
print 'You want the number of the bits of the messages to be random? y/n ',
helper1I=0
while helper1I==0:
	s= (raw_input())
	if s=='y' or s=='n':
		helper1I=1
	else:
		print 'need y/n'

if s == 'y':
	numberOfBitsOfMessagesI= random.randrange(5,100)
else:
	helper1I=0
	print 'Give number of the bits of messages'
	while helper1I==0:
		print 'Give number: ',
		s= (raw_input())
		try:
			s= int(s)
			if s>0:
				helper1I=1
				numberOfBitsOfMessagesI= s
			else:
				print 'need positive number'
		except ValueError:
			print 'Need number'
helper0I= 0
numberOfMessagesThatSuccessfullySentedI=0
for helper0I in range(0,nymberOfMessagesI):
	print '~~~~~~~~~~~'
	helper2I= random.randrange(0,2)
	startingMessageA= [helper2I]
	for x in range(0,numberOfBitsOfMessagesI):
		helper2I= random.randrange(0,2)
		startingMessageA.append(helper2I)
	print 'The ',helper0I+1,'st message is: ',
	printingBits(startingMessageA)
	helper1I= 0
	startingMessageWith0A=copy(startingMessageA)
	for i in range(0, len(devisorA)):
		startingMessageWith0A.append(0)
	#
	#startingMessageA=[1,0,1,0,1,0,1,0]
	#startingMessageWith0A=[1,0,1,0,1,0,1,0,0,0,0,0]
	#devisorA=[1,0,1,1]
	#
	remainA= []
	remainA= dieresh(startingMessageWith0A,devisorA)
	newMessageWithoutErrorsA=copy(startingMessageA)
	for i in range(0,len(remainA)-1):
		newMessageWithoutErrorsA.append(remainA[i])
	print 'New message is: ',
	printingBits(newMessageWithoutErrorsA)
	newMessageWithErrorsA=copy(newMessageWithoutErrorsA)
	for i in range(0,len(newMessageWithErrorsA)):
		helper1I= random.randrange(0,100)
		if helper1I<=errorRate:
			if newMessageWithErrorsA[i]==0:
				newMessageWithErrorsA[i]= 1
			else:
				newMessageWithErrorsA[i]= 0
	print 'Message with errors is: ',
	printingBits(newMessageWithErrorsA)
	for i in range(0, len(devisorA)):
		newMessageWithErrorsA.append(0)
	remainA= dieresh(newMessageWithErrorsA,devisorA)
	checkerI= checkRemain(remainA)
	if checkerI==1:
		print 'The message has been sent successfully'
		numberOfMessagesThatSuccessfullySentedI=numberOfMessagesThatSuccessfullySentedI+1
	else:
		print 'The message has been corrupted'
print 'The number of messages that successfully sented to the user is',numberOfMessagesThatSuccessfullySentedI, 'from',nymberOfMessagesI








