a = input('Введите символы')

b = ''

c = 0
d = ''

for s in a:
    if not d:
        d = s
        c += 1
    else:
        if s != d:
            b += d + str(c)
            d = s
            c = 1
        else:
            c += 1

b += d + str(c)

print(b)