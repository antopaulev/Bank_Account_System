class Account:
    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0 :
            self.__balance += amount
            print("deposit Sucessfully")
        else:
            print("invalid ammount option")
    
    def withdraw(self,amount):
        if amount <= 0:
            print("Invalid Amount ")

        elif amount > self.__balance:
            print("Incufficent balance")

        else:
            self.__balance -= amount
            print("Amount withdraw succesfully")

    def check_balance(self):
        return self.__balance
