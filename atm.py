from card import Card


def options():
    print("~~~~~~Wellcome~~~~~~")
    print("pless enter the number of the operation you want to do:")
    print('1- Deposit')
    print('2- Withdraw')
    print('3- show Balance')
    print('4- Exit')


def deposit(card):
    try:
        deposit_amount = float(input("How much would you like to deposit: "))
        card.set_total(card.get_total() + deposit_amount)
        
        print(f"operation done succsesfule and your new palance: $ {card.get_total()}")
    except:
        print("Invalid input !")

def withdraw(card):
    try:
        withdraw_amount = float(input("How much would you like to withdraw: "))
        if withdraw_amount < card.get_total():
            card.set_total(card.get_total() - withdraw_amount)
            print(f"operation done succsesfule and your new palance: $ {card.get_total()}")
        else:
            print("sorry insufficient balance :(")
    except:
        print("invalid operation!")

def show_balance(card):
    print(f"your balance is: $ {card.get_total()}")


if __name__ == '__main__':
    user = Card("", "", "")

    l = []

    l.append(Card(12545648, 5555, 1000))
    l.append(Card(12544144, 4444, 6000))
    l.append(Card(12554211, 8888, 5000))

    num = ''
    while True:
        try:
            num = int(input("pless enter your card number: ").strip())

            card_match = [i for i in l if i.number == num]
            if card_match:
                user = card_match[0]
                break
            else:
                print("invalid card number pless try again!")
        except:
            print("invalid card number pless try again")

    while True:
        try:
            pin = int(input("pless enter your pin number: ").strip())
            if user.pin == pin:
                options()
                option = int(input("enter the number of the operation: ").strip())
                if option == 1:
                    deposit(user)
                elif option == 2:
                    withdraw(user)
                elif option == 3:
                    show_balance(user)
                elif option == 4:
                    break
                else:
                    print("pless enter a valid number!!!")
            else:
                print('invalid pin pless try again!')
        except:
            print('invalid pin pless try again')