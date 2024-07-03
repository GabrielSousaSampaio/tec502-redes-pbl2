class FisicPerson:

    def __init__(self, accountnumber, name, cpf, user, password):

        self.account_type = 'fisica'
        self.account_number = accountnumber
        self.name = name
        self.cpf = cpf
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