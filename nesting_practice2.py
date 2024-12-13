#Find greatest of all 3 numbers
"""
a=int(input("enter 1st number :"))
b=int(input("enter 2nd number :"))
c=int(input("enter 3rd number :"))


if(a>b and a>c ):
    print("a is the largest number",a)
elif(b>c):
    print("b is the largest number",b)
else:
    print("c is the largest",c)
"""
#largest among 4
a=int(input("enter 1st number :"))
b=int(input("enter 2nd number :"))
c=int(input("enter 3rd number :"))
d=int(input("enter 4th number :"))

if(a>b and a>c ):
    val1="a"
    if(a>d):
        print("a is the lartest number",a)
elif(b>c and b>d):
    print("b is thelargest number",b)
elif(c>d):
    print("c is the largest number",c)
else:
    print("d is the largest number",d)