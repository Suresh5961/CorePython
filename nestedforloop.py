#nested for loop

'''for i in range(3):  #-->(0,1,2)
    for j in range(2):  #-->(0,1)

        print(j)
    print(i)
    '''

  #nested*for loop-pattern program

'''for i in range(3):
     for j in range(0,i+1):

       print("*",end="")
     print("")
'''
'''for i in range(3):
    for j in range(0,i+1):
       print(j,end="")
    print('')
'''

n=int(input("enter the value of n"))
for i in range(n):
    for j in range(0,i+1):
        print(n-j,end="")
    print("")
