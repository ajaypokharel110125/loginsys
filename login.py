import json
import hashlib
import register
import change_pass
with open('userinfo.json') as f:
    user_data = json.load(f)


def valid_user(username):
    for key in user_data.keys():
        if username == key:
            return True


def valid_password(password):
    hash_password = hashlib.sha256(password.encode()).hexdigest()
    for value in user_data.values():
        if hash_password == value:
            return True


def user_login():
    print('         WELCOME TO THE LOGIN SYSTEM         ')
    username = input('Please enter your username --> ')
    password = input('Please enter your password--> ')

    if valid_user(username) and valid_password(password):
        print('You have successfully logged in!')
    elif not valid_user(username):
        print("Username not found! Please try again or Register if you are not yet registered!")
        choice = input('''
        Click one of these:
            1) Try Logging in again
            2) Register into our system
        --> ''')
        if choice == '1':
            user_login()
        elif choice == '2':
            register.save_user()

    elif valid_user(username) and not valid_password(password):
        n_choice = input('''Incorrect password. Choose one of these: 
        1) Try logging in again
        2) Forgot password
        ''')
        if n_choice == '1':
            user_login()
        elif n_choice == '2':
            change_pass.change()


if __name__ == '__main__':
    user_login()
