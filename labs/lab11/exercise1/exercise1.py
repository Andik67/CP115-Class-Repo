speed = int(input())
total_readings = 0
current_streak = 0
longest_streak = 0 
while speed != -1:
    total_readings += 1
    speed = int(input())
    if speed < 20:
      current_streak += 1
      if current_streak > longest_streak:
         longest_streak = current_streak
    else:
       current_streak = 0
print(total_readings)
print(longest_streak)


    


   


