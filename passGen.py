import string
import secrets

def generatePassword(length, isContainLowercase, isContainUppercase, isContainDigits, isContainSymbols):
    chars = ''
    if isContainLowercase:
        chars += string.ascii_lowercase
    if isContainUppercase:
        chars += string.ascii_uppercase
    if isContainDigits:
        chars += string.digits
    if isContainSymbols:
        chars += string.punctuation
    if not chars:
        print("Please select at least one")
        return None
    else:
        return ''.join(secrets.choice(chars) for i in range(length))

try:
    length = int(input("Enter the length of password: "))
    isContainLowercase = input("Contain Lowercase (y/n): ").strip().lower() == 'y'
    isContainUppercase = input("Contain Uppercase (y/n): ").strip().lower() == 'y'
    isContainDigits = input("Contain Digits (y/n): ").strip().lower() == 'y'
    isContainSymbols = input("Contain Symbols (y/n): ").strip().lower() == 'y'
    password = generatePassword(length, isContainLowercase, isContainUppercase, isContainDigits, isContainSymbols)
    print(f"Generated Password: {password}")

except:
    print("Invalid password length")
