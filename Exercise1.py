class Contacts:
    def __init__(self, name, last_name, phone='', email='', display_mode='masked'):
        self.name = name
        self.last_name = last_name
        self.phone = phone
        self.email = email
        self.display_mode = display_mode

    def __eq__(self, other):
        if not isinstance(other, Contacts):
            return False

        if not (self.name == other.name) and (self.last_name == other.last_name):
            return True

        else:
            if (self.phone and other.phone) != '':
                return self.phone == other.phone

            if (self.email and other.email) != '':
                return self.email == other.email
            else:
                return False

    def __hash__(self):
        return hash((self.name, self.last_name, self.phone, self.email))

    @staticmethod
    def _obfuscate(text):
        half_length = len(text) // 2
        return text[:half_length] + '*' * (half_length + 1)

    def __repr__(self):
        if self.display_mode == 'masked':
            return f"Contact( name = '{self._obfuscate(self.name)}' , last_name = '{self._obfuscate(self.last_name)}' )"
        else:
            return (f"Contact( name='{self.name}', last_name= '{self.last_name}',"
                    f"phone='{self.phone}',email='{self.email}'")

    def __str__(self):
        return f"{self.last_name[0]}{self.name[0]}"

    def __format__(self, format_spec):
        if format_spec != 'masked':
            return (f"Contact( name='{self.name}', last_name= '{self.last_name}',"
                    f"phone='{self.phone}',email='{self.email}'")

#
# if __name__ == '__main__':
#     c1 = Contacts('Pranax', 'Kumar', email='kumarpranav0981@gmail.com')
#     c2 = Contacts('Pranav', 'Kumar2', email='kumarpranav0981@gmail.com', display_mode='regular')
#     c3 = Contacts('Andy','Bek')
#     print(str(c3))
