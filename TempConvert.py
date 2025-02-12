# TempConvert.py
# Name: [Your Name]
# Date: [Today's Date]
# Assignment: Convert Fahrenheit to Celsius

def main():
    try:
        # Prompt the user for a Fahrenheit temperature
        tempF = float(input("Enter the temperature in Fahrenheit: "))
    except ValueError:
        print("Invalid input! Please enter a numeric value.")
        return  # Exit the program if the input is not valid

    # Convert the temperature to Celsius using the formula:
    # Celsius = (Fahrenheit - 32) * 5/9
    tempC = (tempF - 32) * 5 / 9
    
    # Round the Celsius temperature to 1 decimal place
    tempC = round(tempC, 1)
    
    # Output the converted temperature
    print(f"{tempF}°F is equivalent to {tempC}°C.")

if __name__ == '__main__':
    main()

