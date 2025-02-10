[![Open in Codespaces](https://classroom.github.com/assets/launch-codespace-2972f46106e565e64193e422d61a12cf1da4916b45550586e14ef0a7c637dd04.svg)](https://classroom.github.com/open-in-codespaces?assignment_repo_id=18110889)
# Lab 3 - CIST 1600
Conditions, boolean logic, logical operators; ranges;
Control statements: if-else, loops (for, while); short-circuit evaluation

### Temperature Conversion
In Homework 1, you will need to convert from Kelvin temperatures to Fahrenheit. This is a fairly standard (cliché?) computer science exercise. In this program, I would like you to prompt the user for degrees in Fahrenheit, and convert to Celsius. This is analogous to the problem in your homework but not exactly the same.

#### Precision
When dealing with decimal values, it is often useful to round data to make it more presentable to the user. Python has several methods to round, here are a few.

```
num = 3.1415926
num = num * 100 #Multiply by 100
num = int(num) #drop the decimal part
num = num / 100.0 #divide by 100 to get 2 decimal points back
print(num)
```
What are the problems with this method?
```
num = 3.1415926
num = round(num, 2) # rounds to two places
print(num)
```
Are there any issues with this method?

## TempConvert.py
Ask user for a temperature in Fahrenheit, convert to Celsius.
You will need to look up the conversion factor online.

## Rock Paper Scissors (RPS.py)
We will be creating the class game of Rock, Paper, Scissors.

Example game:
```
Select Rock, Paper, or Scissors (R, P, S): R
Player chose: Rock
Computer chose: Scissors
You win!

Would you like to play again? (Y/N): Y

Select Rock, Paper, or Scissors (R, P, S): R
Player chose: Rock
Computer chose: Paper
You lose.

Would you like to play again? (Y/N): N

Final Stats:
Wins  Ties  Losses
----  ----  ------
1     0     1
```

## Approximating Pi (ApproxPi.py) - Optional for extra credit
There are many ways to calculate the value of pi. One method is with the following sequence.
> pi = 4/1 - 4/3 + 4/5 - 4/7 + 4/9 - 4/11 + ...  

As this series progresses, the value of pi gets more accurate. We want to use this series to test the speed of our computer. By calculating pi to a given decimal precision, we are able to essentially have a "stopwatch" time for competition. This lets us know how many floating point operations (FLOPS) our computer is capable of in a rough approximation.

Sample run:
```
How many decimal points to compute (0 - 10): 5
Pi: 3.14159
Calculated in 0.2004985809326172 seconds.
```

---
## Testing your code
You may not actually know that your code works until you fully test what you have written. It is often a good idea to get someone else to run your program, they may do something you had not anticipated which could show you a possible flaw or at least a design issue.

## End of class
- Add a commit message
- Commit to GitHub
- Sync work with Repo
- Submit your repo link to Canvas
