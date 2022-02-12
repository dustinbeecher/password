import random as rand
letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
symbols = ['~','!','@','#','$','%','^','&','*','(',')','_','-','+','=','{','[','}',']','|','\\',':',';',"\"",'\'','<',',','>','.','?','/']


def generatePassword(passwordLength):
    while passwordLength > 0:
        randNumber = rand.randint(0,9)
        randLetter = rand.choice(letters)
        randSymbol = rand.choice(symbols)
        randCharacter = rand.choice([randNumber, randLetter, randSymbol])
        password.append(randCharacter)
        passwordLength-=1
    return password


while True:
    password = []
    passwordLength = int(input("\nInsert password length.\n"))
    generatePassword(passwordLength)
    print(*password, sep="")
