RoundGame = int(input("How many round?"))
for round in range(1, RoundGame + 1):
    score = float(input(f"Score for round {round}:"))
    if score >= 100:
       score = (score + (score*0.2))
       
      