class BankAccount:
    def __init__(self,name,mobile_no,account_no):
        self.name=name
        self.mobile_number=mobile_no
        self.account=account_no
        self.balance=0
    def generate_account_no(self):
        import uuid
        self.account_no=str(uuid.uuid4())
    def deposit(self,amount):
        self.balance+=amount
    def wwithdraw(self,amount):
        self.balance-=amount