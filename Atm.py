class Atm(object):
    def __init__(self,card_number,pin_number):
        self.cardNumber=card_number
        self.pinNumber=pin_number
    
    def CashWthdrawal(self,amount):
        new_amount = 100-amount
        print("You withdrawed:" + str(amount) )
    def BalanceEnquiry(self):
        print("Your remaining balance is: $100")
    

def main():
    name = input("Hello! What s your name?")
    print("Hello!"+name)
    cardNumber=input("Enter your card number:")
    pinNumber=input("Enter your pin:")
    new_user = Atm(cardNumber,pinNumber)

    print("choose your activity:")
    print("1.CashWithDrawal")
    print("BalanceEnquiry")
    activity=int(input("Enter activty of your choice:"))

    if(activity == 1):
        amount=int(input("Enter your amount:"))
        new_user.CashWthdrawal(amount)
    elif(activity == 2):
       new_user.BalanceEnquiry()
    else:
        print("Enter a valid number")










       