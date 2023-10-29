#Write a program to print unique values list from a list. Test Case: Input: [1,4,7,2,1,4,6,7,2] Output: [1,2,4,6,7]
input=list(map(int,input("enter elements : ").strip().split()))
duplicate_elements=[]
for element in input:
    if element not in duplicate_elements:
        duplicate_elements.append(element)
print(duplicate_elements)
   
