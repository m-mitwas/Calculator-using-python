a=int(input("Enter 1 for addition \n Enetr 2 subtraction \n Enter 3 for multiplication \n Enter 4 for division \n Choice= "))
b=int(input("Enter 1st number:  "))
c=int(input("Enter 2nd number:  "))
if a==1:
    sum=int(b)+int(c)
    print("Sum of 1st and 2nd number is : ",sum)
elif a==2:
    subs=int(b)-int(c)
    print("Subtraction of 1st and 2nd number is : ",subs)
elif a==3:
    mull=int(b)*int(c)
    print("Multiplication of 1st and 2nd number is : ",mull)
elif a==4:
    divi=int(b)/int(c)
    print("Division of 1st and 2nd number is : ",divi)
else :
    print("You have entered wrong choice !!!")


    




