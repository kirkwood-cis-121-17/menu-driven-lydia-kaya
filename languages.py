import time

def sentence_japanese():
    print("1) I want a cat.")
    print("2) I'm hungry.")
    print("3) I am studying.")
    choice = input("What sentence would you like to translate? ")
    if choice == "1":
        time.sleep(1)
        print("Watashi neko ga hoshii")
        print("私猫が欲しい")
    elif choice == "2":
        time.sleep(1)
        print("Onaka ga suita")
        print("お腹がすいた")
    elif choice == "3":
        time.sleep(1)
        print("Ima bennkyo o shimasu")
        print("今勉強します")
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
    elif choice == "2":
        time.sleep(1)
        print("J'ai faim.")
    elif choice == "3":
        time.sleep(1)
        print("J'étudie")
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
    elif choice == "2":
        time.sleep(1)
        print("Ich habe Hunger")
    elif choice == "3":
        time.sleep(1)
        print("Ich studiere")
    else:
        print("Try again. Enter a valid number.")
        sentence_german()


def main():
    translate = ""
    END = "quit"
    while translate != END:
        print("1) Japanese")
        print("2) French")
        print("3) German")
        print("4) Quit")
        choice = input("What language?: ")
        if choice == "1":
            sentence_japanese()
            print("\n")
        elif choice == "2":
            sentence_french()
            print("\n")
        elif choice == "3":
            sentence_german()
            print("\n")
        elif choice == "4":
            print("Quitting program...")
            translate = "quit"
        else:
            print("Please enter a number from 1-4 and try again.")
            print("\n")
main()