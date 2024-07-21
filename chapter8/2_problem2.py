def temp_Converter(celsius):
    """Converts Celsius to Fahrenheit and vice versa"""
    if (celsius < -273):
        print("Temperature is below absolute zero") 
    elif celsius >= -273:
        fahrenheit = (celsius * 9/5) + 32
        print("the temp in  fahrenheit:  ",fahrenheit)
    
celsius=int(input("enter the celsius value of temp: "))
temp_Converter(celsius)