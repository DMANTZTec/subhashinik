#Write a program to take dynamic arguments and print sum of those numbers.
def sum(n):
    Sum=0
    for i in range(0,len(n)):
        Sum+=i
    print(Sum)
n=list(map(int,input("enter numbers to be added : ").split()))
sum(n)