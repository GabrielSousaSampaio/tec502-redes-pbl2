class SharadAccount:

    def __init__(self, accountnumber, name1, name2, cpf1, cpf2, user, password):

        self.account_type = 'conjunta'
        self.account_number = accountnumber
        self.name = [name1, name2]
        self.cpf = [cpf1, cpf2]
        self.user = user
        self.password = password
        self.balance = 0.0

    def get_info(self):

        return {

            "accountType": self.account_type,
            "accountNumber": self.account_number,
            "name": self.name,
            "cpf": self.cpf,
            "user": self.user,
            "password": self.password,
            "balance": self.balance


        }

    def update_balance(self, amount):
        self.balance += amount