from math import cos, sin
max_iter = 100
x = 5
y = 5
ans = []
i = 0
while i < max_iter:
    ans.append({'i': i, 'x': x, 'y': y})
    x = cos(x)
    y = sin(y)
    i += 1

apple = 1 