p = (0+1j)
max_iter = 100

ans = []
for a in range(-10, 10):
    for b in range(-10, 10):
        x = a + b*1j  
        if abs(x) == 0:
            continue  
        for i in range(max_iter):
            if abs(x) == 0:
                break
            x = p + p / x
        ans.append([a,b,x])

print(ans)