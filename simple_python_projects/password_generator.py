import random

print('Welcome To Password Generator')

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@%^&*().,?0123456789'

number = int(input('Number of passwords to generate'))

length = int(input('Enter the length of your password'))

print('\n Here are your passwords: ')

for pwd in range(number):
    passwords = ''
    for c in range(length):
        passwords += random.choice(chars)
    print(passwords)
