import hashlib
import json
# import login

with open('userinfo.json', 'r') as file:
    user_info = json.load(file)


def check_user(fullname):
    for key in user_info.keys():
        if fullname == key:
            return True


def create_pass():
    y_pass = input('''Note that your password must be at least 5 characters long, have an uppercase, 
    and should contain one of these symbols: @, #, $ Enter your password here: ''')
    return y_pass


def pass_upper(password):
    result = False
    for x in password:
        if 'A' <= x <= 'Z':
            result = True
            break
    return result


def pass_symbol(password):
    result = False
    for x in password:
        if x == '@' or x == '#' or x == '$':
            result = True
            break
    return result


def validate_pass(password):
    if len(password) >= 5:
        if pass_upper(password) and pass_symbol(password):
            return True


def hash_pass(password):
    # x_pass = base64.b64encode(password.encode("utf-8"))
    x_pass = hashlib.sha256(password.encode()).hexdigest()
    return x_pass


def save_user():
    """
    this will ask user for username and password and save username and password in the following format:
    {username: hash(password)}
    """
    print('   WELCOME TO THE USER REGISTERING SYSTEM!   ')

    first_name = input('Please Enter your first name --> ')
    last_name = input('Please Enter your last name --> ')
    user_name = first_name + " " + last_name

    if check_user(user_name):
        print('You are already a registered user. Go to Login! ')
        # login.user_login()

    if not check_user(user_name):
        user_password = create_pass()
        if validate_pass(user_password):
            hashed_pass = hash_pass(user_password)
            user_info[user_name] = hashed_pass
            print('CONGRATS!!! YOU HAVE BEEN REGISTERED INTO OUR SYSTEM.')
            print(f'Your username is {user_name} and your password is {user_password}')
            with open('userinfo.json', 'w') as f:
                json.dump(user_info, f, indent=2)
        elif not validate_pass(user_password):
            if not len(user_password) >= 5:
                print('The password must have at least 5 characters. Try registering again!')
                save_user()
            elif not pass_symbol(user_password):
                print('The password does not contain @, #, $. Try registering again!')
                save_user()
            elif not pass_upper(user_password):
                print('The password does not have at least one upper case letters. Try registering again!')
                save_user()


if __name__ == '__main__':
    save_user()
