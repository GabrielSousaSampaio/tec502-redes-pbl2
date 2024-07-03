
class JuridicPerson:

    def __init__(self, accountnumber, name, cnpj, user, password):

        self.account_type = 'juridica'
        self.account_number = accountnumber
        self.name = name
        self.cnpj = cnpj
        self.user = user
        self.password = password
        self.balance = 0.0

    def get_info(self):

        return {

            "accountType": self.account_type,
            "accountNumber": self.account_number,
            "name": self.name,
            "cnpj": self.cnpj,
            "user": self.user,
            "password": self.password,
            "balance": self.balance


        }

    def update_balance(self, amount):
        self.balance += amount