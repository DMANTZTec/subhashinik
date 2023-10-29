#Using loop to write a program that displays the following pattern   * ** *** **** *****
num_rows = 5
for i in range(1, num_rows + 1):
    for j in range(i):
        print('*',end=' ')
    print()

