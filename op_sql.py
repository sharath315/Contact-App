from contact import *

sqliteConnection = sqlite3.connect('contacts.db')
create(sqliteConnection)
ops = {
    1: add_contact,
    2: display_contacts,
    3: serch,
    4: update_contacts,
    5: delete_contact,
    6: close_contact
}

while True:
    print()
    c = int(input('Enter a number \n'
                  '1:Add a new contact\n'
                  '2:display table\n'
                  '3:serch numbers\n'
                  '4:update a contact\n'
                  '5:delete a contact\n'
                  '6:close \n'
                  ))
    fn = ops.get(c)
    if c == 6:
        print('Contact app closed\n***Thankyou***')
        close_contact(sqliteConnection)
        break

    elif fn is None:
        print('Invalid operation')
        continue
    elif c == 1:
            name = input('Enter name: ')
            num = input('Enter number: ')
            fn(sqliteConnection, name, num)

    elif c == 3:
        name = input('Enter name: ')
        fn(sqliteConnection, name)
    elif c == 4:
            name = input('Enter name: ')
            num = input('Enter number: ')
            fn(sqliteConnection, name, num)
    elif c == 5:
        name = input('Enter name whose contact has to be deleted: ')
        fn(sqliteConnection, name)
    elif c == 2:
        display_contacts(sqliteConnection)
    else:
        print('Enter number between 1 to 6')
        pass
