#Francis Niño A. Eugenio
#BSCPE 1-5 | Object Oriented Programing
#Even & Odd Multiplier

# open and read the source file
with open("integers.txt", "r") as source_file:
    numbers = [int(num) for num in source_file.read().split()]
#create a empty list for both odd and even
odd = []
even = []
# separate the even and odd in the source file
for num in numbers:
    if num % 2 == 0:
        even.append(num)
    else:
        odd.append(num)
    
    print(odd)
# create the new txt file for evem but doubled

# create the new txt file for odd but tripled