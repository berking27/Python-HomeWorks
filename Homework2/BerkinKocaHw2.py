import statistics

#Answers to Grade
def Grade(answerKeyList,answers):
    i = 0
    grades = 0
    while i < len(answerKeyList):
        if(answerKeyList[i] == answers[i]):
            grades = grades + 10
        i = i + 1

    return grades



#Main
answerKeyList = input("Enter answer key: ");
nameList = []
surnameList = []
GradeList = []
j= 0
count = 0
k = 0
studentDictionary = {}

#input name/surname/answer
while count < 2:
    name = input("Enter name: ")
    nameList.append(name)
    surname = input("Enter surname: ")
    surnameList.append(surname)
    answers = input("Enter answers: ")
    grade = Grade(answerKeyList, answers)
    GradeList.append(grade)
    count = count + 1

    
# Made a Tuple of names and surnames
tupleNames = list(zip(nameList,surnameList))


#Add items to Student dictionary
while j < len(GradeList):
    studentDictionary[tupleNames[j]] = GradeList[j]
    j = j + 1

print("Student dictionary:\n",studentDictionary)

#Find avarage of Grades.
avg = statistics.mean(GradeList)
print("The average:\t",round(avg,2))
print("\n")

#Students above Grade part
print("Students above average")
while k < len(studentDictionary):
    if(list(studentDictionary.values())[k] >= avg):
        print("Name: ",list(studentDictionary.keys())[k][0],",",
        list(studentDictionary.keys())[k][1][0],
        ". Score: ",list(studentDictionary.values())[k])
        #To print Name/Surname/Score
    
    k = k+1

print("\n")

#Searching name inside dictionary!
searchName = input("Who are you seraching for? ")
x = 0
found = 0
while x < len(studentDictionary):
    if(searchName == list(studentDictionary.keys())[x][0] or searchName == list(studentDictionary.keys())[x][1]):
        print(list(studentDictionary.keys())[x][0],list(studentDictionary.keys())[x][1],"received ",list(studentDictionary.values())[x])
        found = 1
    x = x + 1

if(found == 0):
    print("Sorry! We can not find her/him.")
