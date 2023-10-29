def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)
ls=[1,2,3,4,5,6,7,8,9,10]
count=[]
ls2=[]
for num in ls:
    count=factorial(num)
    ls2.append(count)
print(ls2)