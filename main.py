import json

coin = []

def coin_checker():
    run = True
    while run:
        print("Welcome to coin checker, Sudhakar!")
        unknown_coin = input("Please enter the coin you would like to check. Enter it in all caps: ")

        file = open('quarter-list.rtf')
        if(unknown_coin.upper() not in file.read()):
            coin.append(unknown_coin.upper())

            f = open('quarter-list.rtf', 'a')
            f.write(json.dumps(coin, indent = 2))
            f.close()
            print(unknown_coin.upper() + " has been added to your list!")
            coin.clear()

            run_again = input("Would you like to check another coin? Enter y/n: ")
            if run_again.upper() != "Y":
                run = False
        else:
            print(unknown_coin + " is already in your list!")
            run_again = input("Would you like to check another coin? Enter y/n: ")
            if run_again.upper() != "Y":
                run = False

if __name__ == "__main__":
    coin_checker()

# hello world