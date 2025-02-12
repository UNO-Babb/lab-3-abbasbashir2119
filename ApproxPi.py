# ApproxPi.py
# Name: [Your Name]
# Date: [Today's Date]
# Assignment: Approximate Pi using the Nilakantha series (Extra Credit)

import math
import time

def main():
    realPi = math.pi

    # Ask the user for the desired decimal precision (0 to 10)
    while True:
        try:
            precision = int(input("Enter desired decimal precision (0-10): "))
            if 0 <= precision <= 10:
                break
            else:
                print("Please enter an integer between 0 and 10.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    # Set the tolerance based on the precision. 
    # For example, if precision=1, then a tolerance of 0.05 ensures rounding correctness.
    tolerance = 0.5 * 10 ** (-precision)

    # Initialize variables for the Nilakantha series:
    # π = 3 + 4/(2×3×4) - 4/(4×5×6) + 4/(6×7×8) - ...
    approxPi = 3.0      # starting value
    term_sign = 1       # alternating sign: +, -, +, ...
    i = 2               # denominator begins with 2, 3, 4
    iterations = 0      # counter for the number of terms added

    start = time.time()

    # Add terms until the approximation is within the desired tolerance.
    while abs(approxPi - realPi) > tolerance:
        term = 4.0 / (i * (i + 1) * (i + 2))
        approxPi += term_sign * term
        term_sign *= -1  # alternate the sign for the next term
        i += 2          # move to the next set (2, 3, 4 then 4, 5, 6, etc.)
        iterations += 1

    end = time.time()
    elapsedTime = end - start

    # Display the results.
    print("\nApproximated Pi: {:.15f}".format(approxPi))
    print("Actual Pi:       {:.15f}".format(realPi))
    print("Difference:      {:.15f}".format(abs(approxPi - realPi)))
    print("Iterations:      ", iterations)
    print("Elapsed time:    {:.6f} seconds".format(elapsedTime))

if __name__ == '__main__':
    main()

