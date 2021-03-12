# Credit to https://www.geeksforgeeks.org/python-program-to-print-all-odd-numbers-in-a-range/ for the help in the code (the entire code, some value names are changed)
startofodd =)
endofodd = 100
for num in range(startofodd, endofodd + 1):
    if num % 2 != 0:
        print(num, end = " ")
