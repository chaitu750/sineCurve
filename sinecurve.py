#Sin curve
import math
s=[]
n=int(input("Enter size of sin curve: "))
for i in range(0,361,360//n): # initially 5 was given inplace of 360//n 
    j = round((math.sin(math.radians(i))*n))
    s.append(j)
    for k in range(-n,n):
        if i<=180:
            if k==0:
                print("!",end='')
            elif k == j:
                print("+",end='')
            elif k >0 and k<j:
                print('+',end='')
            else:
                print(" ",end='')
                
        elif i>180:
            if k==j :
                print("-",end='')
            elif k==0:
                print('!',end='')
            elif k<0 and k>j:
                print('-',end='')
            else:
                print(" ",end='')
    print("")
print(s)
