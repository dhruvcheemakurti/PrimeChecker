factor = 0
number = int(input())
for i in range (1,number):
    if number%i == 0:
        factor = factor + 1
if counter > 2:
    print("not prime")

else:
    print("prime")

