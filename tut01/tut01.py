print("My name is Prabhas. roll number 1901EE17")

def meraki_helper (n):  # declaring function to check whether a number is meraki function
    if(0<= n <=9):   
        print("YES-{} is a Meraki number".format(n))
        return True
    else:          
        k=n
        while(k>10):
            a=k%10; 
            k=k//10
            b=k%10  # a and b stores the adjacent digits
            if(abs( a -b)!=1) : 
                print("NO-{} is NOT a Meraki number".format(n))       
                return False
        print("YES-{} is a Meraki number".format(n))
        return True

input = [12, 14, 56, 78, 98, 54, 678, 134, 789, 0, 7, 5, 123,45,76345, 987654321]
m = len(input)  #length of input
j=0  
for i in range(0,m) :
    res=meraki_helper(input[i])
    if(res==True):
        j=j+1   #j stores the result of number of meraki numbers
print("the input list contains {} meraki and {} non meraki numbers.".format(j,m-j))