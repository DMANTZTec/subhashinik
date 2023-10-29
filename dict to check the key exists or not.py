#Write a program to check whether a given key is exist or not in dictionary.
dict1={1:"subbu",2:"subhashini",3:"family",4:"frineds",5:"happy life"}
key=int(input("enter number : "))
if key in dict1:
    value=dict1[key]
    print(value)
else:
    print("key doen't exists.Thankyou")
