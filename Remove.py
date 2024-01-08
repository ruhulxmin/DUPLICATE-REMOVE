#coded by ruhul xmin
#https://github.com/ruhulxmin
from os import system as clr
clr('clear')
print(60*'~')
print("      =>DUPLICATE ID REMOVER FROM FILE  ")
print("      =>CODED BY          :RUHUL AMIN BOKSHI")
print("      =>Facebook          :Ruhul Xmin BokXi
print("      =>Github            :ruhulxmin
print(60*'~')
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
print(f"DUPLICATE FILE REMOVE SAVE AS : {output_file}")
