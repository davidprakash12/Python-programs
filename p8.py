n=int(input('Enter Number= '))
p=1
f=0
while p<=n:
    if n%p==0:
        f=f+1
        p=p+1
    else:
        p=p+1
    if f==2:
        print("This is Prime Number= ',n)
     else:
        print('Sorry! Not a Prime Number')
              
