BankAccounts = []

class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
        BankAccounts.append(owner)

    def deposit(self, amount):
        self.balance += int(amount)
        print(f"Deposite is completed: {amount}")

    def withdraw(self, amount):
        if int(amount) <= self.balance:
            self.balance -= int(amount)
            print(f"Withdraw completed: {amount}")
            print(f"Current Balance: {self.balance}")
        else:
            print("Insufficient balance!")

    def check_balance(self):
        return self.balance


def options():
    
    print("-----------------------------------")
    print("1. Create a bank account")
    print("2. Deposite money to account")
    print("3. Withdraw amount from account")
    print("4. Balance checking")
    print("5. Accounts")
    print("6. Exit")
    opt = input("Select one option from top: ")
    return opt



def main():

    while(True):
        option = int(options())

        match option:
            case 1:

                owner = input("Enter the name of the customer: ")       
                acc = BankAccount(owner)
                print("Bank account is created.")
                despo = input("If you want to deposite money initially(Y/N): ")
                match despo:
                    case "Y": 
                        despositemoney = input("Enter money for deposite: ")
                        acc.deposit(despositemoney)
                    case "N":
                        continue
            case 2:

                depos = input("Enter deposite money: ")
                acc.deposit(depos)
                
            case 3:
                
                withdraw = input("Enter withdraw money: ")
                acc.withdraw(withdraw)

            case 4: 

                balance = acc.check_balance()
                print(f"Current Balance: {balance}")

            case 5:

                print("Bank Accounts: ")
                n = 1
                for i in BankAccounts:
                    print(f"User{n}: {i}")
                    n += 1
                print("----------------------------------")
                n = 1

            case 6:

                exit()

            case _:
                print("Invalid option")


if __name__ == "__main__":
    main()