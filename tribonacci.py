n=int(input('Enter Number of Terms= '))
a=0
b=1
c=1
d=0
print("Tribonacci Series")
print(a)
print(b)
print(c)
i=4
while i<=n:
    d=a+b+c
    print(d)
    a=b
    b=c
    c=d
    i=i+1
else:
    print('*****')
    
