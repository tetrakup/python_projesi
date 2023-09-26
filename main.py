import datetime

users = {
    'ahmedaccount': {"Name": "Ahmed", "Password": 1234, "Balance": 1000},
    'zeynepaccount': {"Name": "Zeynep", "Password": 4321, "Balance": 1000},
    'albertoaccount': {"Name": "Alberto", "Password": 4422, "Balance": 1000}
}

admin = {"Name": "İbrahim", "Password": "1122"}

def timee():
    time = datetime.datetime.now()
    return time

def guidance(try_login):
    choose4 = input("""
    1. Press "1" to return to the main menu.
    2. Press "2" to exit.""")
    if choose4 == "1":
        return second_menu(try_login)
    else:
        print("Istinye Bank wishes you a good day..")

def second_menu(try_login):
    print(f'Welcome to Sehir Bank, {try_login}! Please enter the number of the service:')
    choose3 = input("""
    1. Withdraw Money
    2. Deposit Money
    3. Transfer Money
    4. My Account Information
    5. Logout""")
    
    if choose3 == "1":
        withdraw = int(input("Please enter the amount you want to withdraw: "))
        if users[f'{try_login}account']['Balance'] < withdraw:
            print("Yetersiz bakiye, lütfen tekrar deneyiniz. Güncel bakiyeniz:", users[f'{try_login}account']['Balance'])
            guidance(try_login)
        else:
            users[f'{try_login}account']['Balance'] -= withdraw
            print("Geriye kalan bakiyeniz: {}".format(users[f'{try_login}account']['Balance']))
            guidance(try_login)
    
    if choose3 == "2":
        deposit = int(input("Lütfen yatırmak istediğiniz miktarı giriniz: "))
        users[f'{try_login}account']['Balance'] += deposit
        print("Your current balance is {} TL.".format(users[f'{try_login}account']['Balance']))
        guidance(try_login)
    
    if choose3 == "3":
        havale = input("Lütfen EFT yapılacak hesabı seçiniz: ")
        while not (havale != f'{try_login}account' and havale in users.keys()):
            print("Kendi hesabınıza para gönderemezsiniz veya hatalı giriş yaptınız. Lütfen tekrar deneyiniz.")
            havale = input("Lütfen EFT yapılacak hesabı seçiniz: ")
        
        eft = int(input("Göndermek istediğiniz miktarı giriniz: "))
        while not (users[f'{try_login}account']['Balance'] >= eft):
            print("Yetersiz bakiye, lütfen tekrar deneyiniz. Güncel bakiyeniz:", users[f'{try_login}account']['Balance'])
            eft = int(input("Göndermek istediğiniz miktarı giriniz: "))
        
        users[f'{try_login}account']['Balance'] -= eft
        users[havale]['Balance'] += eft
        print("İşleminiz başarıyla gerçekleşti. Yeni bakiyeniz: {}".format(users[f'{try_login}account']['Balance']))
    
    if choose3 == "4":
        print("Hesap bilgileriniz:", users[f'{try_login}account'])
    
    if choose3 == "5":
        print("Istinye Bank wishes you a good day..")

def login(users):
    global try_login
    try_login = input("Please login your name: ")
    if f'{try_login.lower()}account' in users:
        try_pass = input("Password: ")
        if int(try_pass) == users[f'{try_login.lower()}account']["Password"]:
            print(f'Sisteme hoş geldin {try_login.lower()}')
            return second_menu(try_login)
        else:
            print("Hatalı giriş yaptınız, lütfen tekrar deneyiniz.")
            return login(users)

def admin_menu(bank_user):
    print(f'Welcome {admin["Name"]}! Please enter the number of the service:')
    choose1 = input("""
    1. Create Account
    2. Delete Account
    3. See Accounts
    4. Log Out""")
    
    if choose1 == "1":
        return create_account(bank_user)
    
    if choose1 == "2":
        return admin_delete(try_login)
    
    if choose1 == "3":
        return bilgi_goruntule(bank_user)
    
    else:
        print("Hatalı giriş yaptınız. Lütfen tekrar deneyiniz.")

def admin_delete(try_login):
    delete = input("Lütfen silmek istediğiniz account name'i yazınız: ")
    if delete not in users.keys():
        print("Hatalı giriş yaptınız. {} bulunamamaktadır.".format(delete))
    if delete in users.keys():
        print(delete)
        print(users.get(delete))
        del users[delete]
        print(users)
    return guidance(try_login)

def bilgi_goruntule(bank_user):
    print("----User Lists----")
    for hesapbilgileri in bank_user:
        print(hesapbilgileri, bank_user[hesapbilgileri])

def create_account(bank_user):
    Name = input("Name: ")
    accountname = f"{Name}account".lower()
    Password = input("Password: ")
    Balance = input("Balance: ")
    bank_user[accountname] = {"Name": Name, "Password": Password, "Balance": Balance}
    return admin_menu(bank_user)

def first_menu(bank_user):
    choose2 = input("""What do you want to login as:
    1. Admin
    2. User
    3. Go Back""")
    if choose2 == "1":
        return admin_menu(bank_user)
    elif choose2 == "2":
        return login(users)
    else:
        print("Istinye Bank wishes you a good day..")

def login_admin(bank_user):
    admin_login = input("Please login your name: ")
    if f'{admin_login.lower()}account' in admin:
        admin_pass = input("Password: ")
        if admin_pass == admin["Password"]:
            print(f'Sisteme hoş geldin {admin_login.lower()}')
            return admin_menu(bank_user)
        else:
            print("Hatalı giriş yaptınız, lütfen tekrar deneyiniz.")
    return login_admin(bank_user)

bank_user = {}
bank_user = users
first_menu(bank_user)
bank_user = create_account(bank_user)

