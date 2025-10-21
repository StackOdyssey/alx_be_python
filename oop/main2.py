from BankAccount import BankAccount

def main():
    
    mohammed_account = BankAccount("Mohammed", 250000)
    kamal_account = BankAccount("Kamal", 300000)

    mohammed_account.deposit(5000)
    kamal_account.deposit(100000)
    mohammed_account.transfer_to(kamal_account, 250000)

    mohammed_account.check_balance()
    kamal_account.check_balance()


if __name__== '__main__':
    main()