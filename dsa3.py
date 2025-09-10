# check palindrome
# when reverse is also same as original
# n=1234
# 1234%10=4   4*10=40     40+3=43 =result
# result=43   43*10=430    430+2=432
# result=432  432*10=4320  4320+1=4321
def palindrome(a):
    num=a
    result=0
    while a>0:
        last_digit=a%10
        result=(result*10)+last_digit
        a=a//10
    
    if a==num:
        print("palindrome")
    else:
        print("not a palindrome")
palindrome(0000)