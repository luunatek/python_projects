user_input = input("Enter some words: ")
s = []
new_value = user_input.split()
for i in new_value:
    index_value = i[:10].split()
    s.append(index_value)

for i in enumerate(s):
    print(i)
