import pickle

with open('studentData.pkl', 'rb') as dataF:
    numStudents = pickle.load(dataF)
    names = pickle.load(dataF)
    grades = pickle.load(dataF)

while True:
    name = input("which student do you want to check: ")
    for i in range(0, numStudents, 1):
        if (names[i] == name):
            print(str(name)+"'s grade is ", grades[i])
