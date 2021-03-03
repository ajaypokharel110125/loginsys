import json
import hashlib
import register

with open('userinfo.json', 'r') as file:
    user_info = json.load(file)


def valid_user(user):
    for key in user_info.keys():
        if user == key:
            return True


def change():
    username = input('Enter your username: ')
    if valid_user(username):
        new_password = input('Enter a new password. Note that your password must be at least 5 characters long, '
                             'have an uppercase, and should contain one of these symbols: @, #, $ --->')
        upp = register.pass_upper(new_password)
        sym = register.pass_symbol(new_password)
        valid = register.validate_pass(new_password)

        if valid:
            for key in user_info.keys():
                user_info.pop(key)
                h_password = hashlib.sha256(new_password.encode()).hexdigest()
                user_info[username] = h_password
                with open('userinfo.json', 'w') as f:
                    json.dump(user_info, f, indent=2, sort_keys=key)
                print('You have successfully changed your password!')

        elif not valid:
            if not len(new_password) >= 5:
                print('The password must have at least 5 characters. Try registering again!')
                change()
            elif not sym:
                print('The password does not contain @, #, $. Try registering again!')
                change()
            elif not upp:
                print('The password does not have at least one upper case letters. Try registering again!')
                change()

    else:
        print('Username not found! Please try again.')
        change()


if __name__ == '__main__':
    change()
