ACCOUNTS_REQUEST = f"""SELECT A.Account_number, V.Val_code, V.Val_name 
FROM accounts AS A, val_code AS V 
WHERE A.Val_code_id = V.id AND A.Client_id = """

PARTNERS_REQUEST = f"""SELECT СP.Counter_name, CC.Country_code, CC.Country_name 
FROM counter_party AS СP, country_code AS CC 
WHERE СP.Country_code_id = CC.id AND СP.Client_id = """

PARTNERS_BANKS_REQUEST = f"""SELECT СPB.Counter_Bank_Name, CC.Country_code, CC.Country_name 
FROM counter_party_bank AS СPB, country_code AS CC 
WHERE СPB.Country_code_id = CC.id AND СPB.Client_id = """

UNIC_CONTR_NUMB_REQUEST = f"""SELECT U.UCN_numb, U.UCN_date, U.Contract_number,
U.Contract_date, U.Sum_of_contract, V.Val_code, V.Val_name, U.Date_of_issue_of_contract,
C.Counter_name
FROM unic_contr_numb AS U, counter_party AS C, val_code AS V
WHERE U.Val_code_id = V.id AND U.Counter_party_id = C.id AND U.Client_id = """

PAYMENT_REQUEST = f"""SELECT U.UCN_numb,
P.Payment_date, P.Payment_sign, P.VO_code, P.Payment_sum,
V.Val_code, V.Val_name, P.Expected_time
FROM unic_contr_numb AS U, payments AS P, val_code AS V
WHERE P.UCN_id = U.id AND P.Val_code_id = V.id AND P.Client_id = """

SUPP_DOC_REQUEST = f"""SELECT U.UCN_numb,
S.Supp_doc_numb, S.Supp_doc_date, S.Supp_doc_code,
S.Supp_doc_sum, V.Val_code, V.Val_name, S.Sum_2_or_1_sign,
S.Delivery_sign, S.Expected_time
FROM unic_contr_numb AS U, supp_doc AS S, val_code AS V
WHERE S.UCN_id = U.id AND S.Val_code_id = V.id AND S.Client_id = """



"""Наименование столбцов талиц приложения"""
BANK_HEADERS_LABELS = ['БИК', 'Наименование Банка', 'Рег.номер Банка', 'Рег.номер Филиала']
CLIENTS_HEADERS_LABELS = ['Наименование клиента', 'ИНН', 'КПП', 'ОГРН', 'Дата регистрации', 
    'Субъект РФ', 'Город', 'Улица', 'Номер дома']
ACCOUNTS_HEADERS_LABELS = ['Номер счета', 'Код валюты счета', 'Валюта счета']
COUNTERS_HEADERS_LABELS = ['Наименование контрагента', 'Код страны контрагента', 'Страна контрагента']
COUNTERS_BANKS_HEADERS_LABELS = ['Наименование Банка контрагента', 'Код страны Банка контрагента', 'Страна Банка контрагента']
UNIC_CONTR_NUMB_LABELS = ['Уникальный номер контракта (УНК)', 'Дата УНК', 'Номер контракта',
'Дата контракта', 'Сумма контракта', 'Код валюты контракта', 'Валюта контракта', 
'Срок действия контракта', 'Наименование контрагента']
PAYMENTS_LABELS = ['Номер УНК', 'Дата платежа', 'Признак платежа', 'Код ВО',
'Сумма платежа', 'Код валюты платежа', 'Валюта платежа', 'Ожидаемый срок']
SUPP_DOC_LABELS = ['Номер УНК', 'Номер ПД', 'Дата ПД', 'Код ПД',
'Сумма ПД', 'Код валюты платежа', 'Валюта платежа','Сумма ПД по признаку 2 или 1' 'Признак платежа',
'Ожидаемый срок']


"""Наименование граф таблиц базы данных"""
BANK_COLUMNS_LIST = ("""BIC TEXT, Bank_name TEXT, Bank_reg_number TEXT, Filial_reg_number TEXT, 
id INTEGER PRIMARY KEY AUTOINCREMENT""")
CLIENTS_COLUMNS_LIST = ('''Client_name TEXT, INN TEXT, KPP TEXT, OGRN TEXT, Date_of_reg DATE, 
Subject_of_RF TEXT, City TEXT, Street TEXT, House_number INTEGER, Bank_id INTEGER NOT NULL, 
id INTEGER PRIMARY KEY AUTOINCREMENT, FOREIGN KEY (Bank_id) REFERENCES banks(id)''')
ACCOUNTS_COLUMNS_LIST = ("""Account_number TEXT,
Client_id INTEGER NOT NULL, Val_code_id INTEGER NOT NULL, id INTEGER PRIMARY KEY AUTOINCREMENT, FOREIGN KEY (Client_id) REFERENCES clients(id),
FOREIGN KEY (Val_code_id) REFERENCES val_code(id)""")
COUNTER_PARTY_COLUMNS_LIST = ("""Counter_name TEXT,
Client_id INTEGER NOT NULL, Country_code_id INTEGER NOT NULL, id INTEGER PRIMARY KEY AUTOINCREMENT, FOREIGN KEY (Client_id) REFERENCES clients(id),
FOREIGN KEY (Country_code_id) REFERENCES country_code(id)""")
COUNTER_PARTY_BANK_COLUMNS_LIST = ("""Counter_Bank_Name TEXT,          
Counter_party_id INTEGER NOT NULL, Country_code_id INTEGER NOT NULL, Client_id INTEGER NOT NULL, id INTEGER PRIMARY KEY AUTOINCREMENT, FOREIGN KEY (counter_party_id) REFERENCES counter_party(id),
FOREIGN KEY (Country_code_id) REFERENCES country_code(id)""")
COUNTRY_CODE_COLUMNS_LIST = ("""Country_code TEXT, Country_name TEXT, id INTEGER PRIMARY KEY AUTOINCREMENT""")
VAL_CODE_COLUMNS_LIST = ("""Val_code TEXT, Val_name TEXT, id INTEGER PRIMARY KEY AUTOINCREMENT""")
UNIC_CONTR_NUMB_COLUMNS_LIST = ("""UCN_numb TEXT,
UCN_date DATE, Contract_number TEXT, Contract_date DATE, Sum_of_contract INTEGER,
Date_of_issue_of_contract DATE, Client_id INTEGER NOT NULL, Counter_party_id INTEGER NOT NULL,
Val_code_id INTEGER NOT NULL, id INTEGER PRIMARY KEY AUTOINCREMENT, FOREIGN KEY (Client_id) REFERENCES clients(id),            
FOREIGN KEY (Counter_party_id) REFERENCES counter_party(id), FOREIGN KEY (Val_code_id) REFERENCES val_code(id)""")
PAYMENTS_COLUMNS_LIST = ("""Payment_date DATE, Payment_sign INTEGER,
VO_code TEXT, Payment_sum INTEGER, Expected_time DATE, UCN_id INTEGER NOT NULL, Val_code_id INTEGER NOT NULL, 
Client_id INTEGER NOT NULL, id INTEGER PRIMARY KEY AUTOINCREMENT,         
FOREIGN KEY (UCN_id) REFERENCES unic_contr_numb(id), FOREIGN KEY (Val_code_id) REFERENCES val_code(id)""")
SUPP_DOC_COLUMNS_LIST = ("""Supp_doc_numb TEXT, Supp_doc_date DATE,
Supp_doc_code TEXT, Supp_doc_sum INTEGER, Sum_2_or_1_sign INTEGER, Delivery_sign TEXT, Expected_time DATE,               
UCN_id INTEGER NOT NULL, Val_code_id INTEGER NOT NULL, Client_id INTEGER NOT NULL, id INTEGER PRIMARY KEY AUTOINCREMENT, FOREIGN KEY (ucn_id) REFERENCES unic_contr_numb(id), 
FOREIGN KEY (Val_code_id) REFERENCES val_code(id)""")