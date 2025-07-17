t=int(input("enter test cases"))
while t>0:
    number=int(input("enter a number"))
    for i in range(10):
        table=number*i
        print(f"{number}*{i}={table}")
t=-1