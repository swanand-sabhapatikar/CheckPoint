 #This scipt is used to retrive name of user for whome schedule of checkpoint is to be derived

import os 
import CustomExceptions.CustomExes as  exes


#way 1: using os.getlogin
#this will give user name of currently logged user to the PC

def getAutoInput():

	name=os.getlogin()
	return name

#way 2: manual input
#if name retrived by above method does not match the name in the email,
#the person have to save his name as in the email in to "Enter_Your_name_here.ss" file.
#name is directly extracted and is used for further process
def GetManualInput():
	
	BaseFolder=os.getcwd()
	f=open(BaseFolder+"\\name\\Enter_Your_name_here.ss",'r')
	r=f.readline()
	
	if r=="":
		raise exes.NameNotFoundException()
		return 0
	else:
		return r 	

#main funcion for this script
def GetName():

	Name=getAutoInput()
	#print (type(Name))
	print ("is "+Name +" your name in in email? (y/n)")
	CheckName=str(input(">>")).upper()
	if CheckName=="Y":
		return Name
	elif CheckName=="N":	
		Name=GetManualInput()
		return Name
	else:
		raise exes.InvalidInputException()	
#print (a)
