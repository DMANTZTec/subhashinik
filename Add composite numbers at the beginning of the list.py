input_list=list(map(int,input("enter numbers : ").strip().split()))
new_composite_list=[]
new_prime_list=[]
combined_list=[]
for x in input_list:
    if x%2!=0:
        new_prime_list.append(x)
    else:
        new_composite_list.append(x)
combined_list=new_composite_list + new_prime_list
print(combined_list)