import sqlite3

class db():
    
    BANK_COLUMNS_LIST = ("""id INTEGER PRIMARY KEY AUTOINCREMENT, BIC TEXT, Bank_name TEXT, 
    Bank_reg_number TEXT, Filial_reg_number TEXT""")
    CLIENTS_COLUMNS_LIST = ('''id INTEGER PRIMARY KEY AUTOINCREMENT, Client_name TEXT,
    INN TEXT, KPP TEXT, OGRN TEXT, Date_of_reg DATE, Subject_of_RF TEXT, City TEXT,
    Street TEXT, House_number INTEGER, Bank_id INTEGER NOT NULL, FOREIGN KEY (Bank_id) REFERENCES banks(id)''')
    ACCOUNTS_COLUMNS_LIST = ("""id INTEGER PRIMARY KEY AUTOINCREMENT, Account_number TEXT,
    Client_id INTEGER NOT NULL, Val_code_id INTEGER NOT NULL, FOREIGN KEY (Client_id) REFERENCES clients(id),
    FOREIGN KEY (Val_code_id) REFERENCES val_code(id)""")
    COUNTER_PARTY_COLUMNS_LIST = ("""id INTEGER PRIMARY KEY AUTOINCREMENT, Counter_name TEXT,
    Client_id INTEGER NOT NULL, Country_code_id INTEGER NOT NULL, FOREIGN KEY (Client_id) REFERENCES clients(id),
    FOREIGN KEY (Country_code_id) REFERENCES country_code(id)""")
    COUNTER_PARTY_BANK_COLUMNS_LIST = ("""id INTEGER PRIMARY KEY AUTOINCREMENT, Counter_Bank_Name TEXT,          
    Counter_party_id INTEGER NOT NULL, Country_code_id INTEGER NOT NULL, FOREIGN KEY (counter_party_id) REFERENCES counter_party(id),
    FOREIGN KEY (Country_code_id) REFERENCES country_code(id)""")
    COUNTRY_CODE_COLUMNS_LIST = ("""id INTEGER PRIMARY KEY AUTOINCREMENT, Country_code TEXT, Country_name TEXT""")
    VAL_CODE_COLUMNS_LIST = ("""id INTEGER PRIMARY KEY AUTOINCREMENT, Val_code TEXT, Val_name TEXT""")
    UNIC_CONTR_NUMB_COLUMNS_LIST = ("""id INTEGER PRIMARY KEY AUTOINCREMENT, UCN_numb TEXT,
    UCN_date DATE, Contract_number TEXT, Contract_date DATE, Sum_of_contract INTEGER,
    Date_of_issue_of_contract DATE, Client_id INTEGER NOT NULL, Counter_party_id INTEGER NOT NULL,
    Val_code_id INTEGER NOT NULL, FOREIGN KEY (Client_id) REFERENCES clients(id),            
    FOREIGN KEY (Counter_party_id) REFERENCES counter_party(id), FOREIGN KEY (Val_code_id) REFERENCES val_code(id)""")
    PAYMENTS_COLUMNS_LIST = ("""id INTEGER PRIMARY KEY AUTOINCREMENT, Payment_date DATE, Payment_sign INTEGER,
    VO_code TEXT, Payment_sum INTEGER, Expected_time DATE, UCN_id INTEGER NOT NULL, Val_code_id INTEGER NOT NULL,          
    FOREIGN KEY (UCN_id) REFERENCES unic_contr_numb(id), FOREIGN KEY (Val_code_id) REFERENCES val_code(id)""")
    SUPP_DOC_COLUMNS_LIST = ("""id INTEGER PRIMARY KEY AUTOINCREMENT, Supp_doc_numb TEXT, Supp_doc_date DATE,
    Supp_doc_code TEXT, Supp_doc_sum INTEGER, Sum_2_or_1_sign INTEGER, Delivery_sign TEXT, Expected_time DATE,               
    UCN_id INTEGER NOT NULL, Val_code_id INTEGER NOT NULL, FOREIGN KEY (ucn_id) REFERENCES unic_contr_numb(id), 
    FOREIGN KEY (Val_code_id) REFERENCES val_code(id)""")

    def __init__(self, path: str):
        self.db = sqlite3.connect(path)
        self.sql = self.db.cursor()

    def table_create(self, table_name: str, columns_names: str):
        self.sql.execute(f'''CREATE TABLE IF NOT EXISTS {table_name} ({columns_names})''')
        self.db.commit()

    def all_table_crate(self):
        self.table_create('banks', self.BANK_COLUMNS_LIST)
        self.table_create('clients', self.CLIENTS_COLUMNS_LIST)
        self.table_create('accounts', self.ACCOUNTS_COLUMNS_LIST)
        self.table_create('counter_party', self.COUNTER_PARTY_COLUMNS_LIST)
        self.table_create('counter_party_bank', self.COUNTER_PARTY_BANK_COLUMNS_LIST)
        self.table_create('country_code', self.COUNTRY_CODE_COLUMNS_LIST)
        self.table_create('val_code', self.VAL_CODE_COLUMNS_LIST)
        self.table_create('unic_contr_numb', self.UNIC_CONTR_NUMB_COLUMNS_LIST)
        self.table_create('payments', self.PAYMENTS_COLUMNS_LIST)
        self.table_create('supp_doc', self.SUPP_DOC_COLUMNS_LIST)

    def columns_names(self, name):
        self.sql.execute(f'PRAGMA table_info({name})')
        columns_names = ', '.join([i[1] for i in self.sql.fetchall()])
        return columns_names[4:]
    
    def add_values(self, table_name, values):
        self.sql.execute(f"""INSERT INTO {table_name} ({self.columns_names(table_name)}) VALUES {values}""")
        self.db.commit()

    
data_base = db('./data bases/banks_data_base.db')
data_base.all_table_crate()















