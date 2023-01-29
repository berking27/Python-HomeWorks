from glob import glob
import math
from re import S

def Max(myList):
    if len(myList) == 1:
        return myList[0]
    else:
        maxVal = Max(myList[1::])
        return maxVal if maxVal > myList[0] else myList[0]
        #Findind the max Value of List
i = 0
def EvenChanger(myList,maxVal,y):
    global i
    if len(myList) == i:
        return myList
    else:
        if maxVal == myList[i]:
            myList[i] = y
            i = i + 1
            EvenChanger(myList,maxVal,y)
        else:
            i = i + 1
            EvenChanger(myList,maxVal,y)
# count = 0
def OddChanger(myList,y,count=0):
    # global count
    if(count == 1):
        return myList
    else:
        if(count == 0):
            count= len(myList)
            count += 1
        myList.insert(0,y)
        count = count - 1
        return OddChanger(myList,y,count)

def form(myList,y):
    if len(myList) % 2 == 0:
        maxVal = Max(myList)
        EvenChanger(myList,maxVal,y)
        #Need to find max first after call the evenLen function
    else:
        OddChanger(myList,y)

def ListMakerInt(x):
    if(x == 0):
        return myList
    digit = x % 10
    myList.append(digit)
    ListMakerInt( math.floor(x / 10))

x = eval(input("Please enter a number:"))
myList = []
ListMakerInt(x)
myList.reverse()
print(myList)
len_of_list = len(myList)
y = eval(input("Enter a number between 0-9:"))
form(myList,y)
print(myList)





