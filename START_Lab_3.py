
def lab3Question1(number, cutoff):
    # Take in two arguments - a number and a 'cutoff' (another number)
    # Return True if the number is less than the cutoff, False otherwise
    # Also, print a statement of "[Number] is less than [cutoff]" or "[Number] is not less than [cutoff]"
    # Where the [Number] and [cutoff] are the actual numbers passed in
    my_number = number
    my_cutoff = cutoff
    if my_number < my_cutoff:
        print(my_number, "is less than", my_cutoff)
        return True
    else:
        print(my_number, "is not less than", my_cutoff)
        return False
      
#print(lab3Question1(5,10))

def lab3Question2(decimal_number):
    # Take in an argument of a float (decimal) number.
    # Return "zero" if the number is 0, "positive" if the number is positive, and "negative" if the number is negative
    # Return "invalid" if the input is not a float
    my_dec_number = decimal_number
    try:
        my_dec_number != float
    except:
        return "invalid"
    
    if my_dec_number == 0:
        return "zero"
    elif my_dec_number < 0:
        return "negative"
    elif my_dec_number > 0:
        return "positive"
    
    
#print(lab3Question2(0))
#print(lab3Question2(-10))
#print(lab3Question2(2.5))



def lab3Question3(year):
    # Take in a number that represents a year
    # Return "21st century" if the year is between 2001 and 2100,
    # "20th century" if the year is between 1901 and 2000,
    # "19th century" if the year is between 1801 and 1900, 
    # "ancient" if the year is older
    # "invalid" if the input is not an acceptable year number. 
    my_year = year
    if type(my_year) != int:
        return "invalid"
    elif my_year >= 2101:
        return "invalid"
    
    if my_year >= 2001 and my_year <= 2100:
        return "21st century"
    elif my_year >= 1901 and my_year <= 2000:
        return "20th century"
    elif my_year >= 1801 and my_year <= 1900:
        return "19th century"
    elif my_year < 1800:
        return "ancient"

#print(lab3Question3(2001))
#print(lab3Question3(1992))
#print(lab3Question3(1834))
#print(lab3Question3(1750))
#print(lab3Question3(3000))
#print(lab3Question3('hi'))

def lab3Question4(number_1, number_2, number_3):
    # Take in three numbers as arguments
    # Return the largest of the three numbers
    # Return None if the inputs are not 3 numbers
    my_one = number_1
    my_two = number_2
    my_three = number_3
    if not isinstance(my_one,int):
        return None
    elif not isinstance(my_two, int):
        return None
    elif not isinstance(my_three, int):
        return None
    return max(my_one,my_two,my_three)


#print(lab3Question4(12,34,55))
#print(lab3Question4('hi',23,11))

def lab3Question5(temperature, scale_used):
    # Take in a temperature and the scale that the temperature is in - either "C" for Celsius or "F" for Fahrenheit (capitalized)
    # Return "Liquid" if water is in liquid state at that temperature
    # Return "Solid" if water is in solid state at that temperature
    # Return "Gas" if water is in gas state at that temperature
    # Return "Invalid" if the temperature or scale are invalid

    try:
        scale_used != "C" or "F"
        temperature == int(temperature)
    except ValueError:
        return "Invalid"
    
    if scale_used == "F":
        temperature = (temperature - 32) * 5 / 9 
    if temperature >= 100:
        return "Gas"
    elif temperature <= 0:
        return "Solid"
    elif temperature > 0 and temperature < 100:
        return "Liquid"
    else: 
        return "Invalid"

print(lab3Question5(25, "C"))
print(lab3Question5(19, "C"))
print(lab3Question5(-19, "C"))
print(lab3Question5("WHAT", "C"))
print(lab3Question5(30000,'C'))
      

