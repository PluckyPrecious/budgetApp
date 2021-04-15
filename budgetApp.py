class Budget:

    Budget_balance = [0, 0, 0]
    Budgets = ["Food", "Clothing", "Subscriptions"]

    def __init__(self, category):
        self.category = category - 1

    def actions(self):
        print("What Would You Like to Do? \n")
        print(f"Press 1 to Deposit fund to {self.Budgets[self.category]} Budget")
        print(f"Press 2 to Withdraw fund from {self.Budgets[self.category]} Budget")
        print(f"Press 3 to Check balance of {self.Budgets[self.category]} Budget")
        print("Press 4 to Trasfer balance between Budget")
        print(f"Press 5 to exit {self.Budgets[self.category]} Budget")

        action = input(": ")

        if (action == "1"):
            self.deposit()

        elif(action == "2"):
            self.withdraw()

        elif(action == "3"):
            self.balance()

        elif(action == "4"):
            self.transfer()

        elif(action == "5"):
            self.out()

        else:
            print("Invalid input")
            pass

    def deposit(self):
        try:
            amount = int(input("Enter amount to deposit: \n"))
            print("You are doing well")
            self.Budget_balance[self.category] += amount
            print("Deposit Sucessful!")

        except ValueError as verr:
            print(f"Error: {verr}")
            print("Deposit failed")

    def withdraw(self):
        try:
            amount = int(input("Enter amount to withdraw: \n"))
            print("Permission granted to spend without guilt or regret")
            if(self.Budget_balance[self.category] != 0 or amount < self.Budget_balance[self.category]):
                self.Budget_balance[self.category] -= amount
                print("Withdrawal Complete!")

            else:
                print("Insufficient Funds!")

        except ValueError as verr:
            print(f"Error: {verr}")
            print("Withdrawal failed")

    def balance(self):
        print(
            f"You have {self.Budget_balance[self.category]} in your {self.Budgets[self.category]} Budget")
        print("Express your values and aspirationns, budget it!")
        pass

    def transfer(self):
        try:
            print("Choose budget to transfer to: ")
            print("1. Food")
            print("2. Clothing")
            print("3. Subscriptions")
            selection = int(input(": "))

            if(selection <= 3):
                selection -= 1

                amount = int(input("Enter amount to transfer: \n"))

                if(selection == self.category):
                    print("Same account selected")
                    print("Transfer failed!")

                elif(self.Budget_balance[selection] != 0 or amount < self.Budget_balance[selection]):
                    print("One rule: Do not go over budget")
                    self.Budget_balance[selection] -= amount
                    self.Budget_balance[(self.category - 1)] += amount

                    print("Transfer Complete!")

                else:
                    print("Insufficient Funds!")

            else:
                print("Invalid input")

        except ValueError as verr:
            print(f"Error: {verr}")
            print("Transaction failed")
        except IndexError as ierr:
            print(f"Error: {ierr}")
            print("Transaction failed")
        except:
            print("Error occured!")

    def out(self):
        try:
            pick = int(
                input("Are you sure you want to quit?\nPress 1 to quit\nPress 2 to continue\n"))
        except:
            print("Invalid input\n")
            quit()

        if(pick == 1):
            print("\nDon't wonder where your money went, budget it!.")
        quit()
        if(pick == 2):
            self.category()
        else:
            print('Invalid input\n')
        quit()


def init():
    print("Hello! Welcome to myPluckyBudget.")
    print("What do You Wish to Budget?:")
    print("1. Food")
    print("2. Clothing")
    print("3. Subscriptions")

    selection = input(": ")

    if (selection == "1"):
        budget = Budget(1)
        budget.actions()
    elif(selection == "2"):
        budget = Budget(2)
        budget.actions()
    elif(selection == "3"):
        budget = Budget(3)
        budget.actions()
    else:
        print("Invalid input")

    retry = input("Would you like to try again? Y/N: ")

    if (retry == "Y" or retry == "Yes" or retry == "y" or retry == "yes"):
        init()
    else:
        print("Well Done!")


init()
