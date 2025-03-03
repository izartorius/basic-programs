odd = []

for i in range(1, 11):
    num = float(input(f"enter num{i}: "))
    if num % 2 != 0:
        odd.append(num)
print("the odd numbers are:", odd)