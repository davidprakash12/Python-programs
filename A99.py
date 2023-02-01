i=99
while i<=999:
    temp=i
    s=0
while temp!=0:
    d=temp%10
    s=s+d*d*d
    temp=(int)(temp/10)
else:
    if(s==i):
        print(s)
    i=i+1
else:
    print("***END***")

