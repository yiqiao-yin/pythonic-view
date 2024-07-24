groups = [[1, 2], [3, 4]]
print(groups)

for g in groups:
    for elem in g:
        print(elem)

c = [
    elem 
    for g in groups
    for elem in g
]

print(c)