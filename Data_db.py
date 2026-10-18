from dbname import get_connection

def add_account(name,last_name,date_of_birth,username,phone_number,email,password):
    connection = get_connection()
    cursor = connection.cursor()
    try:
        cursor.execute('''
        insert into account(name,last_name,date_of_birth,username,phone_number,email,password) 
        values(%s,%s,%s,%s,%s,%s,%s) returning id''', (name,last_name,date_of_birth,username,phone_number,email,password))
        account_id = cursor.fetchone()[0]
        return account_id
    finally:
        connection.commit()
        connection.close()
        cursor.close()


def add_post(title, content, account_id):
    connection = get_connection()
    cursor = connection.cursor()
    try:
        cursor.execute('''insert into posting(account_id, title, content) 
        values(%s, %s, %s) returning id''',(account_id, title, content))
        post_id = cursor.fetchone()[0]
        return post_id
    finally:
        connection.commit()
        connection.close()
        cursor.close()

def add_like(post_id, account_id):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute('''insert into liking(post_id, account_id) 
        values(%s, %s)''', (post_id, account_id))
    connection.commit()
    connection.close()
    cursor.close()

def add_view(post_id, account_id):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute('''insert into viewing(post_id, account_id) 
        values(%s, %s)''', (post_id, account_id))
    connection.commit()
    connection.close()
    cursor.close()

def add_follow(from_account_id, to_account_id):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute('''insert into following(from_account_id, to_account_id) 
        values(%s, %s)''', (from_account_id, to_account_id))
    connection.commit()
    connection.close()
    cursor.close()

def get_posts():
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute('''
    select a.name, a.last_name, p.title, p.content from account a
    inner join posting p on a.id = p.account_id''')
    all_posts = cursor.fetchall()
    for a in all_posts:
        print(f"""
{a[0]} {a[1]}
{a[2]}:
{a[3]}""")
        input()
