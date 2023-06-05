import random

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()_+'


# Function to generate random password
def generatePassword():
    pass_length = int(input('Enter the length of password: '))
    pass_count = int(input('Enter the number of passwords: '))
    passwords = []
    for _ in range(pass_count):
        password = ''
        for _ in range(pass_length):
            password += random.choice(chars)
        passwords.append(password)
    return passwords


# Function to write passwords to file
def writePasswords(passwords):
    with open('passwords.txt', 'a') as f:
        for password in passwords:
            f.write(password + '\n')


# Function to read passwords from file
def readPasswords():
    with open('passwords.txt', 'r') as f:
        for line in f.readlines():
            print(line.rstrip())  # Strip newline character before printing


# Function to clear passwords file
def clearPasswords():
    with open('passwords.txt', 'w') as f:
        f.truncate(0)
    print('Passwords file cleared.')


# Main function
def main():
    while True:
        print('\nWelcome to Random Password Generator')
        print('1. Generate Password')
        print('2. Read Passwords')
        print('3. Clear Passwords')
        print('4. Exit')
        choice = int(input('Enter your choice: '))

        if choice == 1:
            passwords = generatePassword()
            print('\nYour passwords are: ')
            for password in passwords:
                print(password)
            writePasswords(passwords)

        elif choice == 2:
            print('\nPasswords till created are:\n')
            readPasswords()

        elif choice == 3:
            clearPasswords()

        elif choice == 4:
            exit()

        else:
            print('\nInvalid choice')


# Calling main function
main()

# End of program
