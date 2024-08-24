current_tution_fee = int(input("Enter the current tution fees: "))
increase_rate = 7/100 # 7%
double = current_tution_fee * 2
year = 0

while (current_tution_fee <= double):
    current_tution_fee = current_tution_fee + (current_tution_fee * increase_rate)
    year = year + 1

print("The current tution fee is doubled in", year,"years.")