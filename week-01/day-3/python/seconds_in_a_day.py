# Write a program that prints the remaining seconds (as an integer) from a
# day if the current time is represented by the variables

current_hours = 14
current_minutes = 34
current_seconds = 42

total_seconds=24*60*60
past_seconds=14*60*60+34*60+42
remain_seconds=total_seconds - past_seconds
print(remain_seconds)