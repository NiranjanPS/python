###############################################################################################
##Python 3 code for problem statement:
##you are given 3 numbers a,b and c you can subtract 1 from any 2 numbers in one operation.
##you are required to determine the max number of operations that can be performed such 
##that no number is negative
###############################################################################################

ls = [] 
n = 3 # number of elemetns as input 
print("Enter 3 numbers:")
for i in range(0, n): 
    ele = int(input()) 
    ls.append(ele) # adding the element 
print(ls)
def solve(ls):
    ls.sort()
    count = 0
    while(1):
        if(ls[0]|ls[1])==0:
            break
        else:
            count += 1
        ls[1] -= 1
        ls[2] -= 1
        ls.sort()
    return count
print(solve(ls))
