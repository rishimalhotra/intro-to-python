# custom-functions/my_functions.py

# TODO: define temperature conversion function here

# TODO: define gradebook function here

#def celsius_to_fahrenheit(c)
    #return (1.8 * x) + 32
#x = f(0)
#print(x) #> 11


def celsius_to_farenheit(celsius_temp):
    #print(celsius_temp)
    f_temp = 9/5 * celsius_temp + 32
    return f_temp

#replace(parameter_list) with(celsius_temp)


if __name__ == "__main__":

    print("--------------------")
    #print("celsius_to_farenheit")
    print("CUSTOM FUNCTIONS EXERCISE...")

    print("--------------------")
    c = 0
    print("THE CELSIUS TEMP IS:", c, "DEGREES")
    f = celsius_to_farenheit(c)
    print("THE FAHRENHEIT EQUIVALENT IS:", f, "DEGREES")


def numeric_to_letter_grade(n):
    if n < 60:
        return "F"
    if n < 70:
        return "D"
    if n < 80:
        return "C"
    if n < 90:
        return "B"
    else:
        return "A"

if __name__ == "__main__":
       
    print("--------------------")
    score = 87.5
    print("THE NUMERIC SCORE IS:", score)
    grade = numeric_to_letter_grade(score)
    print("THE LETTER-GRADE EQUIVALENT IS:", grade)

