# this script opens a file, reads it and prints the specified number of characters

f = open("test.txt", "r")
n=int(input("Enter number of characters to extract from file: "))
print(f.read(n))
