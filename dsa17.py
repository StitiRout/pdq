# Fibonnaci number
# 0,1,1,2,3,5,8 ....
# through recursion
class solution:
    def fxn(self,num):
        self.num=num
        if num==0:
            return num
        elif num==1:
            return num
        else:
            return self.fxn(num-1)+self.fxn(num-2)
result=solution()
print(result.fxn(5))