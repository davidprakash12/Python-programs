n=20
total=0
while (n<=60):
    count=0
    i=2
while (i<=n/2):
    if(n%i==0):
        count=count+1
        break
    i=i+1
if(count==0 and n!=1):
    print("%d"%n,end='    ')
    total=total+n
    n=n+1
    print("\n\nSum=%d" %total)
