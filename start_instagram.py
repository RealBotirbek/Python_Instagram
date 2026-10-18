from Data_db import add_account, add_post, get_posts, add_view
from Account import Account

def start_project():
    name = 'Botirbek' #input('Name: ')
    last_name = 'Abduxalimov' #input('Last name: ')
    date_of_birth = '2008-12-10' #input('Date of birth: ')
    username = 'botirbek' #input('Username: ')
    phone_number = 996942040 #int(input('Phone number: '))
    email = 'botirbek@gmail.com' #input('Email: ')
    password = '123456' #input('Password: ')
    new_account = Account(name, last_name, date_of_birth, username, phone_number, email, password)
    account_id = add_account(name, last_name, date_of_birth, username, phone_number, email, password)
    while True:
        choice = int(input('''
0 exit
1 Post
2 View posts
'''))
        match choice:
            case 0: break
            case 1:
                title = input('Post title: ')
                content = input('Your post: ')
                new_account.create_post(title, content)
                post_id = add_post(title, content, account_id)
            case 2: get_posts()
start_project()