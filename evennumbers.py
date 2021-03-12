# Credit to https://www.geeksforgeeks.org/python-program-to-print-all-even-numbers-in-a-range/ for the help in the code (the entire code, some value names are changed)
startofeven = 2
endofeven = 18
for num in range(startofeven, endofeven  + 1):
    if num % 2 == 0:
        print(num, end = " ")
