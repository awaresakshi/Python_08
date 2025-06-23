#split,set,fetch
x="Hello All! I am Sakshi Aware.Sanjivani College Of Engineering"
y=x.split()
z=len(x)
print(y)
print(len(x))
frequencies = {}
for i in y:
    if i in frequencies:
        frequencies[i] += 1
    else:
        frequencies[i] = 1
print(frequencies)