a=20
sum=0
while (a<=60):
    i=1
    count=0
    while (i<=a):
        if(a%i==0):
            count=count+1
        i=i+1
    if (count==2):
        sum=sum+i
        print(sum)
 
   
   
