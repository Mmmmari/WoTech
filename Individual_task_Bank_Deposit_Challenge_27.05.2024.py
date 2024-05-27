# EASY
# Welcoming the user to the bank
user = input('Please insert your name: ')
print(f'Hello {user}! Welcome to BestBank! ')

# Initiating balance = 0
balance = 0

# Asking the user to input the amount of money they want to deposit.
deposit = int(input('Please type the amount of money you would like to deposit! '))

#Adding the deposit amount to the total balance
balance = balance + deposit
print(f'Your new balance is {balance}. ')

# Asking the user if they want to make another deposit or exit the bank.
# If they choose to make another deposit, repeat the process (while True).
# If not, print the total amount deposited and exit the bank.
while True:
    next_step = input('Would you like to make another deposit? If not, please type "exit"! ')
    if next_step.lower() == 'yes':
        deposit = int(input('Please type the amount of money you would like to deposit! '))
        balance = balance + deposit
        print(f'Your new balance is {balance}. ')
    elif next_step.lower() == 'exit':
        print(f'Your balance is {balance}. Thank you for visiting BestBank, {user}! Have a great day! ')
        break
    else:
        input('That is not a valid input. Please type either "yes" or "exit"! ')



# MEDIUM
# Using `try` and `except` to handle non-integer inputs for deposits.
user = input('Please insert your name: ')
print(f'Hello {user}! Welcome to BestBank! ')

# Initiating balance = 0
balance = 0

# Asking the user to input the amount of money they want to deposit.
while True:
    try:
        deposit = int(input('Please type the amount of money you would like to deposit! '))
        break
    except: 
        print('That is not a valid input. Please type a number! ')

#Adding the deposit amount to the total balance
balance = balance + deposit
print(f'Your new balance is {balance}. ')

# Asking the user if they want to make another deposit or exit the bank.
# If they choose to make another deposit, repeat the process (while True).
# If not, print the total amount deposited and exit the bank.
while True:
    next_step = input('Would you like to make another deposit? If not, please type "exit"! ')
    if next_step.lower() == 'yes':
        deposit = int(input('Please type the amount of money you would like to deposit! '))
        balance = balance + deposit
        print(f'Your new balance is {balance}. ')
    elif next_step.lower() == 'exit':
        print(f'Your balance is {balance}. Thank you for visiting BestBank, {user}! Have a great day! ')
        break
    else:
        input('That is not a valid input. Please type either "yes" or "exit"! ')



# HARD
# Adding bank withdrawal (if user wants to withdraw money the balance decreases)
# If the balance becomes negative, withdrawal is not possible.
# Adding check balance optionality
user = input('Please insert your name: ')
print(f'Hello {user}! Welcome to BestBank! ')

# Initiating balance = 0
balance = 0

# Asking the user to input the amount of money they want to deposit.
while True:
    try:
        deposit = int(input('Please type the amount of money you would like to deposit! '))
        break
    except: 
        print('That is not a valid input. Please type a number! ')

#Adding the deposit amount to the total balance
balance = balance + deposit
print(f'Your new balance is {balance}. ')

# Asking the user if they want to make another deposit or exit the bank.
# If they choose to make another deposit, repeat the process (while True).
# If not, print the total amount deposited and exit the bank.
while True:
    next_step = input('What would you like to do next? You can check balance, withdraw, deposit or exit. ')
    if next_step.lower() == 'check balance':
        print(f'Your new balance is {balance}. ')
    elif next_step.lower() == 'deposit':
        deposit = int(input('Please type the amount of money you would like to deposit! '))
        balance = balance + deposit
        print(f'Your new balance is {balance}. ')
    elif next_step.lower() == 'withdraw':
        withdrawal = int(input('Please type the amount of money you would like to withdraw! '))
        if balance >= withdrawal:
            balance = balance - withdrawal
            print(f'Your new balance is {balance}. ')
        else: 
            print(f'Your balance is {balance} and that is not enough to withdraw {withdrawal}. ')
    elif next_step.lower() == 'exit':
        print(f'Your balance is {balance}. Thank you for visiting BestBank, {user}! Have a great day! ')
        break
    else:
        print('That is not a valid input. Please type either "check balance", "withdraw", "deposit" or "exit"! ')





