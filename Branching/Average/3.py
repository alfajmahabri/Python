# Write Python program to find smallest of three numbers
n1 = int(input("Enter Number 1: "))
n2 = int(input("Enter Number 2: "))
n3 = int(input("Enter Number 3: "))

# Find the largest number
if n1 < n2 and n1 < n3:
    print("Number 1 is smallest")
elif n2 < n1 and n2 < n3:
    print("Number 2 is smallest")
else:
    print("Number 3 is smallest")