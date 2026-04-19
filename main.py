class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

class LoginSystem:
    def __init__(self):
        self.users = {}

    def register(self, username, password):
        if username in self.users:
            print("Foydalanuvchi allaqachon mavjud")
        else:
            self.users[username] = User(username, password)
            print("Foydalanuvchi muvaffaqiyatli ro'yxatdan o'tdi")

    def login(self, username, password):
        if username in self.users:
            if self.users[username].password == password:
                print("Foydalanuvchi muvaffaqiyatli kirishdi")
            else:
                print("Parol noto'g'ri")
        else:
            print("Foydalanuvchi topilmadi")

    def change_password(self, username, old_password, new_password):
        if username in self.users:
            if self.users[username].password == old_password:
                self.users[username].password = new_password
                print("Parol muvaffaqiyatli o'zgartirildi")
            else:
                print("Eski parol noto'g'ri")
        else:
            print("Foydalanuvchi topilmadi")

    def delete_user(self, username, password):
        if username in self.users:
            if self.users[username].password == password:
                del self.users[username]
                print("Foydalanuvchi muvaffaqiyatli o'chirildi")
            else:
                print("Parol noto'g'ri")
        else:
            print("Foydalanuvchi topilmadi")

def main():
    login_system = LoginSystem()
    while True:
        print("1. Ro'yxatdan o'tish")
        print("2. Kirish")
        print("3. Parolni o'zgartirish")
        print("4. Foydalanuvchini o'chirish")
        print("5. Chiqish")
        choice = input("Tanlang: ")
        if choice == "1":
            username = input("Username: ")
            password = input("Parol: ")
            login_system.register(username, password)
        elif choice == "2":
            username = input("Username: ")
            password = input("Parol: ")
            login_system.login(username, password)
        elif choice == "3":
            username = input("Username: ")
            old_password = input("Eski parol: ")
            new_password = input("Yangi parol: ")
            login_system.change_password(username, old_password, new_password)
        elif choice == "4":
            username = input("Username: ")
            password = input("Parol: ")
            login_system.delete_user(username, password)
        elif choice == "5":
            break
        else:
            print("Noto'g'ri tanlov")

if __name__ == "__main__":
    main()