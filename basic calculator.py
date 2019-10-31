a=int(input("Enter the first number:"))
b=int(input("Enter the second number:"))
sum=a+b
sub=a-b
pro=a*b
quo=a/b
print("\n1.Add\n2.Subtract\n3.Multiply\n4.Divide\n")
opt=int(input("Select an option:"))
if opt==1:
    print("The sum is",sum)
elif opt==2:
    print("The difference is",sub)
elif opt==3:
    print("The product is",pro)
elif opt==4:
    print("The quotient is",quo)
else:
    print("Invalid choice!!")
