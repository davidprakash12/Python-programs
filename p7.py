a=int(input('Enter Number= '))
count=0
temp=a
while temp!=0:
    count=count+1
    temp=(int)(temp/10)
else:
    print("Total Digits= ",count)

