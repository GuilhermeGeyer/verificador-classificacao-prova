
import string

letters = string.ascii_uppercase
c = 1
FIRST_NAME = ''
LAST_NAME = ''

with open('resultados.txt', 'r') as file:
    lines = [line.replace(',', '.') for line in file if line[0] in letters]
    new_lines = [line.split() for line in lines]
    new_lines = [i for i in new_lines if not i[-2][0] == "A"]
    new_lines.sort(key=lambda x: float(x[-2]), reverse=True)
    for i in new_lines:
        if (FIRST_NAME in i and LAST_NAME in i) or (c <= 10):
            print(c, new_lines[c - 1])
        c += 1
