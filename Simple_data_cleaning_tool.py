import re

data_list = ["Hello!", "WORLD", "", "hello", " Machine   Learning "]
list1 = []
for i in range(len(data_list)):
    # Remove special character from a word in a list
    data_list[i] = re.sub(r'[^A-Za-z0-9 ]', '', data_list[i])
    # Remove
    data_list[i] = data_list[i].strip()
    # Remove empty values
    if data_list[i] == "" or data_list[i] == " ":
        continue
        # remove multiple spaces in the middle
    data_list[i] = " ".join(data_list[i].split())
    # Remove duplicates
    if data_list[i] in list1:
        continue
    # Converting text into lower case and then append in a new list
    list1.append(data_list[i].lower())

print(list1)
