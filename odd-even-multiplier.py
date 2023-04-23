#Francis Niño A. Eugenio
#BSCPE 1-5 | Object Oriented Programing
#Even & Odd Multiplier

# open and read the source file
with open("integers.txt", "r") as source_file:
    numbers = [int(num) for num in source_file.read().split()]
# separate the even and odd in the source file
# create the new txt file for evem but doubled
# create the new txt file for odd but tripled