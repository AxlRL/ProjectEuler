svar = 0
x, y = 0, 1
while x < 4000000:
    x, y = y, x + y
    if x % 2:
        continue
    svar += x

print (svar)
