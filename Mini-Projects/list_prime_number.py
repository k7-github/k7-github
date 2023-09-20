print("A prime number is a number that can be divided ONLY by itself and 1.")
print("For example, 7 is a prime number because it can be divided only by 7 (itself) an 1.")
print("Whereas 12 is NOT a prime number. In addition to 12(itself) and 1, 12 can also be divided by 2, 3, 4 and 6.")

min_num = 0
max_num = 0
num_list = []
prime_num = []

while min_num <= 1:
    min_num = int(input("\nType a number larger than one: "))
    if min_num <= 1:
        print("This number is NOT larger than one. Try again.")
        continue
    while max_num <= min_num:
        max_num = int(input("Type another number larger than the previous number: "))
        if max_num <= min_num:
            print("This number is NOT larger than the previous number. Try again.")
            continue
        num_list = list(i for i in range(min_num, max_num + 1))

for num in num_list:
    for div in range(2, num):
        if num % div == 0:
            break    
    else:
        prime_num.append(num)

print(f"\nThere are {len(prime_num)} prime numbers between {min_num} and {max_num}.")
print(prime_num)