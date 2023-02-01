# define a function for finding 
# reverse of the number
def reverseNum(num) :
    
    rev_num = 0

    # iterate the loop till num is not equal to zero
    while(num) :
        rem = num % 10
        rev_num = rev_num* 10 + rem
        num //= 10

    return rev_num


# Main() method
if __name__ == "__main__" :

    # take string input from user
    num = int(input('Enter a number: '))
    
    print('Reverse number is: ', reverseNum(num))
