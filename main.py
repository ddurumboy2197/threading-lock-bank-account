import threading

class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance
        self.lock = threading.Lock()

    def deposit(self, amount):
        with self.lock:
            self.balance += amount

    def withdraw(self, amount):
        with self.lock:
            if self.balance >= amount:
                self.balance -= amount
            else:
                raise ValueError("Insufficient balance")

    def get_balance(self):
        with self.lock:
            return self.balance

class Bank:
    def __init__(self):
        self.accounts = {}

    def create_account(self, account_number, initial_balance=0):
        self.accounts[account_number] = BankAccount(initial_balance)

    def deposit(self, account_number, amount):
        if account_number in self.accounts:
            self.accounts[account_number].deposit(amount)
        else:
            raise ValueError("Account not found")

    def withdraw(self, account_number, amount):
        if account_number in self.accounts:
            self.accounts[account_number].withdraw(amount)
        else:
            raise ValueError("Account not found")

    def get_balance(self, account_number):
        if account_number in self.accounts:
            return self.accounts[account_number].get_balance()
        else:
            raise ValueError("Account not found")

# Test
bank = Bank()
bank.create_account("12345", 1000)

def transfer(amount):
    bank.deposit("12345", amount)
    bank.withdraw("12345", amount)

threads = []
for i in range(10):
    thread = threading.Thread(target=transfer, args=(100,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print(bank.get_balance("12345"))  # 1000
```

Kodda `BankAccount` klassi bank hisobini ifodalaydi, u `threading.Lock` yordamida thread-safe bo'lishi uchun `deposit`, `withdraw` va `get_balance` metodlarida `with self.lock:` bloki ishlatiladi. `Bank` klassi bankni ifodalaydi, u hisoblar ro'yxatini saqlaydi va `create_account`, `deposit`, `withdraw` va `get_balance` metodlariga ega. Test qismida 10 ta thread yaratiladi, ular har birining hisobga 100 so'm o'tkazadi. Natijada hisobda 1000 so'm qoladi.
