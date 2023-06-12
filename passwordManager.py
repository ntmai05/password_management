from cryptography.fernet import Fernet

master_pwd = input("What is your master password?" )

def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

def view():
    with open("passwords.txt", 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split("|")
            print("User: ",user, ", Password: ",passw)


def add():
    name = input("Please enter your account name: ")
    pwd = input("Please enter associated password: ")
    with open('passwords.txt', 'a') as f:
        f.write(name + "|" + pwd + "\n")

while True:
    mode = input("Would you like to add new or view existing ones (view,add), press q to quit?").lower()
    if mode == 'q':
        break
    if mode == 'view':
        view()
    elif mode == 'add':
        add()
    else:
        print("Invalid mode selected")
        continue