n=int(input('Enter Any Number: '))
d=0
rev=0
temp=n
while temp!=0:
    d=temp%10
    rev=(rev*10)+d
    temp=(int)(temp/10)
else:
    print('\nOriginal Number =',n)
    print('\n Reverse of entered number is =',rev)
if n==rev:
    print('This is Palindrome Number')
else:
    print('Sorry! This is not a Palindrome Number')

    
