x = int(input("Enter a Year:"))

if (x % 4 == 0 and x % 100 != 0) or (x % 400 == 0):
    print("Leap Year")
else:
    print("Not a Leap Year")
