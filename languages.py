import time

def main():
    print("1) Japanese")
    print("2) French")
    print("3) German")
    choice = input("What language?: ")
    if choice == "1":
        sentence_japanese()
    elif choice == "2":
        sentence_french()
    elif choice == "3":
        sentence_german()
    else:
        print("Please enter a number from 1-3 and try again.")
        main()
    
def sentence_japanese():
    print("1) I want a cat.")
    print("2) I'm hungry.")
    print("3) I am studying.")
    choice = input("What sentence would you like to translate? ")
    if choice == "1":
        time.sleep(1)
        print("Watashi neko ga hoshii")
        print("私猫が欲しい")
        again()
    elif choice == "2":
        time.sleep(1)
        print("Onaka ga suita")
        print("お腹がすいた")
        again()
    elif choice == "3":
        time.sleep(1)
        print("Ima bennkyo o shimasu")
        print("今勉強します")
        again()
    else:
        print("Try again. Enter a valid number.")
        sentence_japanese()

def sentence_french():
    print("1) I want a cat.")
    print("2) I'm hungry.")
    print("3) I am studying.")
    choice = input("What sentence would you like to translate? ")
    if choice == "1":
        time.sleep(1)
        print("Je veux un chat.")
        again()
    elif choice == "2":
        time.sleep(1)
        print("J'ai faim.")
        again()
    elif choice == "3":
        time.sleep(1)
        print("J'étudie")
        again()
    else:
        print("Try again. Enter a valid number.")
        sentence_french()

def sentence_german():
    print("1) I want a cat.")
    print("2) I'm hungry.")
    print("3) I am studying.")
    choice = input("What sentence would you like to translate? ")
    if choice == "1":
        time.sleep(1)
        print("Ich möchte eine Katze")
        again()
    elif choice == "2":
        time.sleep(1)
        print("Ich habe Hunger")
        again()
    elif choice == "3":
        time.sleep(1)
        print("Ich studiere")
        again()
    else:
        print("Try again. Enter a valid number.")
        sentence_german()

def again():
    print("")
    choice = input("Would you like to translate another sentence? yes or no ")
    if choice.lower() == "yes".lower():
        main()
    else:
        print("Quitting program...")
        exit()

main()