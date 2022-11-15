## setup random password generator using libraries random and string
import string
import random


def main():
    alphabet = list(string.ascii_lowercase)
    lore = list(string.digits)


    x = random.choices(alphabet, k = 25)
    x2 = random.choices(lore, k=15)

    webname = input("what is the website: ")

    val1 = ''.join(x)
    val2 = ''.join(x2)
    password = str(val1 + val2)
    text = 'Your password is : '
    while True:
        file = open('data.txt', 'a')
        file.write("Website :" + str(webname) + ' | Password: ' + password + '\n')
        file.close
        break
    return text + password

print(main())