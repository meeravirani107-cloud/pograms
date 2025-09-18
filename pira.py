n=int(input("Enter No :="))

for i in range(1,n+1):     
    for j in range(1,i+1):
      print("*",end="")
    print()

'''
*
**
***
****
*****
'''    
    
for o in range(1,n+1):
    for p in range(o-1,n):
      print("*",end="")
    print() 

'''
*****
****
***
**
*
'''    
   
for z in range(1,n+1):
    for x in range(n-z):
      print(" ",end="")
    for c in range(1,z+1):
             print("*",end="")
    print()

'''
    *
   **
  ***
 ****
*****
'''    
   
for x in range(1,n+1):
  for d in range(n-x):
    print(" ",end="")
  for a in range(2*x-1):
    print("*",end="")
  print() 
    
'''
    *
   ***
  *****
 *******
*********
'''    