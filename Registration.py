class Registration:
    def __init__(self, login, password):
        self.password = password
        self.login = login

    @property
    def password(self):
        return self.__password
    @password.setter
    def password(self,value):
        if not type(value) is str:
            raise TypeError("Must be a string")
        if len(value)<4 or len(value)>12:
            raise ValueError("Password length must be between 4 and 12")
        self.is_include_digit(value)
        self.is_include_all_register(value)
        self.check_passwor_dictionary(value)
        self.__password=value

    @property
    def login(self):
        return self.__login
    @login.setter
    def login(self,value):
        if value.count('@')!=1 or value.count('.')!=1:
            raise ValueError('Login must include at least one @')
        self.__login = value

    @staticmethod
    def is_include_digit(value):
        r = 0
        for elem in value:
            if elem.isdigit():
                r += 1
        if r== 0:
            raise ValueError("Must contain at least one digit")
        return True

    @staticmethod
    def is_include_all_register(value):
        r = 0
        for elem in value:
            if elem in ascii_uppercase:
                r += 1
        if r <1:
            raise ValueError("Must contain at least two UpperCase")

    @staticmethod
    def check_passwor_dictionary(value):
        with open("easy_passwords.txt") as my_file:
            for line in my_file:
                if line.strip()==value:
                    raise ValueError("Easy password")
        return True
