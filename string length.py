#Write a program to count the number of strings where the string length is >2. Test Case: Input: ['abc', 'aba', 'aa', 'bab', 'bb']
Input = ['abc', 'aba', 'aa', 'bab', 'bb']
count=0
for i in Input:
    if len(i)>2:
        count=count+1
print(count)