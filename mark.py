name=input("enter student name:")
n=int(input("enter number of subjects:"))
total=0
for i in range(1,n+1):
    mark=float(input(f"enter mark for subject{i}:"))

    total+=mark
    percentage=total/n
    if percentage>=90: 
        grade="A+"
        performance="outstanding"
    elif  percentage>=80:
        grade="A"
        performance="exceelent"
    elif percentage>=70:
        grade="B"
        performance="very good"
    elif percentage>=60:
        grade="C"
        performance="good"
    elif percentage>=50:
        grade="D"
        performance="average"
    elif percentage>=40:
        grade="E"
    else:
        grade="F"
        performance="Fail"
    print("academic result")
    print("student name",name)
    print("your grade is",grade)
    print(p)






        