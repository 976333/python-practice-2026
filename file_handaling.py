# | Mode | Meaning |
# |---|---|
# | `r` | Read |
# | `w` | Write |
# | `a` | Append |
# | `x` | Create new file |
# | `r+` | Read + Write |
# | `w+` | Write + Read |
# | `a+` | Append + Read |


# | Method | Purpose |
# |---|---|
# | `open()` | Open file |
# | `read()` | Read complete file |
# | `readline()` | Read one line |
# | `readlines()` | Read all lines as list |
# | `write()` | Write text |
# | `writelines()` | Write multiple lines |
# | `close()` | Close file |
# | `seek()` | Move file pointer |
# | `tell()` | Get pointer position |




path = "demo.txt"

with open (path,"r",encoding="utf-8")as file:
    data = file.readlines()


line = data[0].strip().split(",")
print(line)


new_list =[]

for i in range(1,len(line)):
    new_data = int(line[i])
    new_list.append(new_data)

print(new_list)