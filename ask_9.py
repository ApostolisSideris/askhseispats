print("Give me a number")
number = int (input())
if number < 0: # If the number that the user gave is negative then we turn it into a positive
    number = abs(number)
    num = number
else:
    num = number
sum_of_digits = 0
i = 0
while sum_of_digits == 0:   
    number = number * 3 + 1
    if num >= 0  and num < 3: #This if checks if the given number is in the range of (0-2).If its true then breaks the loop cause these numbers will always be one digit numbers after our calculations
        print("This is our one digit number ", number)
        break
    else:
        while number != 0: #This loop firstly finds each digit of our given number and the it calculates the sum of his digits
            digit = number % 10
            sum_of_digits += digit
            number = number // 10
    if sum_of_digits < 0 or sum_of_digits > 9: #This if checks if the sum is not a single digit number
        number = sum_of_digits
        sum_of_digits = 0
    i = i + 1 # i will tell us how many times the loop was executed
if i != 0: # If the loop breaks the i will be 0 if the loop doesn't break then we need to print our result.
    print("After our calculations the one digit number is ", sum_of_digits)

