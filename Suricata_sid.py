import re


with open('input.rules', 'r') as file:
    text = file.read()

new_text = ""
sid_value = 1


for line in text.split("\n"):
    match = re.search(r"sid:(\d+)", line)
    if match:
        
        new_line = line.replace(match.group(1), str(sid_value))
        new_text += new_line + "\n"
        sid_value += 1
    else:
        new_text += line + "\n"


with open('output.rules', 'w') as file:
    file.write(new_text)
