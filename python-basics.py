import pandas as pd 

df = pd.read_csv("data.csv")

age = 22
height = 5.9
name = "Ubaid"

print(type(age))
print(type(height))
print(type(name))


num1 = "10"
num2 = 7

result = int(num1)+num2

print(result)


# Create List

numbers = [10,20,30,40,50,60,4,8,7,2,16]

for num in numbers:
    if num % 2 == 0:
        print(num)


total = 0
for num in numbers:
    total += num
    
print("Sum:",total)


student = [
    {"name":"Ubaid","age":5.7,"gpa":3.4},
    {"name":"Ali","age":5.3,"gpa":3.9},
    {"name":"Umer","age":5.7,"gpa":3.0},
    {"name":"Usama","age":5.7,"gpa":2.4},
]

for std in student:
    if std["gpa"] >= 3.0:
        print(std["name"])



# for loop and while loop 

i = 0

for i in range(0,11):
    print(i)
    
 
count = 1

while count <=5:
    print(count)
    count +=1  