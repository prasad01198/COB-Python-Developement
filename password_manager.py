from cryptography.fernet import Fernet
import json
import getpass

class PasswordManager:
    def __init__(self, key="secret.key", data_file="passwords.json"):
        self.key = key
        self.data_file = data_file
        self.manage_key()

    def manage_key(self):
        try:
            with open(self.key, "rb") as key:
                self.key = key.read()
        except FileNotFoundError:
            self.key = Fernet.generate_key()
            with open(self.key, "wb") as key:
                key.write(self.key)

    def encrypt(self, data):
        cipher = Fernet(self.key)
        enc_password = cipher.encrypt(data.encode())
        return enc_password

    def decrypt(self, enc_password):
        cipher = Fernet(self.key)
        dec_password = cipher.decrypt(enc_password).decode()
        return dec_password

    def load_passwords(self):
        try:
            with open(self.data_file, "rb") as file:
                enc_password = file.read()
            dec_password = self.decrypt(enc_password)
            return json.loads(dec_password)
        except (FileNotFoundError, json.JSONDecodeError):
            return {}

    def save_pass(self, passwords):
        enc_password = self.encrypt(json.dumps(passwords))
        with open(self.data_file, "wb") as file:
            file.write(enc_password)

    def add_pass(self, service, username, password):
        passwords = self.load_passwords()
        if service not in passwords:
            passwords[service] = {}
        passwords[service][username] = password
        self.save_pass(passwords)

    def ret_pass(self, service, username):
        passwords = self.load_passwords()
        return passwords.get(service, {}).get(username)

if __name__ == "__main__":
    password_manager = PasswordManager()

    while True:
        # print("\nWhat do you want to do? :")
        print("1. Add a new password")
        print("2. Retrieve a password")
        print("3. Exit")

        choice = input("What do you want to do?  (1/2/3): ")

        if choice == "1":
            service = input("Enter the service or website name: ")
            username = input("Enter your username: ")
            password = getpass.getpass("Enter your password: ")
            password_manager.add_pass(service, username, password)
            print("Password added successfully!")

        elif choice == "2":
            service = input("Enter the service or website name: ")
            username = input("Enter your username: ")
            saved_password = password_manager.ret_pass(service, username)
            if saved_password:
                print(f"Username: {username}")
                print(f"Password: {saved_password}")
            else:
                print(f"No password found for {service} and username {username}")

        elif choice == "3":
            print("Exiting Password Manager. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter 1, 2, or 3.")