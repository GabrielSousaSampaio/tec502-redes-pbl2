from flask import Flask, request, jsonify, send_from_directory, redirect, url_for, session, render_template
from flask_cors import CORS
import threading
import time
from queue import Queue
from Transaction import Transaction
from accountTypes.FisicPerson import FisicPerson
from accountTypes.SharadAccount import SharadAccount
from accountTypes.JuridicPerson import JuridicPerson
import os

class Bank:

    def __init__(self, bank_name, host='0.0.0.0', flask_port=5001):
        self.bank_name = bank_name
        self.account_number = 1
        self.clients = []
        self.other_banks = []  # Add other bank instances here
        self.transaction_queue = Queue()

        self.host = host
        self.flask_port = flask_port
        self.app = Flask(__name__)
        self.app.secret_key = 'supersecretkey'
        CORS(self.app)
        self.setup_routes()

        # Start the token ring processing thread
        self.token = threading.Event()
        self.token.set()  # Initially, this bank has the token
        self.processing_thread = threading.Thread(target=self.process_transactions)
        self.processing_thread.start()

    def setup_routes(self):
        @self.app.route('/create_account', methods=['POST'])
        def create_account_route():
            account = request.form

            if self.checking_account(account):
                account_type = account.get('account_type')
                password = account.get('password')
                confirm_password = account.get('confirm_password')

                if password != confirm_password:
                    return jsonify({"error": "Passwords do not match"}), 400

                if account_type == 'fisica':
                    client = FisicPerson(self.account_number, account.get('client_name'), account.get('cpf'), account.get('username'),
                                         account.get('password'))

                elif account_type == 'juridica':
                    client = JuridicPerson(self.account_number, account.get('client_name'), account.get('cnpj'), account.get('username'),
                                           account.get('password'))

                elif account_type == 'conjunta':
                    client = SharadAccount(self.account_number, account.get('client_name1'), account.get('client_name2'),
                                           account.get('cpf1'), account.get('cpf2'), account.get('username'), account.get('password'))

                else:
                    return jsonify({"error": "Invalid account type"}), 400

                self.account_number += 1
                self.clients.append(client.get_info())
                print(self.clients)

                return jsonify({"message": "Account created successfully"}), 201
            else:
                return jsonify({"error": "Account already exists"}), 400

        @self.app.route('/login', methods=['POST'])
        def login():
            data = request.json
            account_type = data.get('account_type')
            username = data.get('username')
            password = data.get('password')

            for client in self.clients:
                if client['accountType'] == account_type and client['user'] == username and client[
                    'password'] == password:
                    session['logged_in'] = True
                    session['client'] = client
                    return jsonify({"success": True}), 200

            return jsonify({"success": False, "message": "Invalid credentials"}), 401

        @self.app.route('/templates/<path:filename>')
        def login_page(filename):
            return send_from_directory(os.path.join(self.app.root_path, 'templates'), filename)

        @self.app.route('/home')
        def home_page():
            if 'logged_in' in session and session['logged_in']:
                client = session['client']
                print(client)
                return render_template('home.html', bank_name=self.bank_name, client=client)
            else:
                return redirect(url_for('login_page', filename='login.html'))

        @self.app.route('/transaction', methods=['POST'])
        def transaction():
            data = request.json
            transaction = Transaction(
                transaction_type=data['transaction_type'],
                sender_bank=self,
                receiver_bank=data.get('receiver_bank', self),
                amount=data['amount'],
                sender_account=data['sender_account'],
                receiver_account=data.get('receiver_account')
            )
            self.transaction_queue.put(transaction)
            return jsonify(success=True)

    def checking_account(self, account):
        account_type = account.get('account_type')

        if account_type == 'fisica':
            for client in self.clients:
                if client["accountType"] == 'fisica':
                    if account.get('cpf') == client["cpf"]:
                        return False

        elif account_type == 'juridica':
            for client in self.clients:
                if client["accountType"] == 'juridica':
                    if account.get('cnpj') == client["cnpj"]:
                        return False

        elif account_type == 'conjunta':
            for client in self.clients:
                if client["accountType"] == 'conjunta':
                    if account.get('cpf1') in client["cpf"] or account.get('cpf2') in client["cpf"]:
                        return False
        else:
            return False

        return True

    def process_transactions(self):
        while True:
            if self.token.is_set():
                while not self.transaction_queue.empty():
                    transaction = self.transaction_queue.get()
                    self.handle_transaction(transaction)
                self.token.clear()
                self.pass_token_to_next_bank()

    def handle_transaction(self, transaction):
        if transaction.transaction_type == 'deposit':
            self.deposit(transaction)
        elif transaction.transaction_type == 'withdraw':
            self.withdraw(transaction)
        elif transaction.transaction_type == 'transfer':
            self.transfer(transaction)

    def deposit(self, transaction):
        for client in self.clients:
            if client['accountNumber'] == transaction.receiver_account:
                client['balance'] += transaction.amount
                return True
        return False

    def withdraw(self, transaction):
        for client in self.clients:
            if client['accountNumber'] == transaction.sender_account and client['balance'] >= transaction.amount:
                client['balance'] -= transaction.amount
                return True
        return False

    def transfer(self, transaction):
        total_balance = 0
        involved_accounts = []
        for client in self.clients:
            if client['accountNumber'] == transaction.sender_account and client['balance'] >= transaction.amount:
                involved_accounts.append(client)
                total_balance += client['balance']
                if total_balance >= transaction.amount:
                    break

        if total_balance < transaction.amount:
            return False

        remaining_amount = transaction.amount
        for account in involved_accounts:
            if account['balance'] >= remaining_amount:
                account['balance'] -= remaining_amount
                remaining_amount = 0
            else:
                remaining_amount -= account['balance']
                account['balance'] = 0

        for client in self.clients:
            if client['accountNumber'] == transaction.receiver_account:
                client['balance'] += transaction.amount
                return True

        return False

    def pass_token_to_next_bank(self):
        if self.other_banks:
            next_bank = self.other_banks.pop(0)
            self.other_banks.append(next_bank)
            next_bank.token.set()

def main():
    banco = Bank('Green Bank')
    banco.app.run(debug=True, port=5001)

if __name__ == '__main__':
    main()
