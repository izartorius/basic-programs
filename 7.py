total = 0
a = float(input('enter the 1st number: '))
b = float(input('enter the 2nd number: '))
c = float(input('enter the 3rd number: '))
total += a + b + c

for i in range(4, 11):
    num = float(input(f"enter the {i}th number : "))
    total += num
print("the sum of numbers is:", total)