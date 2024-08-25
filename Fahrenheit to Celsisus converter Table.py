from Fahrenheit_to_Celsisus_and_Celsius_to_Fahrenheit import fahrenheit_to_celsius

def main():
    lower_temperature = -50
    upper_temperature = 250
    step = 10

    for degrees_f in range(lower_temperature,upper_temperature + 1, step):
        degrees_c = fahrenheit_to_celsius(degrees_f)
        print(format(degrees_f,"3d"), '\t', format(degrees_c,"5.1f"))

main()