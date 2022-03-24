import pickle

num = int(input('how many students: '))

names = []
grades = []

for j in range(0, num, 1):
    name = input("please enter student name: ")
    names.append(name)

    prompt = "please enter " + name + "'s grade:   "

    grade = float(input(prompt))
    grades.append(grade)


with open('studentData.pkl', 'wb') as dataF:
    pickle.dump(num, dataF)
    pickle.dump(names, dataF)
    pickle.dump(grades, dataF)

with open('studentData.pkl', 'rb') as readF:
    a = pickle.load(readF)
    b = pickle.load(readF)
    c = pickle.load(readF)

print(a)
print(b)
print(c)
print("a new print statement is added to the program to experiment with git branches")
