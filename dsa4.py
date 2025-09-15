# Amstrong number
# 153 (total 3 numbers)=1 power 3 +5 power 3 +3 power 3 = 153 then its a amstrong number
from math import *
a=int(input("Enter a number : "))
num=a
length=len(str(a))
def amstrong(a):
    sum=0
    while a>0:
        last_digit=a%10
        last_digit=last_digit**length
        sum+=last_digit
        a=a//10
    return sum
if amstrong(a)==num:
        print("yes it is an amstrong number")
else:
        print("no, not an amstrong number")
