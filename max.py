n=int(input('Enter Number= '))
max=n%10
temp=n
while temp!=0:
    d=temp%10
if d>max:
    temp=(int)(temp/10)
else:
    print('Max= ',max)
    
