# question 1 task 2

def conversion(fahrenheit):
    try: 
        fahrenheit = float(fahrenheit)
        celsius = (fahrenheit - 32) * 5 / 9
    except ValueError:
        print("Please enter a valid number.")
        return None
# question 1 task 3
    else:
        return celsius
# question 1 task 4
    finally:
        print("Thank you for using the weather forecast application.")
        

# question 1 task 1

get_temp = input("Please enter the temperature in Fahrenheit: ")

celsius = conversion(get_temp)

if celsius is not None:
    print(f"{get_temp} degrees Fahrenheit is {celsius:.2f} degrees Celsius.")
