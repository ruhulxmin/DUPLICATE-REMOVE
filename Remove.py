#coded by ruhul xmin
#https://github.com/ruhulxmin
from os import system as clr
clr('clear')

print('\33[1;92m╔━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╗')
print('\33[1;92m║➣\033[1;91m DEVOLPER      : Ruhul Xmin\33[1;92m               ')
print('\33[1;92m║➣ FACEBOOK      : Ruhul Xmin BokXi    \33[1;92m                  ')
print('\33[1;92m║➣\033[1;34m GITHUB        : ruhulxmin               \33[1;92m           ')
print('\33[1;92m║➣\033[1;35m TOOLS         : DUPLICATE ID REMOVER \33[1;92m                  ')
print('\33[1;92m║➣\033[1;35m VERSION       : V1.0  \33[1;92m                  ')
print('\33[1;92m╚━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╝')
input_file = input("INPUT FILE NAME : ")
output_file = input("OUTPUT FILE NAME : ")
unique_ids = {}
with open(input_file, 'r') as infile:
    for line in infile:
        line = line.strip()
        values = line.split('|')
        if len(values) == 3:
            id, pas, coki = values
            key = f"{id}|{pas}|{coki}"
            if key not in unique_ids:
                unique_ids[key] = line
        else:
            id, pas = values
            key = f"{id}|{pas}"
            if key not in unique_ids:
                unique_ids[key] = line
with open(output_file, 'w') as outfile:
    for line in unique_ids.values():
        outfile.write(line + '\n')
print(f"DUPLICATE REMOVED FILE SAVED AS: {output_file}")
import os; import time; os.system('xdg-open https://facebook.com/ruhul.xmin'); time.sleep(1)