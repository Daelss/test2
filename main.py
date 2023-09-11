vvod = input('Введите строку: ')
dict_chars = {}
for c in vvod :
  dict_chars[c] = vvod.count(c)

for c in dict_chars:
  print(c, '->', dict_chars[c])