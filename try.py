import sqlite3

db = sqlite3.connect('./data bases/banks_data_base.db')
sql = db.cursor()
sql.execute('''
CREATE TABLE IF NOT EXISTS banks (
BIC text,
Bank_name text,
Bank_reg_number text,
Filial_reg_number text           
)
''')
db.commit()
sql.execute("""INSERT INTO banks VALUES 
('044111111', 'Филиал Некого Банка в г.Ростове-на-Дону', '9999', '0001'), 
('044222222', 'Филиал Некого Банка в г.Москве', '9999', '0002'),
('044333333', 'Филиал Некого Банка в г.Санкт-Петербурге', '9999', '0003'),
('044444444', 'Филиал Некого Банка в г.Воронеже', '9999', '0004'),
('044555555', 'Филиал Некого Банка в г.Чебоксары', '9999', '0005'),
('044666666', 'Филиал Некого Банка в г.Нижнем  Новогороде', '9999', '0006')
""")
db.commit()
sql.execute('''
CREATE TABLE IF NOT EXISTS clients (
name text,
INN text,
KPP text,
OGRN text,
Date_of_reg DATE,
Subject_of_RF text,
City text,
Street text,
House_number integer           
)
''')
db.commit()
sql.execute("""INSERT INTO clients VALUES 
('ООО "Рога и копыта"', '1111111111', '111111111', '1111111111111', '2000-01-01', 'Ростовская область', 'Ростов-на-Дону', 'Некая', 1),
('ЗАО "Копыта и рога"', '2222222222', '222222222', '2222222222222', '2001-02-02', 'Ростовская область', 'Азов', 'Другая', 2),
('ПАО "Рог у копыта"', '3333333333', '333333333', '3333333333333', '2002-03-03', 'Ростовская область', 'Каменск-Шахтинск', 'Непонятная', 3),
('ГУП "Копыта без рогов"', '4444444444', '333333333', '4444444444444', '2003-04-04', 'Ростовская область', 'Шахты', 'Тасамая', 4)
""")
db.commit()
sql.execute('''
CREATE TABLE IF NOT EXISTS accounts (
INN text,
Account_number text,
Account_currency text          
)
''')
db.commit()
sql.execute("""INSERT INTO accounts VALUES 
('1111111111', '40702810000000000001', '643'), 
('1111111111', '40702840000000000001', '840'), 
('1111111111', '40702978000000000001', '978'), 
('2222222222', '40702810000000000002', '643'), 
('2222222222', '40702156000000000002', '156'), 
('3333333333', '40702810000000000003', '643'), 
('3333333333', '40702840000000000003', '840'), 
('3333333333', '40702398000000000003', '398'), 
('4444444444', '40702810000000000004', '398')
""")
db.commit()
sql.execute('''
CREATE TABLE IF NOT EXISTS counterparty (
Counter_name text,
Counter_country_code text,
Counter_Bank_Name text,
Counter_Bank_country_code text       
)
''')
db.commit()
sql.execute("""INSERT INTO counterparty VALUES 
('Внешбелорг', '112', 'Белторгбанк', '112'), 
('China some org', '156', 'Bank of China', '156'), 
('Казахорг', '398', 'Казкомбанк', '398'), 
('Узбеквнешторг', '860', 'Узбекбанк', '860')
""")
db.commit()
sql.execute('''
CREATE TABLE IF NOT EXISTS country_code_dir (
country_code text,
country_name text       
)
''')
db.commit()
sql.execute("""INSERT INTO country_code_dir VALUES 
('112', 'Республика Белорусь'), 
('156', 'Китай'),
('398', 'Казахстан'), 
('643', 'Росиийская Федерация'), 
('860', 'Узбекистан')      
""")
db.commit()
sql.execute('''
CREATE TABLE IF NOT EXISTS val_code_dir (
val_code text,
val_name text       
)
''')
db.commit()
sql.execute("""INSERT INTO val_code_dir VALUES 
('112', 'Белорусский рубль'), 
('156', 'Китайский юань'),
('398', 'Казахский тенге'), 
('643', 'Рубль РФ'), 
('860', 'Узбекский сом')      
""")
db.commit()
sql.execute('''
CREATE TABLE IF NOT EXISTS unic_contr_numb (
ucn_numb text,
ucn_date,
INN text,
Counter_name text,
Contract_number text,
contract_date DATE,
val_code text,
sum_of_contract INTEGER,
date_of_issue_of_contract DATE      
)
''')
db.commit()
sql.execute("""INSERT INTO unic_contr_numb VALUES 
('24010001/9999/0001/2/1', '2024-01-01','1111111111', 'Внешбелорг', '1-A', '2023-12-12', '643', '1000000', '2025-12-31')
""")
db.commit()
db.close()
