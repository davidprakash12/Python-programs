#Armstrong Number 

n=int(input('Enter Number= '))
temp=n
s=0
while temp!=0:
    d=temp%10
    m=d*d*d
    s=s+m
    temp=int(temp/10)
else:
    print("Original Number=",n)
    print("New Number=",s)
if s==n:
    print("This is Armstrong Number")
else:
    print("Sorry! Not a Armstrong Number")
    

          
