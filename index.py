# to create file if it doesnot exit...
import os
import getpass

if not os.path.exists('record.txt'):
    file = open('record.txt','w')
    file.close()

def register():
    username = input('Enter username: ')
    if username in open('record.txt','r').read():
        print('username already exist')
        message = input('Do you want to continue y/N: ')
        if message == 'y':
            register()
            exit()
        else:
            exit()

    password = getpass.getpass("Enter passwords: ")
    confirm_password = getpass.getpass("Enter confirm password" )
    if password != confirm_password:
        print("password not match")
        exit()

    try:
        handle = open('record.txt','a')
        handle.write(username)
        handle.write(' ')
        handle.write(password)
        handle.write('\n')
        print('user was successfully registered')
    except Exception as error:
        print(error)
    finally:
        handle.close()

register()