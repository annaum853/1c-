import pymysql
from db import host, user, password, db_name

import pymysql
from db import host, user, password, db_name

try:
    connection = pymysql.connect(
        host=host,
        port=3306,
        user=user,
        password=password,
        database=db_name,
        cursorclass=pymysql.cursors.DictCursor
    )
    try:
        with connection.cursor() as cursor:
            drop_table_query = "DROP TABLE IF EXISTS coffee_drinks_sell"
            cursor.execute(drop_table_query)

            create_table_query = "CREATE TABLE if not exists coffee_drinks_sell(id int AUTO_INCREMENT," \
                                 "employee_id int," \
                                 " employee_surname varchar(30)," \
                                 "drink_name varchar(30)," \
                                 "syrop int," \
                                 "PRIMARY KEY(id));"
            cursor.execute(create_table_query)
            print('Вроде норм')

        with connection.cursor() as cursor:
            insert_query = "INSERT INTO coffee_drinks_sell(employee_id,employee_surname,drink_name,syrop) " \
                           "VALUES ('10','Наумов','latte','1');"
            cursor.execute(insert_query)
            connection.commit()
            print('Жесть я крутой')

        with connection.cursor() as cursor:
            select_table_query = "SELECT * from coffee_drinks_sell"
            cursor.execute(select_table_query)
            rows = cursor.fetchall()
            for row in rows:
                print(row)
    except Exception as ex:
        pass

except Exception as ex:
    print('nu i ladno')

emp_id = 0
surname = 0

def func():
    print('Добро пожаловать в систему')
    print('Зайти как администратор или кассир?')
    entry = input()
    if entry == 'администратор':
        print('Введите пароль администратора:')
        adm_pass = input()
        if adm_pass != 'admin':
            print('неверный пароль администратора')
            return func()
        else:
            return 0
    elif entry == 'кассир':
        print('Введите пароль кассира:')
        kass_pass = input()
        if kass_pass != 'kassir':
            print('Неверный пароль для кассира')
            return func()
        else:
            return 1
    else:
        print('нет такого пользователя')
        return func()

login = func()

if login == 0:
    print('admin')
else:
    print('kassir')
    print('Введите ваш уникальный код')
    emp_id = input()
    print('Введите вашу фамилию')
    surname = input()
a = '\''
def buy():
    if login == 1:
        print('Введите напиток который вы продали:')
        drink = input()
        print('Есть ли сироп(Да/Нет):')
        b = input()
        syrop = 0
        if b == 'Да':
            syrop = 1
        str2 = 'VALUES' + ' (' + a + str(emp_id) + a + ',' + a + str(surname) + a + ',' +a + str(drink) + a +\
               ',' + a + str(syrop) + a + ');'
        str1 = 'INSERT INTO coffee_drinks_sell(employee_id,employee_surname,drink_name,syrop) '
        connection = pymysql.connect(
            host=host,
            port=3306,
            user=user,
            password=password,
            database=db_name,
            cursorclass=pymysql.cursors.DictCursor
        )
        with connection.cursor() as cursor:
            insert_query = str1 + str2
            print(insert_query)
            cursor.execute(insert_query)
            connection.commit()
        print('Закончить смену?')
        exit_code = input()
        if exit_code == 'да':
            return 0
        return buy()
buy()

func()

x = 0
name_d = 0
issue = 0
if login == 0:
    print('вы можете посмотреть сколько напитков продали и сколько напитков продал каждый кассир')
    print('какой напиток вас интересует:')
    name_d = input()
    print('интересует ли вас конкретный кассир?')
    x = input()
    if x == 'нет':
        issue = 'SELECT * from coffee_drinks_sell where drink_name = ' + a + str(name_d) + a
        connection = pymysql.connect(
            host=host,
            port=3306,
            user=user,
            password=password,
            database=db_name,
            cursorclass=pymysql.cursors.DictCursor
        )
        with connection.cursor() as cursor:
            select_table_query = issue
            cursor.execute(select_table_query)
            rows = cursor.fetchall()
            for row in rows:
                print(row)
    if x == 'да':
        print('Введите фамилию кассира:')
        x = input()
        issue = 'SELECT * from coffee_drinks_sell where drink_name = ' \
                '' + a + str(name_d) + a + 'and' + ' employee_surname' + '=' + a + str(x) + a
        connection = pymysql.connect(
            host=host,
            port=3306,
            user=user,
            password=password,
            database=db_name,
            cursorclass=pymysql.cursors.DictCursor
        )
        with connection.cursor() as cursor:
            select_table_query = issue
            cursor.execute(select_table_query)
            rows = cursor.fetchall()
            for row in rows:
                print(row)






