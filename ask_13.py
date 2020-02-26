def check_card(card):
    number_of_digits = len(card)
    sum_of_numbers = 0
    flag = False
    i = number_of_digits - 1
    while i >= 0: # This loop starts from the last digit of the card number and stops when it reaches the first digit.
        dgt = card[i]
        digit = int(dgt)
        if (flag == True): # We use flag to indicate every other digit.Then we multiply it by 2.
            digit *= 2
        sum_of_numbers += digit // 10
        sum_of_numbers += digit % 10
        flag = not(flag) # Every other time that the loop executes flag is true.
        i = i - 1
    return (sum_of_numbers % 10 == 0)

print("Type your credit card number: ")
card_number = int(input())
card = str(card_number) # We turn users input into a string just so we can have the length of it later in the function.
if check_card(card): # This if checks if the function check_card returns true or false and prints a sentence for each case.
    print("\nThis card number is valid!")
else:
    print("\nThis card number is not valid!")
    
