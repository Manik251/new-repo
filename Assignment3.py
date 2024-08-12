Student_name= (input("Enter student name: "))
Class= int(input("Enter student class: "))
Roll_No= int(input("Enter student roll.no: "))
# if Math>100 and Science>100 and Nepali>100 and English>100 and Computer>100
Math= float(input("Enter marks of math: "))
Science= float(input("Enter marks of science: "))
Nepali= float(input("Enter marks of Nepali: "))
English= float(input("Enter marks of english: "))
Computer= float(input("Enter marks of computer: "))
sum = Math+Science+Nepali+English+Computer
print("The total marks obtained by student is: ",sum)
percentage= (sum/500)*100
print("The percentage of student is: ",percentage)
if percentage>90 and percentage<=100:
    print("Student got Distinction")
elif percentage>80 and percentage<=90:
    print("Student got First Division")
elif percentage>=60 and percentage<80:
    print("Student got Second Division")
elif percentage>=40 and percentage<60:
    print("Student got Third Division")
else:
    print("Student got Fail")


