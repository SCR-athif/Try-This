#!/usr/bin/python3

# modules
import time
import pyfiglet
import brute
from termcolor import colored
from os import system

# Heading
system('clear')
name = "T R Y  T H I S"
print("."*100)
print(colored(pyfiglet.figlet_format(name, '3-d'), 'cyan'))
print("."*100)

print("""


 BRUTE FORCE MODES
********************

1.OTP BRUTE FORCE

2.DIRECTORY BRUTE FORCE

3.PASSWORD BRUTE FORCE WITH WORDLIST

4.PASSWORD BRUTE FORCE WITHOUT WORDLIST

""")
# Input Area
try:
    a = int(input("Enter your choice here : "))
    if a == 1:
        brute.otp()
    elif a == 2:
        brute.directory()
    elif a == 3:
        brute.passw()
    elif a == 4:
        brute.passnoword()
    else:
        print(colored("\nWrong Entry Try Again", 'red'))
        time.sleep(2)
        system('./main.py')
except ValueError:
    print(colored("\nPlease Enter correct data type", 'red'))
    time.sleep(1)
    system('./main.py')
except KeyboardInterrupt:
    ex = input("\n\nDo you want to exit (y/n): ")
    if ex == 'y' or ex == 'Y':
        print(colored("\nSee You Soon..", 'cyan'))
    else:
        system('./main.py')
