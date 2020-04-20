n = range(5)
names = []
For n:
    names.append(input("Insert name: "))

print(names)

namesLowerCase = [name.lower() for name in names]
print(namesLowerCase)

namesTitle = [name.title() for name in names]
print(namesTitle)

namesBoth = [name.lower().title() for name in names]
print(namesBoth)
