hours = int(input())
if hours > 2:
    if hours > 5:
        charges = hours - 5 * 3 + 4
    else:
        charges = hours - 3 * 2
else:
    charges = 0
if charges > 30:
    parkingFee = 30
else:
    parkingFee = charges
print(parkingFee)
