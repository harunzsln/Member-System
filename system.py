import json
from random import randint

class System:
    def __init__(self):
        self.status = True
        self.datas = self.getData()


    def run(self):
        self.showMenu()
        self.chooseOption()
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
        except FileNotFoundError:
            with open("users.json", "w") as file:
                file.write("{}")

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
        pass
    def exit(self):
        pass
    def check(self,username,password):
        self.datas = self.getData()

        for user in self.datas["users"]:
            if user["username"] == username and user["password"] == password and user["timeout"] == "" and user["isActive"] == True:
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

