import random

letters = [
    'A','B','C','D','E','F','G','H','I','J','K','L','M',
    'N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
    'a','b','c','d','e','f','g','h','i','j','k','l','m',
    'n','o','p','q','r','s','t','u','v','w','x','y','z'
]

numbers = ['0','1','2','3','4','5','6','7','8','9']

symbols = [
    '!', '@', '#', '$', '%', '^', '&', '*', '(', ')',
    '-', '_', '=', '+', '[', ']', '{', '}', '|',
    ';', ':', "'", '"', ',', '.', '<', '>', '/', '?', '`', '~'
]

password = []

print("Welcome to the PyPassword generator!")
letterswanted = int(input("How many letters would you like in your password?\n"))
numberswanted = int(input("How many numbers would you like?\n"))
symbolswanted = int(input("How many symbols would you like?\n"))

length = letterswanted + numberswanted + symbolswanted

for i in range(length):
    if letterswanted > 0 and numberswanted > 0 and symbolswanted > 0:
        all = random.randint(0,2)
        if all == 0:
            password.append(random.choice(letters))
            letterswanted -= 1
        if all == 1:
            password.append(random.choice(numbers))
            numberswanted -= 1
        if all == 2:
            password.append(random.choice(symbols))
            symbolswanted -= 1
    if letterswanted > 0 and numberswanted > 0 and symbolswanted == 0:
        all = random.randint(0,1)
        if all == 0:
            password.append(random.choice(letters))
            letterswanted -= 1
        if all == 1:
            password.append(random.choice(numbers))
            numberswanted -= 1
    if letterswanted > 0 and numberswanted == 0 and symbolswanted > 0:
        all = random.randint(0,1)
        if all == 0:
            password.append(random.choice(letters))
            letterswanted -= 1
        if all == 1:
            password.append(random.choice(symbols))
            symbolswanted -= 1
    if letterswanted == 0 and numberswanted > 0 and symbolswanted > 0:
        all = random.randint(0,1)
        if all == 0:
            password.append(random.choice(numbers))
            numberswanted -= 1
        if all == 1:
            password.append(random.choice(symbols))
            symbolswanted -= 1
    if letterswanted == 0 and numberswanted == 0 and symbolswanted > 0:
        password.append(random.choice(symbols))
        symbolswanted -= 1
    if letterswanted == 0 and numberswanted > 0 and symbolswanted == 0:
        password.append(random.choice(numbers))
        numberswanted -= 1
    if letterswanted > 0 and numberswanted == 0 and symbolswanted == 0:
        password.append(random.choice(letters))
        letterswanted -= 1

print(password)

output = ''.join(password)
print(f"Your password is {output}")

# Alternate method (with shuffle)

# import random

# letters = [
#     'A','B','C','D','E','F','G','H','I','J','K','L','M',
#     'N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
#     'a','b','c','d','e','f','g','h','i','j','k','l','m',
#     'n','o','p','q','r','s','t','u','v','w','x','y','z'
# ]

# numbers = ['0','1','2','3','4','5','6','7','8','9']

# symbols = [
#     '!', '@', '#', '$', '%', '^', '&', '*', '(', ')',
#     '-', '_', '=', '+', '[', ']', '{', '}', '|',
#     ';', ':', "'", '"', ',', '.', '<', '>', '/', '?', '`', '~'
# ]

# password = []

# print("Welcome to the PyPassword generator!")
# letterswanted = int(input("How many letters would you like in your password?\n"))
# numberswanted = int(input("How many numbers would you like?\n"))
# symbolswanted = int(input("How many symbols would you like?\n"))

# for i in range(letterswanted):
#     password.append(random.choice(letters))
# for i in range(numberswanted):
#     password.append(random.choice(numbers))
# for i in range(symbolswanted):
#     password.append(random.choice(symbols))

# print(password)
# random.shuffle(password)

# output = "".join(password)

# print(f"Your password is {output}")