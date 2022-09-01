# def sort_number(a,b,c):

#  biggest_number= max(a,b,c)

#  smallest_number = min(a,b,c)

#  middle_number = (a+b+c) - (biggest_number + smallest_number)

#  print(smallest_number,middle_number,biggest_number)

# sort_number(56,87,23)

n1=int(input("Enter the first number:"))
n2=int(input("Enter the first number:"))
n3=int(input("Enter the first number:"))
if n1>n2:
    max=n1
else:
    max=n2 
if n3>max:
    max=n3 
    print(n1,n2,n3,sep="/")
    print("max:",max)
