#Write a program to take values for two sets and get intersection of that sets.
set1 = int(input("enter number : "))
set2 = int(input("enter number : "))
user_input1=set1.split()
user_input2=set2.split()
user_set1=set(user_input1)
user_set2=set(user_input2)
intersection=user_set1|user_set2
print(intersection)