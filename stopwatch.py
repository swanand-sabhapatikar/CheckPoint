#This program will generate alarm / popup

import datetime
import os
import time
import threading
from subprocess import call
import sys

#below try-catch is to check if easygui module is installed or not, if not it will automatically install the same and the pr
try:
	import easygui
except Exception as e:
	print("easygui module not installed. Installing it now")
	call("python -m pip install easygui")
	a=10
	print("successfully installed 'easygui'. Terminating the program. Please re-run the program ")
	for i in range(a,0,-1):
		print("The screen will be cleared in :",end="")
		print(i,"\r",end="")
		time.sleep(1)
	
	sys.exit(0)

#Global variables start 

TimestampDict={}

tie=0

#Global variables end 


#This function acts as realtime clock for this program and will convert into format as: "hh:mm"
def stopwatch():
	while True:
		global tie
		tie=(datetime.datetime.now().strftime("%H:%M"))
		time.sleep(1)
		return tie

def makeDisplay(checkpoint,task):
	#tasks=task.join(";")	
	message="tasks to do:{}".format(task)
	Title="Remailder for checkpoint at{}".format(checkpoint)
	easygui.msgbox(msg=message,title=Title,ok_button="OK")


##This function takes two values 
# 1. time of checkpoint (t)
# 2. min before time of checkpoint at which alarm needs to be displayed (timeBeforeT)
#this funciton returns exact time, which is timeBeforeT min before the checkpoint time t
#eg: if t:14:45, and timeBeforeT=15, program will return: 14:30
#we will substract the current min value of time form the timeBeforeT value to get exact time.
def LookBeforeTime(t,timeBeforeT):
	
	#Converting STR value to INT for substraction
	hrOfT=int(t[0:2])
	minOfT=int(t[3:])s
	timeBeforeT=int(timeBeforeT)
	

	#case 1:- for hour value 
	
	#if hour value is zero
	
	if hrOfT==00:
		hrOfT=24
		
	#case 2:- for min value	
	
	#if min value is zero
	if minOfT==00:
		#print("int 1")
		
		hrOfT-=1
		minOfT=60-timeBeforeT
		
	#if min value is not zero: 
	#case 2.1:
	#if the "min value of current time" is less than the "timeBeforeT"
	#eg: if minOfT=10 timeBeforeT=15;
	#as time cant be negative, we will add the result(minOfT=10 timeBeforeT) onto 60 and we will get our required value.
	elif minOfT-timeBeforeT<0:
		
		minOfT=60+(minOfT-timeBeforeT)
		hrOfT-=1	
	
	#case 2.2:
	#if the "min value of current time" is greater than the "timeBeforeT"
	#eg: if minOfT=20 timeBeforeT=15;
	#directly substract and return the same.
	elif minOfT-timeBeforeT>=0:
		
		if hrOfT==24:
			hrOfT=00
		minOfT-=timeBeforeT


	#converting back to STR 
	
	hrOfT=str(hrOfT)
	minOfT=str(minOfT)		

	#Time to return the time
	#If hour or min value is single digit, as time value is alwasys double
	if len(hrOfT)==1:
		"0"+hrOfT
		
	if len(minOfT)==1:
		"0"+minOfT
			
	return hrOfT+":"+minOfT

			

#This funcion will serially take each value from SortedList containing checkpoints in ascending order or 't' and pass it to other funcion MakeAlarm responsible to create alarm and also display message on screen.
def SelectOneByOne(t):

	for i in t:
		#print(i)
		MaKeAlarm(i)

#This function will take one by one input from above function and do following things:
#Display popup on screen 15 and 5 min before the checkpoint.

def MaKeAlarm(t):
	global TimestampDict
	
	TaskToDo=[]
	for i in (TimestampDict):
		
		if TimestampDict[i]==t:
			TaskToDo.append(i)

	
	
		#print("i: ",i)
	
	# for 15 min before checkpoint
	rem1=LookBeforeTime(t,15)
	
	#funciton responsible for popup
	makeDisplay(t,TaskToDo)
		#while  True:
			#clock=stopwatch()
			#if rem1==clock:
				
				#break
		#	pass
	# for 5 min before checkpoint
	rem2=LookBeforeTime(t,5)
	
	#funciton responsible for popup
	makeDisplay(t,TaskToDo)
	
	#while  True:
		#clock=stopwatch()
		#if rem2==clock:
			#	makeDisplay(rem2,TaskToDo="Test file")
			#break
	#	pass	
		


#This function sorts the checkpoints  in assending order  and return the sorted list
def sortTheList(lt):

	sortedTimestamp=[]
	for i in lt:
		sortedTimestamp.append(int(i[:2]+i[3:]))
	#list to sort
	TempListc=sorted(sortedTimestamp)

	sortedTimestamp.clear()
	#convert back to string
	for t in TempListc:
		t=str(t)
		if len(t)==3:
			sortedTimestamp.append("0"+t[0]+":"+t[1:])
		else:
			sortedTimestamp.append(t[:2]+":"+t[2:])	
	#print("original value after sorting :")
	return sortedTimestamp


#This function takes input form the Exctact.py script and remove unwanted date and process further.
##@part 1 
# "ll" is  list containing values, where each value containg three value : task_name,name_of_person_responsible_for_task,time_of_checkpoint
#for each value of the list "ll", this program picks time_of_checkpoint and add to another list "TimestampToSort" to further sort the list into assending order, hence ordering the time_of_checkpoint in ascending order
##@part 2
#same ll(the list input) is used to create dictionary, with key value as time of checkpoint and its values will be all the checkpoint for that time.

def RefineInput(ll):
	
	#To Pop unnecessary elements from the list
	ll.pop(0)
	ll.pop(0)
	
	##@part1 --start 

	#print("list form Exctact scrypt:", ll )
	TimestampToSort=[]
	global TimestampDict
	limit=len(ll)
	for i in range(0,limit,):
		if i%2!=0:
			TimestampToSort.append(ll[i])
	
	SortedList=sortTheList(TimestampToSort)

	##@part1 --end 

	##@part2 --start 
	j=i=0		
	while i<(limit-1):
		
		j=i+1
		TimestampDict[ll[i]]=ll[j]
		
		i+=2
	##@part2 --end

	#see brief above the funciton "SelectOneByOne" for below statement
	SelectOneByOne(SortedList)

	#print(k)

# to run the script stand alone
if __name__=="__main__":
	a="07:02"# 3(03. .15 .2 .0)    15(15)
	b=3# 
	c=LookBeforeTime(a,b)
	print ("currtime={},t={},before t ={}  ".format(a,b,c))	

