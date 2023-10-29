#Write a program to take number as input from user and print it's factorial
def fac(n):
    if n==1:
        return 1
    else:
        return n* fac(n-1)
n=int(input("enter number : "))
print(fac(n))