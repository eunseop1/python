from datetime import datetime

class Account:
    account_num_cont = 10000

    def __init__(self, owner, password, balance=0):
        self.account_number = Account.account_num_cont
        Account.account_num_cont += 1
        self.owner = owner
        self.balance = balance
        self.password = password
        self.history = []

    def check_password(self, input_password):
        return self.password == input_password

    def deposit(self, amount, password):
        if self.check_password(password):
            self.balance += amount
            self.history.append(f'거래 시간: {datetime.now()}, 입금: {amount}, 잔액: {self.balance}')
            print(f'{amount}원이 입금되었습니다. 현재 잔액: {self.balance}')
        else:
            print('계좌 비밀번호를 확인해 주세요')

    def withdraw(self, amount, password):
        if self.check_password(password):
            if self.balance < amount:
                print('잔액이 부족합니다')
            else:
                self.balance -= amount
                self.history.append(f'거래 시간: {datetime.now()}, 출금: {amount}, 잔액: {self.balance}')
                print(f'{amount}원이 출금되었습니다. 현재 잔액: {self.balance}')
        else:
            print('계좌 비밀번호를 확인해 주세요')

    def account_transfer(self, amount, password, recipient):
        if self.check_password(password):
            if self.balance < amount:
                print('잔액이 부족합니다')
            else:
                self.balance -= amount
                recipient.balance += amount
                self.history.append(f'거래 시간: {datetime.now()}, 이체 출금: {amount}, 잔액: {self.balance}')
                recipient.history.append(f'거래 시간: {datetime.now()}, 이체 입금: {amount}, 잔액: {self.balance}')
                print(f'{amount}원이 {self.owner}님 계좌에서 {recipient.owner}님 계좌로 이체되었습니다. 현재 잔액: {self.balance}')
        else:
            print('계좌 비밀번호를 확인해 주세요')


    def display_balance(self, password):
        if self.check_password(password):
            print(f'{self.owner}님의 계좌 잔액은 {self.balance}원 입니다')
        else:
            print('계좌 비밀번호를 확인해 주세요')
    
    def account_history(self, password):
        if self.check_password(password):
            print(f'{self.owner}님의 거래 내역:')
            print('\n'.join(self.history))
        else:
            print('계좌 비밀번호를 확인해 주세요')

class User:
    def __init__(self, name):
        self.name = name
        self.accounts = []
    
    def add_account(self, account): # Account 객체를 리스트에 추가
        self.accounts.append(account)
    
    # def get_account_num(self, account_number): 
    #     for account in self.accounts:
    #         if account.account_number == account_number:
    #             return account
    #     return None

    # def get_account_num_password(self, account_number, password):
    #     for account in self.accounts:
    #         if account.account_number == account_number and account.check_password(password):
    #             return account
    #     return None

    # def account_num_transfer(self, from_transfer, to_transfer, amount, password):
    #     from_account = self.get_account_num_password(from_transfer, password)
    #     if from_account is None:
    #         print('계좌 번호와 비밀번호를 확인해 주세요')
    #         return
    #     to_account = self.get_account_num(to_transfer)
    #     if to_account:
    #         from_account.account_transfer(amount, password, to_account)
    #     else:
    #         print('수신 계좌 번호를 확인해 주세요')

    def list_accounts(self):
        print(f'{self.name}님이 소유한 계좌 목록:')
        for index in range(len(self.accounts)):
            print(f'계좌 {index+1}, 계좌 번호 {self.accounts[index].account_number} {self.accounts[index].owner}, 잔액: {self.accounts[index].balance}')

class Bank:
    def __init__(self):
        self.users = []
    
    def add_user(self, user): # User 객체를 리스트에 추가
        self.users.append(user)

    def get_account_num_password(self, account_number, password):
        for user in self.users:
            for account in user.accounts:
                if account.account_number == account_number and account.check_password(password):
                    return account
        return None

    def get_account_num(self, account_number):
        for user in self.users:
            for account in user.accounts:
                if account.account_number == account_number:
                    return account
        return None

    def transfer_between_accounts(self, from_transfer, to_transfer, amount, password):
        from_account = self.get_account_num_password(from_transfer, password)
        if from_account is None:
            print('계좌 번호와 비밀번호를 확인해 주세요')
            return
        to_account = self.get_account_num(to_transfer)
        if to_account:
            from_account.account_transfer(amount, password, to_account)
        else:
            print('수신 계좌 번호를 확인해 주세요')
