#    PROJECT    12
# CHECKING OF NUMBER IN FIBONICC SERIES

m= int(input("Enter amount of numbers to be checked: "))  #Amount of numbers user wants to check
n1,n2=0,1
if m>0:
    for i in range(0,m):
        n=int(input("Number: "))                           #No. to be checked
        l=[0,1]
        for i in range(1,n+1):
            nth=n1+n2
            n1=n2
            n2=nth
            l.append(nth)
        if n in l:
            print(n,"is valid")
        else:
            print(n,"is invalid")
else:
    print("ERROR!!! Enter valid amount of numbers to be checked .i.e., >0")