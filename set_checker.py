number = int(input("Enter A Number: "))
bit_number = int(input("Enter Bit Number: "))

if number & (1 << bit_number):
    print("Bit is set")
else:
    print("Bit is not set")