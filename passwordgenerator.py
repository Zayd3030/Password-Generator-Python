import random

uppercase_letters = string.ascii_uppercase
lowercase_letters = string.ascii_lowercase
numbers = "0123456789"
symbols = "!£$%^&*()@#?"

upper, lower, nums, syms = True, True, True, True, 

all = ""

if upper:
    all += uppercase_letters
if lower:
    all += lowercase_letters
if nums:
    all += numbers
if syms:
    all += symbols

length = 10
amount = 10

for x in range(amount):
    password = "".join(random.sample(all, length))
    print(password)
