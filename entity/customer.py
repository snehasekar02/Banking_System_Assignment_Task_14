class Customer:
    def __init__(self, customer_id: int, first_name: str, last_name: str, dob: str, email: str, phone: str, address: str):
        self.customer_id = customer_id
        self.first_name = first_name
        self.last_name = last_name
        self.dob = dob
        self.email = email
        self.phone = phone
        self.address = address

    def get_customer_id(self):
        return self.customer_id

    def set_customer_id(self, customer_id):
        self.customer_id = customer_id

    def get_first_name(self):
        return self.first_name

    def set_first_name(self, first_name):
        self.first_name = first_name

    def get_last_name(self):
        return self.last_name

    def set_last_name(self, last_name):
        self.last_name = last_name

    def get_dob(self):
        return self.dob

    def set_dob(self, dob):
        self.dob = dob

    def get_email(self):
        return self.email

    def set_email(self, email):
        self.email = email

    def get_phone(self):
        return self.phone

    def set_phone(self, phone):
        self.phone = phone

    def get_address(self):
        return self.address

    def set_address(self, address):
        self.address = address

    def __str__(self):
        return f"Customer ID: {self.customer_id}, Name: {self.first_name} {self.last_name}, DOB: {self.dob}, Email: {self.email}, Phone: {self.phone}, Address: {self.address}"
