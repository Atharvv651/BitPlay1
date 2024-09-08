number = int(input("Enter A Number: "))
print()

def number_of_zeros(number):
    number_of_zeros = 0
    while number > 0:
         number_of_zeros += ~number & 1
         number >>= 1
    return number_of_zeros

def number_of_ones(number):
     number_of_ones = 0
     while number > 0:
         number_of_ones += number & 1
         number >>= 1
     return number_of_ones

print(f"Number of Zeros: {number_of_zeros(number)}")
print(f"Number of Ones: {number_of_ones(number)}")