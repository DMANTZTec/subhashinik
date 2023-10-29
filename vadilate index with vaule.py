''' Write a program that takes two inputs from user first one is index and second is value. 
And validate the value exist in the given index or not in the list. If value matchs print 
'Value matching with index' else 'Value not matching with index' Test case: List: 
[10,20,30,40,50] Please enter index: 2 Please Enter Value: 100 Output: [10,20,100,30,40,50] 4'''
input=[10,20,30,40,50]
index=list(map(int,input("enter index value : ").split()))
value=list(map(int,input("enter value : ").split()))
if index in input:
    if index(value) in input:
        print('Value matching with index')
else:
    print('Value not matching with index')
