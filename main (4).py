import psutil  # For memory usage monitoring

class ATM:
    def __init__(self, balance):
        self.balance = balance

    def check_balance(self):
        return self.balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return amount
        else:
            return "Insufficient funds"

def detect_malware():
    # Check for abnormal memory usage (this is a simplistic approach)
    mem_threshold = 80  # Adjust as needed
    mem_percent = psutil.virtual_memory().percent
    if mem_percent > mem_threshold:
        return True
    else:
        return False

def main():
    balance = 1000  # Starting balance
    atm = ATM(balance)

    while True:
        print("\nATM Menu:")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            print("Current Balance:", atm.check_balance())
        elif choice == "2":
            amount = float(input("Enter amount to deposit: "))
            print("New Balance:", atm.deposit(amount))
        elif choice == "3":
            amount = float(input("Enter amount to withdraw: "))
            result = atm.withdraw(amount)
            if isinstance(result, str):
                print(result)
            else:
                print("Withdrawn:", result)
                print("New Balance:", atm.check_balance())
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please choose again.")

        if detect_malware():
            print("WARNING: Potential malware detected! Terminating ATM...")
            break

if __name__ == "__main__":
    main()
