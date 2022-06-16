i = 1
skips = [23, 24, 25, 26]
while i <= 50:
    if i not in skips:
        print(i)
    i += 1

#Alternatively:
i = 1
while i <= 50:
    if i == 23:
        i = 27
    print(i)
    i += 1