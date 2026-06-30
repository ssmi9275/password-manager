#V00709275 Sydney Smith
from cryptography.fernet import Fernet
key = Fernet.generate_key()
with open("key.key", "wb") as key_file:
    key_file.write(key)
with open("key.key", "rb") as key_file:
    key = key_file.read()
fernet = Fernet(key) 
def save_password(account, username, password):
    encrypted_password = fernet.encrypt(password.encode())
    with open("passwords.txt", "a") as file:
        file.write(f"{account},{username},{encrypted_password.decode()}\n")
def retrieve_password(account):
    with open("passwords.txt", "r") as file:
        for line in file:
            acc, user, enc_password = line.strip().split(",")
            if acc == account:
                decrypted_password = fernet.decrypt(enc_password.encode()).decode()
                return f"Username: {user}, Password: {decrypted_password}"
    return "Account not found." 
while True:
    choice = input("Enter 'save' to store a password or 'get' to retrieve one (or 'exit' to quit):").strip()
    if choice == "save":
        account = input("Enter account name: ")
        username = input("Enter username: ")
        password = input("Enter password: ")
        save_password(account, username, password)
    elif choice == "get":
        account = input("Enter account name: ")
        print(retrieve_password(account))
    elif choice == "exit":
        break
else:
    print("Invalid choice. Try again.")