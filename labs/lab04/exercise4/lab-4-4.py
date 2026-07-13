weight = int(input())
tiketPrice = int(input())
if weight > 15:
    tiketPrice = weight - 15 * 4 + tiketPrice
else:
    tiketPrice = tiketPrice
if weight == 0:
    finalPrice = tiketPrice - 10
else:
    finalPrice = tiketPrice
print(finalPrice)
