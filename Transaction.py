
class Transaction:
    def __init__(self, transaction_type, sender_bank, receiver_bank, amount, sender_account, receiver_account=None):

        self.transaction_type = transaction_type  # 'deposit', 'withdraw', or 'transfer'
        self.sender_bank = sender_bank
        self.receiver_bank = receiver_bank
        self.amount = amount
        self.sender_account = sender_account
        self.receiver_account = receiver_account