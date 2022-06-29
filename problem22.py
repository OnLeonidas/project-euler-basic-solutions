import string

f = open('names.txt')
#inserting names from names.txt in contents list
contents = f.read().replace('"', '').split(',')
f.close()
#names = contents sorted
names = sorted(contents)
total_name, total_local, total_global = 0, 0, 0

for name in names:
    for letter in name:
        #sum of all letter position in name
        total_name += string.ascii_uppercase.index(letter) + 1
    #multiplying name value with name position in name list
    total_local = total_name * (names.index(name) + 1)
    total_global += total_local
    total_name = 0

print(total_global)
