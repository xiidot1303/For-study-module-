n = input('Natural sonni kiriting: ')
l = []
for i in n:
    l.append(i)
r = []

m = max(l)
r.append(m)

while m in l:
    l.remove(m)

m = max(l)
r.append(m)

a, b = r
print('Natija: ', a, b)