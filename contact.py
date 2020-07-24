import sqlite3


def create(sqliteConnection):
    try:
        cursor = sqliteConnection.cursor()
        sqlite_Query = 'create table if not exists ' \
                       'contacts(name text,number integer )'
        cursor.execute(sqlite_Query)
        cursor.close()
    except sqlite3.Error as error:
        print('Error while connecting to sqlite', error)


def add_contact(sqliteConnection, Name, num):
    try:
        cursor = sqliteConnection.cursor()
        cursor.execute('select * from contacts where Name=? ', (Name,))
        records = cursor.fetchall()
        if not records:
            cursor.execute('insert into contacts values(?,?)', (Name, int(num)))
            print('Contact Inserted.')
        else:
            print('Contact Already Exists.')
        sqliteConnection.commit()
        cursor.close()
    except sqlite3.Error as error:
        print("Error while connecting to sqlite ", error)
    except ValueError as e:
        print('Error: Give appropriate input')


def display_contacts(sqliteConnection):
    try:
        cursor = sqliteConnection.cursor()
        cursor.execute('select * from contacts')
        check = cursor.fetchall()
        if check is None:
            print("No Contacts present.")
        elif len(check) == 0:
            print('List is empty\nYou can create your first contact by pressing 1')
        else:
            print("Contacts list:")
            for i in check:
                print('Name   : ', i[0])
                print('Contact: ', i[1])

        sqliteConnection.commit()
        cursor.close()
    except sqlite3.Error as error:
        print("Error while connecting to sqlite", error)


def serch(sqliteConnection, name):
    try:
        cursor = sqliteConnection.cursor()
        cursor.execute('select * from contacts where name like ?', ('%{}%'.format(name),))
        records = cursor.fetchall()
        if not records:
            print('Contact does not exist\n You can create by pressing 1')
        else:
            for r in records:
                print('Name   : ', r[0])
                print('Contact:', r[1])
        sqliteConnection.commit()
        cursor.close()
    except sqlite3.Error as error:
        print("Error while connecting to sqlite", error)


def update_contacts(sqliteConnection, newName, number):
    try:
        cursor = sqliteConnection.cursor()
        cursor.execute('select * from contacts where Name=?', (newName,))
        records = cursor.fetchone()

        if records is None:
            print('No Contact present\nYou can create by pressing 1')

        else:
            cursor.execute('update contacts set Number=? where Name=?', (int(number), newName))
            print("Contact Updated Successfully")
        sqliteConnection.commit()
        cursor.close()
    except sqlite3.Error as error:
        print("Error while connecting to sqlite", error)

    except ValueError as e:
        print('Error: Give appropriate input')


def delete_contact(sqliteConnection, name):
    try:
        cur = sqliteConnection.cursor()
        cur.execute('select * from contacts where Name=?', (name,))
        check = cur.fetchone()
        if check is None:
            print("contact not found\nYou can create by pressing 1")
        else:
            cur.execute('delete from contacts where Name=?', (name,))
            print("contact  deleted")

        sqliteConnection.commit()
        cur.close()
    except sqlite3.Error as error:
        print("Error while connecting to sqlite", error)


def close_contact(sa):
    sa.close()
