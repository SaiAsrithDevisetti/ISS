number = int(input("Enter the number of students: "))
name = []
roll = []
math = []
cse = []
Science = []
total = []
add=0
print("Enter the following data")
for i in range(number):        #taking input
    name.append(input("Enter the name: "))
    roll.append(input("Enter the roll number: "))
    math.append(int(input("Enter the Maths marks: ")))
    cse.append(int(input("Enter the CSE marks: ")))
    Science.append(int(input("Enter the Science marks: ")))
    total.append(math[i] + cse[i] + Science[i])
    add = add + total[i]

total.sort(reverse=True)
if number%2 == 0:            #calculation of median
    a = int(number/2)
    median= (total[a] + total[a + 1]) / 2
if number%2 != 0:
    a = int((number + 1) / 2)
    median= total[a]
print("Name : Roll Number")
for i in range(number):       #printing the list of names and roll numbers
    print(name[i], roll[i])

search = input("Select any name or roll number: ") #taking the input of any identity
for i in range(number):
    if search == name[i]:      #printing the desired data if name is the identity 
        temp = math[i] + cse[i] + Science[i]
        rank = total.index(temp)
        print("The name of the student is: ",name[i])
        print("The Roll number of the student is: ",roll[i])
        print("The class average of all courses is: ", add/number)
        print("The class median of all courses is: ", median)
        print("The Rank of the student: ",rank + 1)
    if search == roll[i]:     #printing the desired data if roll number is the identity 
        temp = math[i] + cse[i] + Science[i]
        rank = total.index(temp)
        print("The name of the student is: ",name[i])
        print("The Roll number of the student is: ",roll[i])
        print("The class average of all courses is: ", add/number)
        print("The class median of all courses is: ", median)
        print("The Rank of the student: ",rank + 1)
          