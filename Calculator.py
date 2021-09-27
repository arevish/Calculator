a= int(input("Enter your 1st number "))

print( "Select what task you want to perform\n Enter + for addition \n Enter - for substraction \n Enter * for multiplication \n Enter / for division ")
c= input()
b= int(input("Enter your 2nd number "))
if c=="+" :
    print("Sum of number is ",a +b)
elif c=="-" :
    print("Substraction of number is ",a -b)
elif c=="*" :
    print("multiplication of number is ",a *b)
elif c=="/" :
    print("division of number is ",a /b)