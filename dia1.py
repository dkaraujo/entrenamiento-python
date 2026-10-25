print(7 / 2, 7 // 2, 7 % 2, type(6 / 3))

x = [1, 2, 3]
y = x
z = x.copy()
y.append(4)
print(x, y, z)
print(x is y, x is z)

print(id(x), id(y), id(z))
