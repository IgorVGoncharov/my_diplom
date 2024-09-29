import sqlite3
from constants import *

class db():
    
    def __init__(self, path: str):
        self.db = sqlite3.connect(path)
        self.sql = self.db.cursor()

    def table_create(self, table_name: str, columns_names: str):
        self.sql.execute(f'''CREATE TABLE IF NOT EXISTS {table_name} ({columns_names})''')
        self.db.commit()

    def all_table_crate(self):
        self.table_create('banks', BANK_COLUMNS_LIST)
        self.table_create('clients', CLIENTS_COLUMNS_LIST)
        self.table_create('accounts', ACCOUNTS_COLUMNS_LIST)
        self.table_create('counter_party', COUNTER_PARTY_COLUMNS_LIST)
        self.table_create('counter_party_bank', COUNTER_PARTY_BANK_COLUMNS_LIST)
        self.table_create('country_code', COUNTRY_CODE_COLUMNS_LIST)
        self.table_create('val_code', VAL_CODE_COLUMNS_LIST)
        self.table_create('unic_contr_numb', UNIC_CONTR_NUMB_COLUMNS_LIST)
        self.table_create('payments', PAYMENTS_COLUMNS_LIST)
        self.table_create('supp_doc', SUPP_DOC_COLUMNS_LIST)

    def columns_names(self, name):
        self.sql.execute(f'PRAGMA table_info({name})')
        columns_names = ', '.join([i[1] for i in self.sql.fetchall()])
        return columns_names[:-4]
    
    def add_values(self, table_name, values):
        self.sql.execute(f"""INSERT INTO {table_name} ({self.columns_names(table_name)}) VALUES {values}""")
        self.db.commit()

    def select_from_db_all(self, table_name):
        self.sql.execute(f"SELECT * FROM {table_name} WHERE id != '$id'")
        self.db.commit()
        return self.sql.fetchall()
    
    def select_from_db_choiced(self, request, row_number):
        self.sql.execute(request + f'{row_number}')
        self.db.commit()
        return self.sql.fetchall()
    
data_base = db('./data bases/banks_data_base.db')
data_base.all_table_crate()
banks = data_base.select_from_db_all('banks')
clients = data_base.select_from_db_all('clients')


