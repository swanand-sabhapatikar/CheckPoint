#--this prog reads te file and transfer the data to speccific file for further processing
#Following script is divided into 3 parts:
#part 1: GETTING SCHEDULE FORM THE FILE
#	.reading the file where schedule is written
#	.extracting required part
#	.further extracting name,checkpoint and timing
	
#part 2: WRITING INTO FILE 
#	.extracted list of name,checkpoint and timing is then saved at path:
#	. schedule\Your_Schedule.txt

#part 3: Alarm
#	.The list which is save as above is passed to other scrpit resonsible for producing popups on screen exactly 15 and 5 min before the actual timing of checkpoint

#--import start
import os
import time
from ALARM import stopwatch as alarm
import CustomExceptions.CustomExes as  exes
import getname as name 

#--import ends

#Global variables --start 
BaseFolder=os.getcwd()
f=open(BaseFolder+"\\schedule\\Your_schedule.txt","w")
finalList=[]
#Global variables --end

## PART-1: START 
#GETTING SCHEDULE FORM THE FILE

# read the file containing schedule
#if not found raises exception
def readFile():
    global BaseFolder
    name=os.listdir(BaseFolder+"\\Paste_Here")
    print(len(name))
    if len(name)<1:
        raise exes.FileNotFoundError()
    else:
        f=open(BaseFolder+"\\Paste_Here\\"+name[0],"r")
        return f

#Following fuction reds the file form above function containing the schedule and only extracts the required text and pass on to next function 
def extractFromFile():
    #level 1 sorting 
    #take only needed input 
    fRead=readFile()
    read=fRead.read()
    rread=read.split("\n")
    i=0
    while (i<len(rread)):
        if  rread[i]=="Task":
        #print(i)
            break
        else:
            pass
        i+=1
  
    i-=1
    while i>=0:
        rread.pop(i)
        # print(i)
        i-=1
    i=0
    while (i<len(rread)):
        if  rread[i]=="":
            #print(i)
            break
        else:
            pass
        i+=1
  
  #i
    j=len(rread)
    while j>=(i+1):
        rread.pop()  
        j-=1

    return rread          


#Following funciton takes refined output from function "extractFromFile()" as input and further process it
#Following funciton creates a list in which each element is list containing three values :task_name,name_of_person_responsible_for_task,time_of_checkpoint
#which is then passed to two functions : PutIntoFile() and remainders()

def extractSchedule():
    a=extractFromFile()
     
  
    i=j=k=0
    l_main=[]
    l_sub=[]
    schedule_ditc={}
    #
    while j<((len(a))):
        
        while i<3:
            l_sub.append(str(a[j]).strip())
            #logging.info("j:{}".format(j))#print("j:",j)
            #logging.info("a[j] : {}".format(a[j]))
            j+=1
            i+=1
            
        i=0
        l_main.append(l_sub.copy())
        l_sub.clear()    
    #logging.info("l_main : {}".format(l_main))
   # logging.info("function ends\n")
    return l_main

##PART:1 END



##PART:2 START

#-- WRITING INTO FILE 
#
def sortByName():
    n=(name.GetName()).lower()
    #print(type(n))
    global finalList # finalList  is a list 
    extt=extractSchedule()
    ##logging.info("function starts")
    finalList.append(extt[0][1])
    finalList.append(extt[0][2])
    #logging.info("finalList:{} ".format(finalList))
    for i in extt:
        #print(i)
        b=i[1].lower()
        #print(b,n)
        if (b)==n:

            finalList.append(i[0])
            finalList.append(i[2])
        else:
            pass 
    
#Following functions takes the "finalList" containing final list of checkpoint(s) for the particular person and write it into file at path: schedule\Your_Schedule.txt, for user  to view it at anytime.
def PutIntoFile():
    sortByName()
    global finalList
    data=finalList
    for i in range(51):
        print("-",end="",file=f)
    print("+",file=f)
    k=b=0
    for i in data:
        if k==0:
            wd=40
        if k==1:
            wd=10
        print(i.ljust(wd," "),end="",file=f)
        print("|",end="",file=f)
        k+=1
        if b==1:
            print(end="\n",file=f)
            for i in range(51):
                print("-",end="",file=f)
            print("+",end="",file=f)
        b+=1
        if k>1:
            print(end="\n",file=f)
            
            k=0
    for i in range(51):
        print("-",end="",file=f)
    print("+",file=f)        

##PART:2 END

##PART:3 START

#--Alarm 
#Following function takes the "finalList" containing final list of checkpoint(s) for the particular person and pass it to another script "stopwatch.py" in the Alarm package.
def remainders():
    #print(finalList)
    alarm.RefineInput(finalList)

##PART:3 END


#Main function
def main():

    #part 1
    extractFromFile()

    #part 2
    PutIntoFile()

    #part 3
    remainders()


#THE MAIN DRIVING CODE     
try:

    main()

except Exception as  e:
    print("error details:",e)
    print("exiting terminal in 10 sec ") 
    a=10
    for i in range(a,0,-1):
        print("Exiting terminal in :",end="")
        print(i,"\r",end="")
        time.sleep(1)
   # time.sleep(10)
else:
    print("Process complete")
    print("your schedule is written at >schedule\\Your_schedule.txt")
    print("also you will get remainders 15 and 5 min before the checkpoint")    
    a=10
    for i in range(a,0,-1):
        print("Exiting terminal in :",end="")
        print(i,"\r",end="")
        time.sleep(1)
   # time.sleep(10)

finally:
    f.close() 

