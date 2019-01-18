
'''

Bitpass Password Generator

A password generator utility which utilizes the slot technique
to generate strong passwords of required length having combinations
of lower and upper characters, digits and symbols.

'''


def passwordgen(n):

    import string
    import random

    slot = [0, 0, 0, 0, 0]
    
    for x in range(n):
        r = random.randint(0,4)
        slot[r] += 1
    
    lower_letter = random.choices(string.ascii_lowercase, k=slot[0])
    upper_letter = random.choices(string.ascii_uppercase, k=slot[1])
    digits = random.choices(string.digits, k=slot[3])
    symbols = random.choices('!@#$%^&*_+-|/[]}{><?:",.', k=slot[2])
    symbols2 = random.choices('!@#$%^&*_+-|/[]}{><?:",.', k=slot[4])    
    
    password = digits + upper_letter  + symbols + lower_letter + symbols2
    random.shuffle(password)
    
    print(''.join(password))


def main():
    
    n = int(input('Enter total number of characters : '))
    passwordgen(n)
        
if __name__ == "__main__":
    main()
