a=int(input("Enter First Number= " ))
b=int(input("Enter Second Number= "))
c=int(input("Enter Third Number= "))
if(a>b):
    print('Max= ',a)
if(a>c):
    print('Max= ',a)
else:
    if(b>c):
        print('Max= ',b)
    else:
        print("Max= ",c)
              
