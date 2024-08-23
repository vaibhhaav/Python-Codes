seconds = int(input("Enter total number of seconds"))
hours = seconds // 3600
minutes = (seconds % 3600) // 60
print ("Time in hours & minutes =",hours,":",minutes)

nseconds = seconds % 60 
print ("Time in hours, minutes & seconds =",hours,":",minutes,":",nseconds)