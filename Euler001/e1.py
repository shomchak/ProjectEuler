i, j, k = 1, 1, 1
sum3 = 0
sum5 = 0
sum15 = 0
while i <= 334:
    if 3 * i < 1000:
        sum3 = 3 * i + sum3
    i = i + 1
while j <= 200:
    if 5 * j < 1000:
        sum5 = 5 * j + sum5
    j = j + 1
while k <= 70:
    if 15 * k < 1000:
        sum15 = 15 * k + sum15
    k = k + 1
print sum3  + sum5 - sum15
