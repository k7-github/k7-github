# Is this number a prime number?
print("A prime number is a number that can be divided ONLY by itself and 1.")
print("For example, 7 is a prime number because it can be divided only by 7 (itself) an 1.")
print("Whereas 12 is NOT a prime number. In addition to 12(itself) and 1, 12 can also be divided by 2, 3, 4 and 6.")

prime = int(input("Type a number: "))
is_prime = ""

for i in range(2, prime - 1):
    if prime % i != 0:
        continue    
    else:
        print(f"{prime} is NOT a prime number.")
        break

else:
    print(f"{prime} is a prime number.")