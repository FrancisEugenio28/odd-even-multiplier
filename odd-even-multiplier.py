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
# create the new txt file for evem but doubled
with open("double.txt", "w") as even_file:
    for num in even:
        double = num ** 2
        even_file.write(str(double) + "\n")
# create the new txt file for odd but tripled