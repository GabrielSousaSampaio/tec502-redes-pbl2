from flask import Flask, jsonify
import logging
from flask_cors import CORS
from flask import *


class Bank:
    def __init__(self, bank_name, client_name, cpf, password, host, port):

        self.bank_name = bank_name
        self.balance = 0.0
        self.client_name = client_name
        self.cpf = cpf
        self.password = password
        self.host = host
        self.port = port

        self.banks = []


        self.app = Flask(__name__)
        CORS(self.app)


    @self.app.route('/create_account', methods=['POST'])
    def create_account_route(self):

        data = request.get_json()
        bank_name = data['bank_name']
        client_name = data['client_name']
        cpf = data['cpf']
        password = data['password']
        saldo_inicial = data.get('saldo_inicial', 0.0)
        success = self.create_account(bank_name, client_name, cpf, password, saldo_inicial)

        if success:
            return jsonify({'status': 'account created'}), 201
        else:
            return jsonify({'status': 'account creation failed'}), 400

    def create_account(self, bank_name, client_name, cpf, password, saldo_inicial=0.0):
        try:
            if cpf in self.contas:
                logging.error("Conta já existe para este CPF!")
                return False
            else:
                self.contas[cpf] = {
                    'saldo': saldo_inicial,
                    'password': password,
                    'client_name': client_name,
                    'bank_name': bank_name,
                    'extrato': []
                }
                logging.info(f"Conta criada com sucesso para CPF: {cpf}")
                return True
        except Exception as e:
            logging.error(f"Não foi possível criar a conta: {e}")
            return False

    @self.app.route('/deposit', methods=['POST'])
    def deposit():
        data = request.get_json()
        cpf = data['cpf']
        amount = data['amount']
        conta = self.contas.get(cpf)
        if conta:
            with self.get_lock(cpf):
                conta['saldo'] += amount
                conta['extrato'].append({'tipo': 'depósito', 'quantia': amount})
            return jsonify({'status': 'deposit successful'}), 200
        else:
            return jsonify({'error': 'account not found'}), 404

    @self.app.route('/withdraw', methods=['POST'])
    def withdraw():
        data = request.get_json()
        cpf = data['cpf']
        amount = data['amount']
        conta = self.contas.get(cpf)
        if conta:
            with self.get_lock(cpf):
                if conta['saldo'] >= amount:
                    conta['saldo'] -= amount
                    conta['extrato'].append({'tipo': 'saque', 'quantia': amount})
                    return jsonify({'status': 'withdraw successful'}), 200
                else:
                    return jsonify({'error': 'insufficient funds'}), 400
        else:
            return jsonify({'error': 'account not found'}), 404

    #def transfer

    #def get_extract

    @self.app.route('/balance/<cpf>', methods=['GET'])
    def get_balance(cpf):
        conta = self.contas.get(cpf)
        if conta:
            return jsonify({'cpf': cpf, 'saldo': conta['saldo']})
        else:
            return jsonify({'error': 'account not found'}), 404


    def get_allbanks(self):

        return self.banks

    def get_bankname(self):

        return self.bank_name

    def get_client_name(self):

        return self.client_name

    def get_cpf(self):

        return self.cpf

    def set_bankname(self, bank_name):

        self.bank_name = bank_name

    def set_client_name(self, client_name):

        self.client_name = client_name

    def set_cpf(self, cpf):

        self.cpf = cpf

