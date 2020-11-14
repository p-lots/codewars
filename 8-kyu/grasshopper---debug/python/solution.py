def weather_info(temp):
    c = convert_to_celsius(temp)
    return f'{c} is {"above " * (c > 0)}freezing temperature'
    
def convert_to_celsius(temperature):
    return (temperature - 32) * (5/9)