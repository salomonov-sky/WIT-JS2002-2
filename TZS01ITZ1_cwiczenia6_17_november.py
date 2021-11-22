class BankCard:
    def __init__(self, owner, number, provider):
        self.owner = owner
        self.number = number
        self.provider = provider

    def get_number(self):
        number = self.number
        print(number)

    def get_owner(self):
        owner = self.owner
        print(owner)

    def get_provider(self):
        provider = self.provider
        print(provider)


class BankAccount:
    def __init__(self, owner, balance, bank):
        self.owner = owner
        self.balance = balance
        self.bank = bank

    def get_owner(self):
        owner = self.owner
        print(owner)

    def get_balance(self):
        balance = self.balance
        print(balance)

    def get_bank(self):
        number = self.bank
        print(bank)

    def set_balance(self):
        print("set_balance()")


class Bank:
    def __init__(self, name, bank_accounts, bank_cards):
        self.name = name
        self.bank_accounts = bank_accounts
        self.bank_cards = bank_cards

    def get_bank_accounts(self):
        bank_accounts = self.bank_accounts
        print(bank_accounts)

    def get_bank_cards(self):
        bank_cards = self.bank_cards
        print(bank_cards)


class CreditCard(BankCard):
    def __init__(self, owner, number, provider, balance, payments_history):
        super(). __init__(number, owner, provider)
        self.balance = balance
        self.payments_history = payments_history

    def get_balance(self):
        balance = self.balance
        print(balance)

    def set_balance(self):
        print("set_balance")

    def set_balance(self):
        print("set_balance")

    def get_payments_history(self):
        payments_history = self.payments_history
        print(payments_history)


class GoldenCreditCard(CreditCard):

    def __init__(self, owner, number, provider, balance, payment_history, reward_points):
        super().__init__(owner, number, provider, balance, payment_history)
        self.reward_points = reward_points

    def get_reward_points(self):
        reward_points = self.reward_points
        print(reward_points)

    def set_reward_points(self):
        print("set_reward_points()")


class PremiumBankAccount(BankAccount):
    def __init__(self, owner, balance, bank, financial_manager):
        super(). __init__(owner, balance, bank)
        self.financial_manager = financial_manager

    #premium_bank = PremiumBankAccount("owner", "MBank", "Adm")

    def get_financial_manager(self):
        financial_manager = self.financial_manager
        print(financial_manager)

    def set_financial_manager(self):
        print("set_financial_manager()")


class StudentBankAccount(BankAccount):
    def __init__(self, owner, balance, bank, overdraft_balance, overdraft_limit):
        super(). __init__(owner, balance, bank)
        self.overdraft_balance = overdraft_balance
        self.overdraft_limit = overdraft_limit

    #student_account = StudentBankAccount("owner",1111, "MBank", 2222, 3333)

    def get_overdraft_balance(self):
        overdraft_limit = self.overdraft_limit
        print(overdraft_limit)

    def set_overdraft_balance(self):
        overdraft_limit = self.overdraft_limit
        print("set_overdraft_limit()")

    def get_overdraft_limit(self):
        overdraft_limit = self.overdraft_limit
        print(overdraft_limit)

    def set_overdraft_limit(self):
        overdraft_limit = self.overdraft_limit
        print("set_overdraft_limit()")


#

class testowa:

    bank_card = BankCard("Test", 111, "Test")
    bank_card.get_number()
    bank_card.get_owner()
    bank_card.get_provider()

    bank_account = BankAccount("Test", 3353, "Test")
    bank_account.get_owner()
    bank_account.balance
    bank_account.bank
    bank_account.set_balance()

    bank = Bank("name", 9999, 8888)
    bank.get_bank_accounts()
    bank.get_bank_cards()

    credit_card = CreditCard("owner", 5555, "provider", 7777, 0000)
    credit_card.get_balance()
    credit_card.set_balance()
    credit_card.get_payments_history()

    golden_credit_card = GoldenCreditCard(
        "owner", 545, "provider", 787, 442, 444)
    golden_credit_card.get_reward_points()
    golden_credit_card.set_reward_points()

    premium_bank_account = PremiumBankAccount("owner", 5215, "MBank", "Adm")
    premium_bank_account.get_financial_manager()
    premium_bank_account.set_financial_manager()

    student_bank_account = StudentBankAccount(
        "owner", 6507, "MBnak", 8097, 8790)
    student_bank_account.get_overdraft_balance()
    student_bank_account.set_overdraft_balance()
    student_bank_account.get_overdraft_limit()
    student_bank_account.set_overdraft_limit()
