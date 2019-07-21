# Open file for reading
ReadFile = open("test.txt", "r")
# Set Loop counter
Loopcount = 1
# Get user input
Num1=int(input("Enter number of lines to extract from file: "))
# Start to loop through file until Loopcount is greater then user input
while Loopcount <= Num1:
    # Print counter text followed by line from file
    print("Line Counter", Loopcount)
    print(ReadFile.readline())
    # Increment Loop counter
    Loopcount += 1
