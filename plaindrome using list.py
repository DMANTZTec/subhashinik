s = []
n = ['subhashini', 'kolluri', 'madam']

for word in n:
    if word == word[::-1]:
        s.append(1)
    else:
        s.append(0)

print(s)