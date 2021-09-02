import random

numbers = '0123456789'
upperAlphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lowerAlphabet = 'abcdefghijklmnopqrstuvwxyz'
specialCharacters = '@$%^&*'

finalText = list(numbers + upperAlphabet + lowerAlphabet + specialCharacters)

userPassword = []
finalPassword = ""
userInput = input("Enter number for password charachters -> ")
i = 0
while i < int(userInput):
    passwordGenerate = random.choice(finalText)
    userPassword.append(passwordGenerate)
    i = i + 1


for m in userPassword:
    finalPassword += m

print("your password : " + finalPassword)