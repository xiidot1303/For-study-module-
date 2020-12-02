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
s = int(a)+int(b)
if int(n)/s == int(int(n)/s):
    print('karrali')
else:
    print('Karrali emas')