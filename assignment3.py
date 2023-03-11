testa =int( input("Enter test1 marks"))
testb =int( input("Enter test2 marks"))
course = int(input("course work marks")) 

def tests(testa, testb):
    if testa >=testb:
        return testa
    else:
        return testb

def averageCoursework(course):
    myBest = tests(testa,testb)
    averageMarks =(myBest + course)/2
    averageCoursemark = averageMarks*0.4
    return averageCoursemark
print("average course unit mark",averageCoursework(course))

def examMark():
    finalExam =( averageCoursework(course)+ course)*0.6
    return finalExam
print("final course unit marks",examMark())

finalexam =  open('C:/Users/Richard/Desktop/final_exam.txt', 'w')  
finalexam.write(str(testa))
finalexam.write(str(testb))
finalexam.write(str(examMark()))





