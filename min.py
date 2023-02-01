n=int(input('Enter Number= '))
min=n%10

temp=n
while temp!=0:
    d=temp%10
if d<min:
    min=d
    temp=(int)(temp/10)
else:
    print('Min= ',min)
    
    
