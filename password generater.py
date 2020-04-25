#imports da things
from random import *
from string import *

#defines password
def password():

    #sets the to print
    password=""

    #for de loop
    count = 0

    #asks for length of pass
    length=int(input("how long do you want your password"))

    #while loop(while count not equal to length)
    while count != length:

        #makes the lists that are randomly chosen from
        upper = [choice(ascii_uppercase)]
        lower = [choice(ascii_lowercase)]
        num = [choice(digits)]
        symbol = [choice(punctuation)]

        #adds everything together
        everything = upper + lower + num + symbol

        #takes one random element from the added list
        password += choice(everything)

        #ends da loop by adding 1 to count(0_0)
        count += 1

    #prints the password and calls da function
    print(password)
password()
