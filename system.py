import json
from random import randint

class System:
    def __init__(self):
        self.status = True
        self.datas = self.getData()


    def run(self):
        self.showMenu()
        choose = self.chooseOption()

        if choose == 1:
            self.signIn()
        if choose == 2:
            self.logIn()
        if choose == 3:
            self.forgetPassword()
        if choose == 4:
            self.exit()
        

    def showMenu(self):
        print("""
        1. Sign In
        2. Log In
        3. Forget Password
        4. Exit""")
        
    def chooseOption(self):
        while True:
            try:
                choose = int(input("Please choose an option: "))
                while choose not in [1, 2, 3, 4]:
                    choose = int(input("Please choose an option between 1 and 4: "))
                break
            except ValueError:
                print("Invalid input. Please enter a number.\n")

        return choose
        
    def getData(self):
        try:
            with open("users.json", "r") as file:
                datas = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            with open("users.json", "w") as file:
                file.write("{}")

            with open("users.json", "r") as file:
                datas = json.load(file)   

        return datas



    def signIn(self):
        username = input("Please enter your username: ")
        password = input("Please enter your password: ")

        status = self.check(username, password)
        if status:
            self.loginSuccess()
        else:
            self.loginFailed("Invalid username or password. Please try again.")

    def logIn(self):
        username = input("Please enter your username: ")
        while True:
            password = input("Please enter your password: ")
            passwordAgain = input("Please enter your password again: ")
            if password == passwordAgain:
                break
            else:
                print("Passwords do not match. Please try again.")

        email = input("Please enter your email: ")

        status = self.isRegistered(username, email)

        if status:
            print("This username and email are already registered. Please try again.")
        else:
           activationCode = self.sendActivationCode(username)
           activationStatus = self.checkActivation(activationCode)
           
           if activationStatus:
                self.submit(username, password, email)
           else:
                print("Invalid activation code.")


    def forgetPassword(self):

        mail = input("Please enter your email: ")
        
        if self.isMailExist(mail):
            with open("activation.txt", "w") as file:
                activation = str(randint(10000, 99999))
                file.write(activation)

            actCodeInput = input("Please enter the activation code sent to your email to reset your password: ")    

            if actCodeInput == activation:
                while True:
                    newPassword = input("Please enter your new password: ")
                    newPasswordAgain = input("Please enter your new password again: ")
                    if newPassword == newPasswordAgain:
                        break
                    else:
                        print("Passwords do not match. Please try again.")
            self.datas = self.getData()

            for user in self.datas["users"]:
                if user["mail"] == mail:
                    user["password"] = str(newPassword)
            with open("users.json", "w") as file:
                json.dump(self.datas, file)
                print("Your password has been reset successfully!")
        
        else:
            print("There is no user with this email. Please try again.")

        

    def isMailExist (self,mail):
        self.datas = self.getData()
        for kullanici in self.datas["users"]:
            if kullanici["mail"] == mail:
                return True
        return False

    def exit(self):
        self.status = False


    def check(self,username,password):
        self.datas = self.getData()

        for user in self.datas["users"]:
            if user["username"] == username and user["password"] == password and user["timeout"] == "0" and user["isActive"] == True:
                return True
        return False
    


    def isTimeOut(self):
        pass

    def isActive(self):
        pass

    def loginFailed(self, reason):
        print(f"Login failed: {reason}")

    def loginSuccess(self):
        print("Login successful!")
        self.status = False

    def isRegistered(self,username,email):
        
        self.datas = self.getData()

        try:
            for user in self.datas["users"]:
                if user["username"] == username and user["email"] == email:
                    return True
        except KeyError:
            return False
        
        return False
    
    def registerFailed(self):
        pass

    def sendActivationCode(self,username):
        with open("activation.txt", "w") as file:
            activation = str(randint(100000, 999999))
            file.write(activation)
        return activation

            

    def checkActivation(self,activationCode):
        getActivation = input("Please enter the activation code sent to your email: ")
        if activationCode == getActivation:
            return True
        else:
            return False

    def submit(self, username, password, email):
        self.datas = self.getData()

        try:
            self.datas["users"].append({"username": username, "password": password, "email": email, "timeout": "0", "isActive": True})
        except KeyError:
            self.datas["users"] = [{"username": username, "password": password, "email": email, "timeout": "0", "isActive": True}]
        
        with open("users.json", "w") as file:
            json.dump(self.datas, file)
            print("Registration successful!")

system = System()

while system.status:
    system.run()

