# Open file for reading
ReadFile = open("test.txt", "r")
# Set Loop counter and number of lines in file
Loopcount = 1
Linecount = 0
with ReadFile as f:
    for line in f:
        Linecount += 1
# Get user input
Num1=int(input("Enter number of lines to extract from file: "))
# Check that user input is in range
if Num1 <1:
    print("Extraction of less than one not possible")
if Num1 > Linecount:
    print("That's a bigger number then lines in the file!")
if Num1 >= 1 and Num1 <= Linecount:
    ReadFile = open("test.txt", "r")
# Start to loop through file until Loopcount is greater then user input
    while Loopcount <= Num1:
        # Print counter text followed by line from file
        print("Line Counter", Loopcount)
        print(ReadFile.readline())
        # Increment Loop counter
        Loopcount += 1
